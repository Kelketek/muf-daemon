from muf_arg_check import arg_check, range_check
from muf_data_types import *

def swap(muf_env):
    """Switch the top two stack items."""
    args = arg_check(muf_env, [(),()], ["Unknown error.", "Unknown error."])
    muf_env["stack"].push(muf_env,args[1])
    muf_env["stack"].push(muf_env,args[0])

def pop(muf_env):
    """Remove the top stack item."""
    arg_check(muf_env, [()], ["Unknown error."])

def dup(muf_env):
    """Duplicate the top stack item."""
    args = arg_check(muf_env, [()], ["Unknown error."])
    muf_env["stack"].push(muf_env,args[0])
    muf_env["stack"].push(muf_env,args[0])

def dupn(muf_env):
    """Duplicate an arbitrary number of items."""
    duplist = range_check(muf_env)
    for duplication in range(0,2):
        for item in duplist:
            muf_env["stack"].push(muf_env,item)

def ldup(muf_env):
    """Duplicate a full stackrange, including number."""
    duplist = range_check(muf_env)
    for duplication in range(0,2):
        for item in duplist:
            muf_env["stack"].push(muf_env,item)
        muf_env["stack"].push(muf_env,len(duplist))

def over(muf_env):
    """Push the second item from the top of the stack onto the stack again."""
    stlencheck(muf_env,2)
    muf_env["stack"].push(muf_env,muf_env["stack"][-2])

def rot(muf_env):
    """Rotate the top three items on the stack."""
    args = arg_check(muf_env, [(), (), ()],
                   ["Unknown error.", "Unknown error.", "Unknown error."])
    muf_env["stack"].push(muf_env,args[1])
    muf_env["stack"].push(muf_env,args[2])
    muf_env["stack"].push(muf_env,args[0])

def rotate(muf_env):
    """Rotate an arbitrary number of items on the stack"""
    args = arg_check(muf_env, [(int)], ["Invalid argument type."])
    stlencheck(muf_env,abs(args[0]))
    if args[0] > 0:
        item = muf_env["stack"][-args[0]]
        muf_env["stack"].pop(-args[0])
        muf_env["stack"].append(item)
    elif args[0] < 0:
        item = muf_env["stack"].pop()
        muf_env["stack"].insert(args[0] + 1,item)

def depth(muf_env):
    """Get the number of items on the stack"""
    muf_env["stack"].push(muf_env,len(muf_env["stack"]))

def reverse(muf_env):
    """Reverse a number of items on the stack."""
    revlist = range_check(muf_env)
    revlist.reverse()
    muf_env["stack"] += revlist

def lreverse(muf_env):
    """Reverse a number of items on the stack preserving original number."""
    revlist = range_check(muf_env)
    revlist.reverse()
    muf_env["stack"] += revlist
    muf_env["stack"].append(len(revlist))

def popn(muf_env):
    """Pop an arbitrary number of items off the stack."""
    args = arg_check(muf_env, [(int)], ["Non-integer argument."])
    if args[0] < 1:
        raise MufSoftException("POPN", "Invalid popn quantity.")
    stlencheck(args[0])
    for item in range(0,args[0]):
        muf_env["stack"].pop()

def pick(muf_env):
    """Push an item in the stack onto the stack again."""
    args = arg_check(muf_env, [(int)], ["Non-integer argument."])
    if args[0] < 0:
        raise MufSoftException("PICK", "Operand not a positive integer")
    stlencheck(args[0])
    muf_env["stack"].push(muf_env,muf_env["stack"][-args[0]])

def put(muf_env):
    """Replace an item on the stack."""
    args = arg_check(muf_env, [(), (int)],
                   ["Unknown error.", "Operand not a positive integer"])
    if args[1] < 0:
        raise MufSoftException("PUT", "Operand not a positive integer")
    stlencheck(args[1])
    muf_env["stack"][-args[1] + 1]=args[0]

def stack_range(muf_env):
    counter = 1
    for item in reversed(muf_env["stack"]):
        if isinstance(item, marker):
            break
        counter += 1
    else:
        raise MufSoftException("}", "No matching mark on stack!")
    muf_env["stack"].pop(-counter)
    muf_env["stack"].push(muf_env,counter - 1)
