import muf_arg_check
from muf_data_types import *
"""Prop import conversion module

Set of functions for type checking properties that are pulled
and for adding metadata for the types of props that will be placed.

"""

# Storago names
__forward_type_table={ unicode : "STRING", int : "INT", str : "STRING",
                       float : "FLOAT", Dbref : "DBREF" }

# Conversion functions
__back_type_table={  "INT" : int, "STRING" : unicode,
                "FLOAT" : float, "DBREF" : Dbref.stod }

# This wouldn't normally be necessary, but some MUF types need special handling.
__to_string_table={  int : unicode, str : unicode, unicode : unicode,
                     float : unicode, Dbref :  Dbref.dtos }

def restore_typed_value(muf_env,prop_type, prop_val):
    """Convert an item in a string to the specified type."""
    try:
        return __back_type_table[prop_type](prop_val)
    except TypeError:
        raise MufSoftException(muf_arg_check.get_function_name(muf_env),
                               "MUF meta data table failure. String can't be converted to specified type.")
def save_type_value(muf_env,item):
    """Returns a name for the type, and a stringified value."""
    try:
        return __forward_type_table[type(item)]
    except KeyError:
        raise MufSoftException(muf_arg_check.get_function_name(muf_env),
                               "MUF meta data table failure. Type cannot be converted.")

def stringer(muf_env,item):
    try:
        return __to_string_table[type(item)](item)
    except TypeError:
        raise MufSoftException(muf_arg_check.get_function_name(muf_env),
                               "MUF meta data table failure. Type cannot be converted.")
    
