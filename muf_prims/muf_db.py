from muf_arg_check import arg_check, range_check
from  muf_data_types import *
from muf_api_wrappers import *

def getprop(muf_env):
    """Get a property from an object"""
    args = arg_check(muf_env, [(Dbref), (str)],
                   ["Error: Non-object argument (1)",
                    "Error: Non-string argument (2)"])
    muf_env["stack"].append(get_props(muf_env,args[0],args[1]))

def setprop(muf_env):
    """Set a property on an object"""
    args = arg_check(muf_env, [(Dbref), (str), (str, Dbref, int, float)], ["Error: Non-object argument (1)", "Error: Non-string argument (2)", "Invalid argument type (3)"])
    set_props(muf_env,args[0],args[1],args[2])

