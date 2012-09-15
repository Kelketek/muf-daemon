from muf_data_types import *
import string, re, ast
"""Muf Compiler class.

At the top of this file is a variable with a dictionary.
The following is an explination of each key and its significance:

code: This is a list of the instructions a MUF program contains.

debug_line: If an interesting event starts that can span multiple lines, this will mark
            the first one.

current_line: This contains the current line in the string we are parsing.

in_func: 1 if we're in a proceedure, 0 if we're not.

loop_stack: List used to keep track of loop syntax

if_stack: List used to keep track of if statement syntax

in_else: Has an else been declared for the current if? 1 or 0

character_number: How many characters into the source string are we?

break_list: When in a loop, this is where we keep track of all the break statements to
            fill in once we find the end.

argcount: The number of arguments a function is determined to have.

line_index: A list of transition points for new lines against instructions used for
            backtracing.

v_table: List of values for global variables

v_list: List of names for global variables

lv_table: List of values for local variables

lv_list: List of names for local variables

sv_table: List of values for scoped variables

sv_list: List of names for scoped variables

prims_table: table of all known primitives.

"""
__c = {}

def set_table():
    global __c
    __c = {  "code"       : [], "debug_line"   : 0,  "current_line"  : 1,
         "in_func"     : 0 , "loop_stack"   : [], "if_stack"      : [],
         "in_else"     : 0 , "character_number"     : 0 , "break_list"    : [],
         "argcount"   : 0 , "line_index"   : [],
         "v_list"      : [ "me" , "loc" , "trigger" , "command"  ], #v_table also exists, but is defined by the compiler from the muf environment.
         "lv_list"     : [],
         "lv_table"    : [],
         "sv_list"     : [],
         "sv_table"    : [],
         "prims_table" : {}, "address_table": {}, "start_address" : ""
      }

ifset = ["if", "else", "then"] #Conditionals must be treated specially.

loopset = ["begin", "for","repeat", "until",
         "while", "continue", "break"] #Loops are also special.

declaratories = ["var", "lvar", "var!"] #Variable declarations.

#The following is a list of prim aliases. these are prims that are just inserver defines for a set of other prims.
aliases = { "instring"  :  [["primitive", "tolower"], ["primitive", "swap"],
                            ["primitive", "tolower"], ["primitive", "swap"],
                            ["primitive", "instr"]],
            "rinstring" :  [["primitive", "tolower"], ["primitive", "swap"],
                            ["primitive", "tolower"], ["primitive", "swap"],
                            ["primitive", "instr"]],
            "stringcmp" :  [["primitive", "tolower"], ["primitive", "swap"],
                            ["primitive", "tolower"], ["primitive", "swap"],
                            ["primitive", "strcmp"]],
            "strip"     :  [["primitive", "striplead"], ["primitive", "striptail"]],
            "}list"     :  [["primitive", "}"], ["primitive", "array_make"]],
            "}dict"     :  [["primitive", "}"], ["primitive", "array_make_dict"]]
        }

def new_liner():
    """Places the current instruction number on the line_index, incriments linecount."""
    __c["line_index"].append(len(__c["code"]))
    __c["current_line"] += 1

def scan_white(source, counter):
    """Takes a point, scans until there is whitespace, reports that charcter position."""
    linecount = 0
    try: #Wrapping this in try. If we hit the end of the source code, it will raise an exception.
        while True:
            if source[counter] not in string.whitespace:
                return [counter, linecount]
            else:
                if source[counter] == "\n":
                    linecount +=1
            counter += 1
    except:
        return [counter, linecount]


def scan_non_white(source, counter):
    """Takes a start point, scans until there is a non-whitespace, reports
    that character position, and any new lines"""
    #Wrapping this in try. If we hit the end of the source code, it will raise an exception.
    try:
        while True:
            if source[counter] in string.whitespace:
                return counter
            else:
                counter += 1
    except:
        return counter

