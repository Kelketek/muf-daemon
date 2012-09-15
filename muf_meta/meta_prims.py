"""
Metaprims. These are primitives needed internally for the MUF interpreter
but which will never be called by users directly.
"""
import muf_object
from muf_data_types import *
def function(muf_env):
    func=muf_env["code"][muf_env["instruction"]][1]
    muf_env["exec_stack"][-1].append(func[0])
    # Each function on the address table has a  structure of
    # { "funcname", [ argnumber, vartable, varlist ] }
    func=muf_env["address_table"][func[0]]
    muf_env["sv_table"]=func[1]
    muf_env["sv_list"]=func[2]
    counter=0
    for counter in range(0,muf_env["code"][muf_env["instruction"]][1][1]):
        muf_env["sv_table"][counter]=muf_env["stack"][-1]
        muf_env["stack"].pop()

def execute_this(muf_env):
    if len(muf_env["exec_stack"][-1]) > 255:
        raise MufSoftException("EXEC->" +
                               muf_env["code"][muf_env["instruction"]][1],
                               "System Stack Overflow")
    muf_env["jumpstack"].append({"instruction": muf_env["instruction"],
                                 "for_stack" : muf_env["for_stack"],
                                 "sv_list" : muf_env["sv_list"],
                                 "sv_table" : muf_env["sv_table"],})
    func=muf_env["code"][muf_env["instruction"]][1]
    muf_env["instruction"]=muf_env["address_table"][func][0]
    muf_env["override"]=1

def push(muf_env):
    """Pushes a string from the instruction set onto the stack."""
    muf_env["stack"].push(muf_env,muf_env["code"][muf_env["instruction"]][1])

def variable(muf_env):
    """Pushes a variable from the instruction set onto the stack"""
    muf_env["stack"].push(muf_env,
                          muf_env["v_table"][muf_env["code"][muf_env["instruction"]][1]])

def primitive(muf_env):
    """Executes a primitive"""
    muf_env["self"].prims_list[muf_env["code"][muf_env["instruction"]][1]](muf_env)

def if_start(muf_env):
    """If conditional"""
    if not  muf_env["stack"][-1]:
        muf_env["override"] = 1
        muf_env["instruction"] = muf_env["code"][muf_env["instruction"]][1]
    muf_env["stack"].pop()

def jump(muf_env):
    """Jump to instruction"""
    muf_env["override"] = 1
    muf_env["instruction"] = muf_env["code"][muf_env["instruction"]][1]

def foriter(muf_env):
    """Iterate the for list."""
    muf_env["for_stack"][-1][0] += muf_env["for_stack"][-1][2]
    #Increments the for loop the amount specified by for.
    if muf_env["for_stack"][-1][0] >= muf_env["for_stack"][-1][1]:
        #Is the loop over?
        muf_env["stack"].push(muf_env,0)
    else:
        muf_env["stack"].push(muf_env,muf_env["for_stack"][-1][0])
        #If not, put the current count on the stack.
        muf_env["stack"].push(muf_env,1) #And a 1 to satisfy the upcoming if.

def forpop(muf_env):
    """Pop top item off for_stack"""
    muf_env["for_stack"].pop()
