from muf_arg_check import arg_check, range_check
from  muf_data_types import *
from itertools import izip

def array_make(muf_env):
    """Create an array from a stackrange."""
    array = range_check(muf_env)
    muf_env["stack"].push(muf_env,array)

def array_make_dict(muf_env):
    """Creates a dictionary from a stackrange"""
    array = range_check(muf_env)
    if len(array) % 2 == 1:
        muf_env["stack"].push(muf_env,array.pop(0))
        # Muf drops the first item back onto the stack if the stackrange isn't even.
    i = iter(array)
    muf_env["stack"].push(muf_env,dict(zip(i, i)))

def array_explode(muf_env):
    """Breaks a MUF array into its set of key, value pairs."""
    args = arg_check(muf_env, [(list, dict)], ["Argument not an array."])
    if isinstance(args[0],list):
        count = 0
        for item in args[0]:
            muf_env["stack"].push(muf_env,count)
            muf_env["stack"].push(muf_env,item)
        muf_env["stack"].push(muf_env,len(args[0]))
    else:
        for key, value in args[0].items():
            muf_env["stack"].push(muf_env,key)
            muf_env["stack"].push(muf_env,value)
        muf_env["stack"].push(muf_env,len(args[0]))

def array_vals(muf_env):
    """Gets the values of an array."""
    args = arg_check(muf_env, [(list, dict)], ["Argument not an array."])
    if isinstance(args[0],list):
        muf_env["stack"] += args[0]
        muf_env["stack"].push(muf_env,len(args[0]))
    if isinstance(args[0],dict):
        muf_env["stack"] += args[0].values()
        muf_env["stack"].push(muf_env,len(args[0]))

def array_keys(muf_env):
    """Gets the values of an array."""
    args = arg_check(muf_env, [(list, dict)], ["Argument not an array."])
    if isinstance(args[0],list):
        muf_env["stack"] += range(0,len(args[0]))
        muf_env["stack"].push(muf_env,len(args[0]))
    if isinstance(args[0],dict):
        muf_env["stack"] += args[0].keys()
        muf_env["stack"].push(muf_env,len(args[0]))

def array_count(muf_env):
    """Gets the length of an array."""
    args = arg_check(muf_env, [(list, dict)], ["Argument not an array."])
    muf_env["stack"].push(muf_env,len(args[0]))


