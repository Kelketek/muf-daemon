from muf_data_types import *

def get_function_name(muf_env):
    return muf_env["code"][muf_env["instruction"]][1].upper()

def stack_len_check(muf_env,requirement):
    if len(muf_env["stack"]) < requirement:
        raise MufSoftException(get_function_name(muf_env), "Stack underflow.")

def arg_check(muf_env, arg_list, except_list):
    """This function checks if arguments are valid and then passes back a list of them in order if they are.

    muf_env should be the MUF environment dictionary.
    arg_list should contain a list of tuples of valid types to be checked against.
    except_list contains the information the exception should contain if the item does not match.

    """
    returnlist=[]
    count=0
    stack_len_check(muf_env,len(arg_list))
    arg_list.reverse()
    for xtype in arg_list:
        if not xtype or isinstance(muf_env["stack"][-1], xtype):
            returnlist.append(muf_env["stack"][-1])
            muf_env["stack"].pop()
        else:
            raise MufSoftException(get_function_name(muf_env), except_list[count])
        count += 1
    returnlist.reverse()
    return returnlist

def range_check(muf_env):
    """Checks to make sure that the argument is a proper stackrange. If it is,
    brings the items into a list. If it isn't, brings up a proper error."""
    stack_len_check(muf_env,1)
    if not isinstance(muf_env["stack"][-1], int):
        raise MufSoftException(get_function_name(muf_env), "Invalid item count.")
    stack_len_check(muf_env,muf_env["stack"][-1])
    count=muf_env["stack"][-1]
    muf_env["stack"].pop()
    array=[]
    for item in range(0,count):
        array.append(muf_env["stack"][-1])
        muf_env["stack"].pop()
    array.reverse()
    return array
