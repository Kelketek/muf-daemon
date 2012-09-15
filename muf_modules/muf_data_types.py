import string
import re

class MufSoftException(Exception):
    """Used to define special soft exceptions in MUF."""
    pass
    
class MufRPC:
    """
    Used whenever we make an API call-- Allows us to pull out
    of execution while retaining state.
    """
    pass
    
class MufStack(list):
    """List with internal checks for overflow."""
    def push(self, muf_env, item):
        if len(self) + 1 >= 1024:
            raise MufSoftException(muf_env["code"][muf_env["instruction"][1]].upper(),
                                   "Stack overflow!")
        else:
            self.append(item)

class MufVariable:
    """Variable class for MUF."""
    def __init__(self, context, i):
        self.context=context
        self.index=i
    def __repr__(self):
        try:
            self.x=str(MufVariable.muf_env[self.context + "_list"][self.index])
        except KeyError:
            self.x="(null)"
        return self.context + str(self.index) + ":" + self.x
    def __str__(self):
        return str(self.index)
    def __add__(self, x):
        self.index += x
        return self
    def index_info(self):
        return [self.context, self.index]
    def debug_populate(self, muf_env):
        # Used for mapping variable numbers to names.
        MufVariable.muf_env=muf_env

class Dbref:
    """Database reference number class"""
    def __init__(self, site, number):
        self.db_number=number
        self.site=site
    def __str__(self):
        return str(self.db_number)
    def __add__(self, x):
        self.db_number += x
    def __repr__(self):
        return "#" + str(self.db_number)
    def get_dbref(self):
        """Get the reference number (integer)"""
        return self.db_number
    def stod(string):
        """String to DBREF"""
        match = re.match("#(\d+)\.(-?\d+)", string)
        if not match:
            raise TypeError
        else:
            return Dbref(match.group(1),match.group(2))
    def dtos(item):
        """DBREF to string"""
        return u'#' + unicode(item.site) + u'.' + unicode(item.db_number)
    def __nonzero__(self):
        if self.get_Dbref() == -1:
            return False
        else:
            return True

class Address:
    """Address for MUF function"""
    def __init__(self, name, instrnum):
        self.name=name
        self.instrnum=instrnum
    def __repr__(self):
        return "'" + self.name
    def get_addr(self):
        return [ self.instrnum, self.name ]

class marker:
    """Stackrange/Array open marker"""
    def __repr__(self):
        return "{"
    def __str__(self):
        return "0"
    def __nonzero__(self):
        return False
