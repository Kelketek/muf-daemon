import inspect
import re
import sys

sys.path.append("muf_modules")
import meta_translations
import muf_api_wrappers
import muf_meta
import muf_prims
import prim_checklist
import prim_translations
import random

from muf_compiler import muf_compile
from muf_data_types import *

class muf_program:
    """
    MUF program object.
    """
    prims_list={}

    def inform(self, message):
        """Wrapper function for sending a notification to the user."""
        muf_api_wrappers.notify_objects(self.muf_env,self.muf_env["user"],message)

    def getmuf_prims(self):
        """Compiles a list of MUF prims"""
        # Get the standard prims from their module.
        muf_program.prims_list=dict(inspect.getmembers(muf_prims, inspect.isfunction))
        # Get the meta prims from their module.
        muf_program.meta_prims=dict(inspect.getmembers(muf_meta, inspect.isfunction))
        for prim_name in prim_translations.get_translations():
            # Swap out the names for prims that can't match the parsed code. Like @ and grabvarval
            muf_program.prims_list[prim_name[0]] = muf_program.prims_list.pop(prim_name[1])
        for metaname in meta_translations.get_translations():
            # Swap out the names for prims that can't match the parsed code. Like if and ifstart
            muf_program.meta_prims[metaname[0]] = muf_program.meta_prims.pop(metaname[1])

    def __init__(self, environment):
        self.muf_env=environment
        self.code=[]
        # We don't want to rebuild the prims list each time we make a MUF object.
        if not muf_program.prims_list: 
            self.getmuf_prims()
        self.compiled=0
        self.verbose=0
        self.initialized=0

    def explain(self):
        """Internal function for diagnostics."""
        print "Code:"
        print self.muf_env["rawcode"]
        print "Primslist: "
        print muf_program.prims_list
        print muf_program.meta_prims
        print self.address_table
        print "Environment:"
        print self.muf_env
        print "Compiled code:"
        print self.code

    def check_prim_status(self):
        checklist=prim_check_list.getprims_list()
        for prim in checklist:
            try:
                muf_program.prims_list[prim]
                print '{0:25}{1:10}'.format(prim, "[ \033[92mYES\033[0m ]")
            except:
                print '{0:25}{1:10}'.format(prim, "[ \033[91mNO!\033[0m ]")

    def jump_back(self):
        """Jump the execution stack back."""
        for key, value in self.muf_env["jump_stack"][-1].items():
            self.muf_env[key]=value
        self.muf_env["exec_stack"][-1].pop()


    def find_line(self, instruction):
        counter=0
        for checkpoint in self.muf_env["line_index"]:
            if instruction + 1 <= checkpoint:
                break
            else:
                counter += 1
        return counter

    def backtrace(self, instr_name, error_mesg):
        self.inform("Program Error. The program encountered the following error:")
        self.inform("testprogram, line "
                     + str(self.find_line(self.muf_env["instruction"]+ 1))
                     + "; "
                     + instr_name
                     + ": "
                     + error_mesg)
        self.inform("System stack backtrace:")
        counter=0
        for program in self.muf_env["exec_stack"][::]:
            # Unsafe to iterate on a list you're modifying.
            raw_code_list=self.muf_env["raw_code"].split("\n")
            for function in self.muf_env["exec_stack"][-1][::]:
                line=self.find_line(self.muf_env["instruction"])
                self.inform("  " + str(counter)
                            + ") " + "test_program"
                            + " line " + str(line + 1)
                            + ", in "
                            + self.muf_env["exec_stack"][-1][-1]
                            + "():")  # Arguments will go here.
                self.inform("  " + str(line + 1) + ": " + raw_code_list[line].strip())
                self.jump_back()
                counter += 1
            self.muf_env["exec_stack"].pop()
        self.inform("Done.")

    def compiler(self):
        self.result=muf_compile(self.muf_env, muf_program.prims_list)
        if not self.result[0]:
            return 1, self.result[1]
        else:
            self.result=self.result[1]
            self.compiled=1
            self.code=self.result["code"]
            self.generate_muf_env()
            var_debug=MufVariable("V", 0)
            var_debug.debug_populate(self.muf_env)
            self.address_table=self.result["address_table"]
            return 0, "OK!"

    def generate_muf_env(self):
        """Finish generating the full MUF environment.

        This should only be called once right before execution.

        """

        #Most of these are explained within the compiler object.
        self.muf_env.update({"address_table" : self.result["address_table"],
                             "code" : self.result["code"],
                             "exec_stack" : [],
                             "for_stack" : [],
                             "instr_count" : 1,
                             "jump_stack" : [{}],
                             "line_index" : self.result["line_index"],
                             "lv_table" : self.result["lv_table"], 
                             "lv_list" : self.result["lv_list"],
                             "override": 0,
                             "random"  : random.Random(),
                             "self" : self,
                             "stack" : MufStack(),
                             "start_address" : self.result["start_address"],
                             "sv_table" : [],
                             "sv_list" : {},
                             "v_table" : self.result["v_table"],
                             "v_list" : self.result["v_list"]})
        self.initialized=1

    def compile_check(self):
        """
        Check if the program is compiled. Compile if not.
        Return true or false.
        """
        if not self.compiled:
            self.compiler()
        if not self.compiled:
            return False
        return True

    def debug_send(self):
        """
        Send debug information to the user if the debug option
        is on.
        """
        if self.muf_env["debug"]:
            debugline=str(self.muf_env["stack"]) + " " +  str(self.code[self.muf_env["instruction"]])
            self.inform(debugline)

    def instruction(self):
        """
        Run a single instruction in a MUF program, incrementing all needed counters and
        checking for errors.
        """
        # Die if the limit is hit.
        if self.muf_env["instr_count"] == self.muf_env["instr_limit"]:
            self.backtrace(str(self.muf_env["code"][self.muf_env["instruction"]][1]).upper(),
                           "Instruction limit hit.")
            return 4, "Instruction limit hit."

        try:
            muf_program.meta_prims[self.code[self.muf_env["instruction"]][0]](self.muf_env)
        except MufSoftException as (instr_name, error_mesg):
            self.backtrace(instr_name, error_mesg)
            return 3, "Program error. " + instr_name + ":" + error_mesg
        except MufRPC:
            return 0, "Sleeping."
            
        if self.deferred:
            return 0, "Sleeping."

        self.muf_env["instr_count"] += 1
        self.current_slice += 1
        
        if self.muf_env["override"]:
            self.muf_env["override"]=0
        else:
            self.muf_env["instruction"] +=1

    def prep_for_exec(self):
        """
        Set some basic variables in the MUF environment in preparation for
        executing code.
        
        The first item to set is the execution stack's starting point. We need
        to make sure that the program starts on the last function that was defined.
        The MUF compiler sets any function it finds as the start_address. When it finds a
        new function, it overwrites it with a new start_address. So, whatever function was
        defined last is the starting function.
        
        Once we have that function, we check for its entry in the address_table. The address
        table has an entry for each function, all of which are lists. The first item in the list
        is the instruction where the function begins.
        
        In order to make sure debugging info is properly tracked and displayed,
        the variable class needs to be aware of the global MUF environment.
        The way to make it aware is to create a new variable object, then use its debug_populate
        function, which just sets a class-wide variable pointing to the MUF object. Now all variables
        have access to the MUF object, and can get their name from the variable tables and whatnot.
        """
        INSTRUCTION = 0
        
        self.muf_env["exec_stack"].append([])
        start_func = self.muf_env["address_table"][self.muf_env["start_address"]]
        
        self.muf_env["instruction"]=start_func[INSTRUCTION]
        
        var_debug=MufVariable("v", 0)
        var_debug.debug_populate(self.muf_env)
        del var_debug

    def execute(self, instr_slice):
        """
        Executes the current MUF object's code.
        """
        self.current_slice=0
        
        if not self.compile_check():
           return 3, "Program not compilable. Cannot run."
           
        if not self.initialized:
            self.generate_muf_env()
            
        if not self.muf_env["exec_stack"]:
            self.prep_for_exec()
        
        while self.muf_env["exec_stack"] and self.current_slice <= instr_slice:
            result = self.instruction()
            if result:
                return result

        if current_slice >= instr_slice:
            return 0, "Sleeping."
        else:
            return 2, "Program completed."
