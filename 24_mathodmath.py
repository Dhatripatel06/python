import math

x=float(input("enter number"))


# ceil(x)#  • Returns the smallest integer greater than or equal to x.
print(" ceil = ",math.ceil(x))


#  • copysign(x, y)#• Returns x with the sign of y
print(" copysign= ",math.copysign(x,-9))


#  • fabs(x)#  • Returns the absolute value of x
print(" fabs = ",math.fabs(x))


#  • factorial(x)#  • Returns the factorial of x
print(" factorial = ",math.factorial(int(x)))


#  • floor(x)#  • Returns the largest integer less than or equal to x
print("floor  = ",math.floor(x))


#  • fmod(x, y)#  • Returns the remainder when x is divided by y
print("fmod = ",math.fmod(x, 3))


#  • isfinite(x)#  • Returns True if x is neither an infinity nor a NaN (Not a Number)
print("isfinite  = ",math.isfinite(x))

n=int(x)
#   • isinf(x)#  • Returns True if x is a positive or negative infinity
print(" isinfinite= ",math.isinf(n))


#  • isnan(x)#  • Returns True if x is a NaN
print("is nan = ",math.isnan(n))


#  • ldexp(x, i)#  • Returns x * (2**i)
print("idexp = ",math.ldexp(x,2))


# • modf(x)#  • Returns the fractional and integer parts of x
print(" modf= ",math.modf(x))


#  • trunc(x)#  • Returns the truncated integer value of x
print(" truncat = ",math.trunc(x))

