from muf_arg_check import arg_check
from muf_data_types import *
import string, inspect, os, base64, muf_api_wrappers
from ctypes import *
#checkmatchstr=cdll.LoadLibrary(os.path.dirname(inspect.getfile(inspect.currentframe())) + "/smatch.so").equalstr
def notify(muf_env):
    """Sends a message to a player"""
    args = arg_check(muf_env, [(Dbref), (str)], ["Invalid object argument (1)", "Non-string argument (2)"])
    muf_api_wrappers.notify_objects(muf_env,args[0],args[1])

def strcat(muf_env):
    """Concatinates two strings."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument.", "Non-string argument."])
    muf_env["stack"].push(muf_env,args[0] + args[1])

def intostr(muf_env):
    """Converts an item into a string representing it."""
    args = arg_check(muf_env, [()], ["Unknown error."])
    muf_env["stack"].push(muf_env,str(args[0]))

def explode(muf_env):
    """Splits a string into several strings, using another string as a delimiter."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    if not args[1]:
        raise MufSoftException("EXPLODE", "Empty string argument (2)")
    particles = args[0].split(args[1])
    particles.reverse()
    for particle in particles:
        muf_env["stack"].push(muf_env,particle)
    muf_env["stack"].push(muf_env,len(particles))

def instr(muf_env):
    """Checks to see if a string is in another string. Returns where."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    if not args[1]:
        raise MufSoftException("INSTR", "Empty string argument (2)")
    muf_env["stack"].push(muf_env,args[0].find(args[1]) + 1)

def rinstr(muf_env):
    """Checks to see if a string is in another string. Searches in reverse."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    if not args[1]:
        raise MufSoftException("INSTR", "Empty string argument (2)")
    muf_env["stack"].push(muf_env,args[0].rfind(args[1]) + 1)

def strcmp(muf_env):
    """Compares two strings to see if they are the same."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    if args[0] == args[1]:
        muf["stack"].push(muf_env,0)
    elif args[0].find(args[1]):
        muf["stack"].push(muf_env,1)
    else:
        muf["stack"].push(muf_env,-1)

def strncmp(muf_env):
    """Compares the first x characters in a string to see if they are the same."""
    args = arg_check(muf_env, [(str), (str), (int)], ["Non-string argument.", "Non-string argument.", "Non-integer argument."])
    args[0] = args[0][0:args[3] - 1]
    args[1] = args[1][0:args[3] - 1]
    if args[0]  == args[1]:
        muf["stack"].push(muf_env,0)
    elif args[0].find(args[1]):
        muf["stack"].push(muf_env,1)
    else:
        muf["stack"].push(muf_env,-1)

def stringpfx(muf_env):
    """Checks to see if one string prefixes another."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    
    if string.lower(args[0]).find(string.lower(args[1])) == 0:
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)

def subst(muf_env):
    """Does a greedy find and replace in a string."""
    args = arg_check(muf_env, [(str), (str), (str)], ["Non-string argument (1)", "Non-string argument (2)", "Non-string argument (3)"])
    muf_env["stack"].push(muf_env,string.replace(args[0],args[2],args[1]))

def striptail(muf_env):
    """Removes trailing whitespace from a string."""
    args = arg_check(muf_env, [(str)], ["Not a string argument."])
    muf_env["stack"].push(muf_env,strings.rstrip(args[0]))

def striplead(muf_env):
    """Removes leading whitespace from a string."""
    args = arg_check(muf_env, [(str)], ["Not a string argument."])
    muf_env["stack"].push(muf_env,strings.lstrip(args[0]))

def strcut(muf_env):
    """Splits one string into two at a specified index marker."""
    args = arg_check(muf_env, [(str), (int)], ["Non-string argument (1)", "Non-integer argument (2)"])
    muf_env["stack"].push(muf_env,args[0][:args[1]])
    muf_env["stack"].push(muf_env,args[0][args[1]:])

def split(muf_env):
    """Splits a string at the first occurance of another string."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    mark = args[0].find(args[1])
    if mark == -1:
        muf_env["stack"].push(muf_env,args[0])
        muf_env["stack"].push(muf_env,"")
    else:
        muf_env["stack"].push(muf_env,args[0][:mark])
        muf_env["stack"].push(muf_env,args[0][mark + len(args[1]):])

def rsplit(muf_env):
    """Splits a string at the last occurance of another string."""
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    mark = args[0].rfind(args[1])
    if mark == -1:
        muf_env["stack"].push(muf_env,args[0])
        muf_env["stack"].push(muf_env,"")
    else:
        muf_env["stack"].push(muf_env,args[0][:mark])
        muf_env["stack"].push(muf_env,args[0][mark + len(args[1]):])

def midstr(muf_env):
    """Extracts a substring from a string from two indexes."""
    args = arg_check(muf_env, [(str), (int), (int)], ["Non-string argument (1)", "Non-interger argument (2)", "Non-integer argument (3)"])
    muf_env["stack"].push(muf_env,args[0][args[1]:args[2]])

def strlen(muf_env):
    """Gets the length of a string."""
    args = arg_check(muf_env, [(str)], ["Non-string argument."])
    muf_env["stack"].push(muf_env,len(args[0]))

def toupper(muf_env):
    """Returns a string in all uppercase."""
    args = arg_check(muf_env, [(str)], ["Non-string argument."])
    muf_env["stack"].push(muf_env,string.upper(args[0]))

def tolower(muf_env):
    """Returns a string in all lowercase."""
    args = arg_check(muf_env, [(str)], ["Non-string argument."])
    muf_env["stack"].push(muf_env,string.lower(args[0]))

def stripspaces(muf_env):
    """Truncates whitespace between words in a string."""
    args = arg_check(muf_env, [(str)], ["Non-string argument."])
    muf_env["stack"].push(string.join(args[0].split()))

"""
def smatch(muf_env):
    ""\"Checks to see if a string matches a pattern.""\"
    args = arg_check(muf_env, [(str), (str)], ["Non-string argument (1)", "Non-string argument (2)"])
    muf_env["stack"].push(checkmatchstr(args[1], args[0]))
"""

def base64encode(muf_env):
    """Encode a string into base64."""
    args = arg_check(muf_env, [(str)], ["Non-string argument."])
    muf_env["stack"].push(muf_env,base64.b64encode(args[0]))

def base64decode(muf_env):
    """decodes a string from base64."""
    args = arg_check(muf_env, [(str)], ["Non-string argument."])
    muf_env["stack"].push(muf_env,base64.b64decode(args[0]))