def get_next_word(source, character_number):
    """Get the next instruction, the starting point for it, and the ending point.
    Also get the number of new lines."""
    start = scan_white(source,character_number)
    linecount = start[1]
    start = start[0]
    end = scan_non_white(source,start)
    total=end - character_number
    return [source[start:end], start, end, linecount, total]

def commentator(source, character_number):
    """Disreguard comments, increase character_number."""
    closeposition=source.find(")", character_number) + 1
    __c["debug_line"] = __c["current_line"]
    if not closeposition:
        for newline in re.findall("\n",source[character_number:]):
            new_liner()
        raise Exception
    for newline in re.findall("\n",source[character_number:closeposition]):
        new_liner()
    __c["character_number"] = closeposition

def stringer(source, character_number):
    """Distill strings, increase character_number."""
    counter = 1
    switch = 1
    while switch:
        try:
            quote = ast.literal_eval(source[character_number:character_number + counter])
            switch = 0
        except SyntaxError:
            if counter > len(source):
                switch = 0
            counter += 1
    __c["character_number"] += len(quote)+ 2
    __c["code"].append(["push",quote])

def iffer(item): #Ifception!
    if item == "if":
        __c["code"].append(["if",None])
        __c["if_stack"].append(len(__c["code"]) - 1)
    elif item == "else":
        if __c["in_else"]:
            return [ 0, "ELSE without IF." ]
        else:
            __c["code"].append(["jump",None])
            __c["code"][__c["if_stack"][-1]].pop()
            __c["code"][__c["if_stack"][-1]].append(len(__c["code"]))
            __c["if_stack"].append(len(__c["code"]) - 1)
            __c["in_else"] = 1
    elif item == "then":
        if not __c["if_stack"]:
            return [ 0, "THEN without IF." ]
        else:
            __c["code"][__c["if_stack"][-1]].pop()
            __c["code"][__c["if_stack"][-1]].append(len(__c["code"]))
            if __c["in_else"]:
                __c["if_stack"].pop()
                __c["if_stack"].pop()
                __c["in_else"] = 0
            else:
                __c["if_stack"].pop()
    return [1, None]

def snap_shot_ifs(item):
    """Takes a snapshot of the if states, and resets them"""
    __c["loop_stack"].append({ "type" : item, "start" : len(__c["code"]) -1,
                               "if_stack" : __c["if_stack"], "in_else" : __c["in_else"]})
    __c["if_stack"] = []
    __c["in_else"] = 0
    __c["break_list"].append([])
    #If we're doing this, we're in a loop. Breaks will need to be filled in later.

def restore_ifs(item):
    """Restores if snapshot, fills in breaks, pops top off loop_stack and break_list."""

    if __c["if_stack"]:
        return [0, "Unterminated IF-THEN at " + item + "."]

    for breakloc in __c["break_list"][-1]:
        __c["code"][breakloc][1]=len(__c["code"])

    __c["if_stack"] = __c["loop_stack"][-1]["if_stack"]
    __c["in_else"] = __c["loop_stack"][-1]["in_else"]

    if __c["loop_stack"][-1]["type"] == "for":
        # For loops are special.
        __c["code"].append(["forpop",None])
        __c["code"][__c["loop_stack"][-1]["start"] + 1][1] = len(__c["code"])
        #Needed for the if that ends the for loop.

    __c["loop_stack"].pop()
    __c["break_list"].pop()
    return [1, None]

