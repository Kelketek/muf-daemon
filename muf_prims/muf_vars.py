from muf_arg_check import *
from muf_data_types import *
def grab_variable_value(muf_env):
    args = arg_check(muf_env, [(MufVariable)], ["Non-variable argument."])
    x = args[0].index_info()
    x = muf_env[x[0] + "_table"][x[1]]
    muf_env["stack"].push(muf_env,x)

def set_variable_value(muf_env):
    args = arg_check(muf_env, [(), (MufVariable)],
                   ["Unknown Error.","Non-variable argument."])
    x = args[1].index_info()
    muf_env[x[0]+"table"][x[1]]=args[0]

def variable(muf_env):
    args = arg_check(muf_env, [(int)], ["Non-integer argument"])
    muf["stack"].push(muf_env,MufVariable("V",args[0]))

def localvar(muf_env):
    args = arg_check(muf_env, [(int)], ["Non-integer argument"])
    muf["stack"].push(muf_env,MufVariable("LV",args[0]))

