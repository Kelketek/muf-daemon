from muf_arg_check import arg_check
from muf_data_types import *
def check_if_string(muf_env):
    """Checks if the top item is a string."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],str):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)

def check_if_integer(muf_env):
    """Checks if the top item is an integer."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],int):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)

def check_if_float(muf_env):
    """Checks if the top item is a float."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],float):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)

def check_if_dbref(muf_env):
    """Checks if the top item is a DBREF."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],Dbref):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)

def check_if_array(muf_env):
    """Checks if the top item is an array."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],list):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)

def check_if_dict(muf_env):
    """Checks if the top item is a dictionary."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],dict):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)

def check_if_marker(muf_env):
    """Checks if the top item is a stack range marker."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],marker):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)

def check_if_variable(muf_env):
    """Checks if the top item is a variable."""
    args = arg_checker(muf_env, [()], ["Unknown error."])
    if isinstance(args[0],MufVariable):
        muf["stack"].append(1)
    else:
        muf["stack"].append(0)
