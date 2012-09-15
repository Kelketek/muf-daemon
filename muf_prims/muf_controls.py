from muf_arg_check import arg_check
from muf_data_types import *
def exit(muf_env):
    """Exit the current function"""
    for key, value in muf_env["jump_stack"][-1].items():
        muf_env[key]=value
    muf_env["jump_stack"].pop()
    muf_env["exec_stack"][-1].pop()
    if len(muf_env["exec_stack"][-1]) == 0:
        muf_env["exec_stack"].pop()

def for_loop(muf_env):
    """Prepare for a for loop."""
    if len(muf_env["for_stack"]) > 255:
        raise MufSoftException("FOR", "For stack overflow.")
    args = arg_check(muf_env, [(int), (int), (int)],
                   ["Starting count expected. (1)", "Ending count expected. (2)",
                    "Step count expected. (3)"])
    muf_env["for_stack"].append([args[-3], args[-2], args[-1]])
