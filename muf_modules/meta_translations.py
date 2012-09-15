"""Contains a dictionary list of prims whose function names cannot
be their MUF equivilent. Such as @ for grabvarval. @ is a special symbol
in Python, so we can't use it in our final dictionary of prims.
It's a little silly to have this as its own function, but I'd rather not
put it in the main body and this is easy enough to do."""
def get_translations():
    return [ ["if", "if_start"]] #List of list for more sane manipulation in this case.
