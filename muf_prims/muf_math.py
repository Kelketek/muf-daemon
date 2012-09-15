from muf_arg_check import arg_check
from muf_data_types import *
import math, random
def plus(muf_env):
    """Adds two numbers"""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type", "Invalid argument type"])
    muf_env["stack"].push(muf_env,args[0] + args[1])

def minus(muf_env):
    """Subtracts one number from another"""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type", "Invalid argument type"])
    muf_env["stack"].push(muf_env,args[0] + args[1])

def multiply(muf_env):
    """Multiplies two numbers"""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type", "Invalid argument type"])
    muf_env["stack"].push(muf_env,args[0] * args[1])

def divide(muf_env):
    """Divides a number by another"""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type", "Invalid argument type"])
    try:
        muf_env["stack"].push(muf_env,args[0] / args[1])
    except ZeroDivisionError:
        muf_env["stack"].push(muf_env,0) #This is MUF's default behavior for division by 0.

def pow(muf_env):
    """Raises to a power"""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Non-float argument. (1)", "Non-float argument. (2)"])
    try:
        muf_env["stack"].push(muf_env,math.pow(args[0],args[1]))
    except ValueError:
        muf_env["stack"].push(muf_env,float('NaN'))

def modulo(muf_env):
    """Divides a number by another"""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Invalid argument type", "Invalid argument type"])
    muf_env["stack"].push(muf_env,args[0] % args[1])

def fmod(muf_env):
    """Gets the remainder from floating point division."""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Non-float argument. (1)", "Non-float argument. (2)"])
    muf_env["stack"].push(muf_env,math.fmod(args[0],args[1]))

def modf(muf_env):
    """Returns the integral and fractional parts of a number, both as floats."""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Non-float argument. (1)", "Non-float argument. (2)"])
    muf_env["stack"].push(muf_env,math.fmod(args[0],args[1]))

def atan2(muf_env):
    """Arc Tangent 2: Revenge of the trigonometric function."""
    args = arg_check(muf_env, [(int, float), (int, float)],
                   ["Non-float argument. (1)", "Non-float argument. (2)"])
    muf_env["stack"].push(muf_env,args[0] % args[1])

def increment(muf_env):
    """Adds one to a number"""
    args = arg_check(muf_env, [(int, float)], ["Invalid datatype."])
    muf_env["stack"].push(muf_env,args[0] + 1)

def decrement(muf_env):
    """Subtracts one from a number"""
    args = arg_check(muf_env, [(int, float)], ["Invalid datatype."])
    muf_env["stack"].push(muf_env,args[0] + 1)

def abs(muf_env):
    """Gets the absolute value of a number"""
    args = arg_check(muf_env, [(int)], ["Non-integer argument."])
    muf_env["stack"].push(muf_env,math.abs(args[0]))