def looper(item):
    """Handles prims dealing with loops."""
    if item == "for":
        __c["code"].append(["primitive", "for"])
        __c["code"].append(["foriter", None])
        snap_shot_ifs(item)
        __c["code"].append(["if",None])

    elif item == "begin":
        snap_shot_ifs(item)

    elif item == "continue":
        try:
            __c["code"].append(["jump",__c["loop_stack"][-1]["start"]])
        except IndexError:
            return [0, "Can't CONTINUE outside of a loop."]

    elif item == "break":
        try:
            __c["code"].append(["jump", None])
            __c["breakstack"][-1].append(len(__c["code"]))
        except IndexError:
            return [0, "Can't have a BREAK outside of a loop."]

    elif item == "while":
        try:
            __c["code"].append(["if", None])
            __c["breakstack"][-1].append(len(__c["code"]))
        except IndexError:
            return [0, "Can't have a WHILE outside of a loop."]

    elif item == "repeat":
        try:
            __c["code"].append(["jump", __c["loop_stack"][-1]["start"]])
            loop_end = restore_ifs(item)
            if not loop_end[0]:
                return [0, loop_end[1]]
        except IndexError:
            return [0, "Loop start not found for REPEAT."]

    elif item == "until":
        try:
            __c["code"].append(["if", __c["loop_stack"][-1]["start"]])
            restore_ifs(item)
            if not loop_end[0]:
                return [0, loop_end[1]]
        except IndexError:
            return [0, "Loop start not found for UNTIL."]

    return [1, None]

def var_maker(item, source):
    """Declares a variable, sets it up in the tables."""
    if (item == "var"):
        if __c["in_func"]:
            scope = "sv"
        else:
            scope = "v"
    elif (item == "lvar"):
        if __c["in_func"]:
            return [0, "Local variable declared within procedure."]
        else:
            scope = "lv"
    elif (item == "var!"):
       if not __c["in_func"]:
           return [0, "VAR! used outside of procedure."]
       else:
           scope = "sv"

    next_word=get_next_word(source, __c["character_number"] + len(item))
    __c[scope + "_list"].append(next_word[0])
    __c[scope + "_table"].append(0) #All declared variables default to zero.
    __c["character_number"] += next_word[4] + len(item)
    __c["current_line"] += next_word[3]
    for lines in range(0, next_word[3]):
        new_liner()
    return [1, None]

