"""Contains a dictionary list of prims whose function names cannot
be their MUF equivilent. Such as @ for grabvarval. @ is a special symbol
in Python, so we can't use it in our final dictionary of prims.
It's a little silly to have this as its own function, but I'd rather not
put it in the main body and this is easy enough to do."""
def get_translations():
    return [ ["@", "grab_variable_value"], ["for", "for_loop"], ["!", "set_variable_value"], ["}", "stack_range"],
             ["+", "plus"], ["-", "minus"], ["*", "multiply"], ["/", "divide"],
             ["%", "modulo"], ["++", "increment" ], ["--", "decrement"], ["round", "muf_round"],
             ["<", "less_than"], [">", "greater_than"], ["=", "equals"], ["<=", "less_or_equal"],
             [">=", "greater_or_equal"], ["and", "muf_and"], ["or", "muf_or"], ["not", "muf_not"],
             ["xor", "muf_xor"], ["dbref?", "check_if_dbref"], ["string?", "check_if_string"], ["int?", "check_if_integer"],
             ["float?", "check_if_float"], ["array?", "check_if_array"], ["dict?", "check_if_dict"], ["variable?", "check_if_variable"],
             ["mark?", "check_if_marker"]
           ] #List of list for more sane manipulation in this case.