def floor(muf_env):
    """Rounds a float down to the nearest whole number"""
    args = arg_check(muf_env, [(float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.floor(args[0]))

def ceil(muf_env):
    """Rounds a float up to the nearest whole number"""
    args = arg_check(muf_env, [(float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.ceil(args[0]))

def muf_round(muf_env):
    """Rounds a float up to a specified precision"""
    args = arg_check(muf_env, [(float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,round(args[0]))

def sqrt(muf_env):
    """Gets the square root of a number."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.sqrt(args[0]))

def sin(muf_env):
    """Gets the sine of a value in radians."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.sin(args[0]))

def cos(muf_env):
    """Gets the cosine of a value in radians."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.cos(args[0]))

def tan(muf_env):
    """Gets the tangent of a value in radians."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.tan(args[0]))

def asin(muf_env):
    """Gets the sine of a value in radians."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.asin(args[0]))
    
def acos(muf_env):
    """Gets the cosine of a value in radians."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.acos(args[0]))

def atan(muf_env):
    """Gets the tangent of a value in radians."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.atan(args[0]))

def exp(muf_env):
    """Returns e to the power of a number specified."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.exp(args[0]))

def fabs(muf_env):
    """Returns the absolute value of a number as a floating point."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    muf_env["stack"].push(muf_env,math.fabs(args[0]))

def log(muf_env):
    """Returns the natual log of a number."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    try:
        muf_env["stack"].push(muf_env,math.log(args[0]))
    except ValueError:
        muf_env["stack"].push(muf_env,math.log(float('NaN')))

def log10(muf_env):
    """Returns the log base 10 of a number."""
    args = arg_check(muf_env, [(int,float)], ["Non-float argument. (1)"])
    try:
        muf_env["stack"].push(muf_env,math.log(args[0]))
    except ValueError:
        muf_env["stack"].push(muf_env,math.log(float('NaN')))

def pi(muf_env):
    """Drops an approximation of pi onto the stack."""
    muf_env["stack"].push(muf_env,math.pi)

def frand(muf_env):
    """Pushes a random flaoting point between 0 and 1 on the stack."""
    muf_env["stack"].push(muf_env,random.random())

def random(muf_env):
    """Pushes a random number between 0 and 2,147,483,647, for compatiblity."""
    muf_env["stack"].push(muf_env,random.randint(0,2147483647))

def dist3d(muf_env):
    """Find the distance of a point in 3D space from the origin."""
    args = arg_check(muf_env, [(int, float), (int, float), (int, float)],
                             ["Non-float argument. (1)", "Non-float argument. (2)",
                              "Non-float argument. (3)"])
    muf_env["stack"].push(muf_env,math.sqrt((args[0] ** 2) + (args[1] ** 2) + (args[3] ** 2)))

def xyz_to_polar(muf_env):
    """Convert X_Y_Z coordinates to spherical coordinates."""
    args = arg_check(muf_env, [(int, float), (int, float), (int, float)],
                             ["Non-float argument. (1)", "Non-float argument. (2)",
                              "Non-float argument. (3)"])
    muf_env["stack"].push(muf_env,math.sqrt((args[0] ** 2) + (args[1] ** 2) + (args[3] ** 2)))
    muf_env["stack"].push(muf_env,math.atan2(math.sqrt((args[0] ** 2) + (args[2] ** 2)), args[1]))
    muf_env["stack"].push(muf_env,math.atan2(args[0], args[2]))

def polar_to_xyz(muf_env):
    """Convert spherical coordinates to X_Y_Z coordinates."""
    args = arg_check(muf_env, [(int, float), (int, float), (int, float)],
                             ["Non-float argument. (1)", "Non-float argument. (2)",
                              "Non-float argument. (3)"])
    muf_env["stack"].push(muf_env,args[0] * math.cos(args[1]) * math.sin(args[2]))
    muf_env["stack"].push(muf_env,args[0] * math.sin(args[1]) * math.sin(args[2]))
    muf_env["stack"].push(muf_env,args[0] * math.cos(args[2]))

def setseed(muf_env):
    """Set the seed for the random number generator."""
    args = arg_check(muf_env, [(str, tuple)], ["Invalid argument type."])
    if isinstance(args[0], str):
        muf_env["random"].setseed(args[0])
    else:
        muf_env["random"].setstate(args[0])

def getseed(muf_env):
    """Get the state from the random number generator."""
    muf_env["stack"].push(muf_env,muf_env["random"].getstate(args[0]))

def srand(muf_env):
    """Gets a random seeded number."""
    muf_env["stack"].push(muf_env,muf_env["random"].randint(-2147483648,2147483647))

def sign(muf_env):
    """Pointless prim that checks the sign of a number."""
    args = arg_check(muf_env, [(int, float)], ["Non-integer argument."])
    if args[0] < 0:
        muf_env["stack"].push(muf_env,-1)
    elif args[0] > 0:
        muf_env["stack"].push(muf_env,1)
    else:
        muf_env["stack"].push(muf_env,0)

def bitor(muf_env):
    """Performs a bitwise or on two integers."""
    args = arg_check(muf_env, [(int), (int)],
                   ["Invalid argument type", "Invalid argument type"])
    muf_env["stack"].push(muf_env,args[0] | args[1])

def bitxor(muf_env):
    """Performs a bitwise xor on two integers."""
    args = arg_check(muf_env, [(int), (int)],
                   ["Invalid argument type", "Invalid argument type"])
    muf_env["stack"].push(muf_env,args[0] ^ args[1])

def bitand(muf_env):
    """Performs a bitwise and on two integers."""
    args = arg_check(muf_env, [(int), (int)],
                   ["Invalid argument type", "Invalid argument type"])
    muf_env["stack"].push(muf_env,args[0] & args[1])

def bitshift(muf_env):
    """Performs a bitwise and on two integers."""
    args = arg_check(muf_env, [(int), (int)],
                   ["Invalid argument type", "Invalid argument type"])
    if args[1] < 0:
        muf_env["stack"].push(muf_env,args[0] >> args[1])
    else:
        muf_env["stack"].push(muf_env,args[0] << args[1])