def muf_compile(muf_env, prims_table):
    """Compiles a source string into a list of instructions"""
    source = muf_env["raw_code"]
    set_table()
    __c["prims_table"] = prims_table
    __c["v_table"] = muf_env["v_table"]
    while True:
        next_word = get_next_word(source, __c["character_number"])
        item = next_word[0]
        for new_line in range(0,next_word[3]):
            new_liner()
        __c["character_number"] = next_word[1]
        character_number=next_word[1]
 
        #Check for end of file first, lest we crash.
        if character_number >= len(source) or item == "":
            break

        if ( item[0] == '"' ):
            try:
                stringer(source, character_number)
            except UnboundLocalError:
                return [0, "Error in line " + str(__c["current_line"]) 
                        + ": Unterminated string found at end of line."]
            continue

        if ( item[0]  == "(" ):
            try:
                commentator(source,character_number)
            except Exception:
                return [0, "Error in line " + str(__c["current_line"]) 
                        + ": Unterminated comment starting in line "
                        + str(__c["debug_line"]) + "."]
            continue

        #Items defined by the programmer take priority.
        if string.lower(item) in __c["address_table"]:
            __c["code"].append(["executethis",string.lower(item)])
            __c["character_number"] += len(item)
            continue

        #Recognizing Variables
        found = 0
        for context in [ "sv", "lv", "v" ]:
             if string.lower(item) in __c[ context + "_list"]:
                 found=1
                 r=__c[ context + "_list"][::-1] #We have to do some fiddling to get the last occurance in a list.
                 x=len(r)-1 - r.index(item)
                 __c["code"].append(["push",MufVariable(context, x)])
                 __c["character_number"] += len(item)
                 break
        if found:
            continue

        #Declaring Variables
        if string.lower(item) in declaratories:
            vartest = var_maker(string.lower(item), source)
            if vartest[0]:
                continue
            else:
                return [0, "Error in line"
                           + str(__c["current_line"]) + ": " + vartest[1]]

        #Ifs
        if string.lower(item) in ifset:
            condstest = iffer(string.lower(item))
            if not condstest[0]:
                return [0, "Error in line " 
                           + str(__c["current_line"]) + ": " + condstest[1] ]
            else:
                __c["character_number"] += len(item)
                continue

        if string.lower(item) in loopset:
            looptest = looper(string.lower(item))
            if not looptest[0]:
                return [0, "Error in line "
                           + str(__c["current_line"]) + ": " + looptest[1] ]
            else:
                __c["character_number"] += len(item)
                continue

        #Prims
        if item in __c["prims_table"]:
            __c["code"].append(["primitive",string.lower(item)])
            __c["character_number"] += len(item)
            continue

        if item in aliases:
            for directive in aliases[item]:
                __c["code"].append(directive)
                __c["character_number"] += len(item)
            continue

        #If statements are special. We'd put them here next. For now, moving to proceedure definitions.
        #Interestingly, the compiler ignores most anything outside of a proceedure definition anyway.
        if ( item == ":" ): #There must be a space between colons and proceedure names.
            if __c["in_func"]:
                return [ 0, "Error in line " + str(__c["current_line"])
                            + ": Inception error - Definition within definition." ]
            else:
                try:
                     this_address=get_next_word(source,character_number + len(item))
                     __c["character_number"] = this_address[2]
                     for newline in range(0,this_address[3]):
                         new_liner()
                     __c["in_func"] = 1
                     __c["code"].append(["function",
                                        [string.lower(this_address[0]), __c["argcount"]]])
                     # Reminder: comment out what I was doing here, when I remember. :(
                     __c["address_table"][this_address[0]] = [len(__c["code"]) -1,
                                                              None, None]
                     __c["start_address"] = this_address[0]
                     continue
                except IndexError:
                     return [0,"Error in line " + str(__c["current_line"])
                             + ": Unexpected end of file within proceedure."]
                            # This error message isn't very clear,
                            # but it's what they used before.
        if ( item[0] == ";" ):
            if not __c["in_func"]:
                return [0,"Error in line " + str(__c["current_line"]) 
                        + ": Proceedure end without body."]
            elif __c["if_stack"]:
                return [0, "Error in line " + str(__c["current_line"])
                        + ": Unexpected end of procedure definition. (Unterminated if-then.)"]
            elif __c["loop_stack"]:
                return [0, "Error in line " + str(__c["current_line"])
                        + ": Unexpected end of procedure definition. (Unterminated loop.)"]
            else:
                __c["code"].append(["primitive","exit"])
                __c["character_number"] += 1
                __c["in_func"] = 0
                __c["address_table"][__c["start_address"]][1]=__c["sv_table"]
                __c["address_table"][__c["start_address"]][2]=__c["sv_list"]
                continue

        #Check for Dbref
        if re.match("#[0-9]+",item):
            __c["code"].append(["push",Dbref(muf_env["site_id"],int(item[1::]))])
            __c["character_number"] += len(item)
            continue

        #Check for float

        if re.match("^[0-9]*\.[0-9]+$",item):
            __c["code"].append(["push",float(item)])
            __c["character_number"] += len(item)
            continue

        #Check for integer

        if re.match("^[0-9]+$",item):
            __c["code"].append(["push",int(item)])
            __c["character_number"] += len(item)
            continue

        if item == "{":
            __c["code"].append(["push",marker()])
            __c["character_number"] += 1
            continue

        #And if we're down here, we're out of ideas.

        return [0, "Error in line " + str(__c["current_line"]) + ": Unrecognized word " + item + "."]

    #All done with the compile, just need to check a couple things for sanity...
    if len(__c["address_table"]) < 1:
        return [0, "Error on line " + str(__c["current_line"]) 
                + ": Missing procedure definition."]

    if muf_env["raw_code"] == "" :
        return [0, "Error on line " + str(__c["current_line"])
                + ": Missing program text."]

    if __c["in_func"]:
        return [0, "Error on line " + str(__c["current_line"])
                + ": Unexpected end of file."]

    return [ 1, __c ]
