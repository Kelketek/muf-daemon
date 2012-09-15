from muf_arg_check import *
from muf_data_types import *
def greater_than(muf_env):
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type.", "Invalid argument type."])
    if arg[0] > arg[1]:
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)

def less_than(muf_env):
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type.", "Invalid argument type."])
    if arg[0] < arg[1]:
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)

def greater_or_equal(muf_env):
    args = arg_check(muf_env, [(int, float), (int, float)],
                             ["Invalid argument type.", "Invalid argument type."])
    if arg[0] >= arg[1]:
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)

def less_or_equal(muf_env):
    args = arg_check(muf_env, [(int, float), (int, float)],
                             ["Invalid argument type.", "Invalid argument type."])
    if arg[0] <= arg[1]:
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)

def equals(muf_env):
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type.", "Invalid argument type."])
    if arg[0] == arg[1]:
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)

def muf_and(muf_env):
    args = arg_check(muf_env, [(), ()], ["Unknown Error.", "Unknown Error."])
    muf_env["stack"].push(muf_env,args[0] and args[1])

def muf_or(muf_env):
    args = arg_check(muf_env, [(), ()], ["Unknown Error.", "Unknown Error."])
    muf_env["stack"].push(muf_env,args[0] or args[1])

def muf_not(muf_env):
    args = arg_check(muf_env, [()], ["Unknown Error."])
    if not args[0]:
        muf_env["stack"].push(1)
    else:
        muf_env["stack"].push(0)

def muf_xor(muf_env):
    args = arg_check(muf_env, [(), ()], ["Unknown Error.", "Unknown Error."])
    if bool(arg[0]) != bool(arg[1]):
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)
