"""
    Asymtotic Analysis
    High-level idea: Supress constant factors and lower-order temrs
    O(1)	constant
    O(log n)	logarithmic
    O(n)	linear
    O(n log n)	"n log n"
    O(n2)	quadratic
    O(n3)	cubic
    nO(1)	polynomial
    2O(n)	exponential

    
"""


# get product of two huge numbers using Karatsuba
import math


one = 3141592653589793238462643383279502884197169399375105820974944592
two = 2718281828459045235360287471352662497757247093699959574966967627

t1 = 2345
t2 = 6789

def karatsuba(num1, num2):
    num_len = len(str(num1))
    if num_len == 1:
        product = num1 * num2
    else:
        half_len = num_len // 2

        a = int("".join(str(num1)[: half_len]))
        b = int("".join(str(num1)[half_len :]))
        c = int("".join(str(num2)[: half_len]))
        d = int("".join(str(num2)[half_len :]))

        ac = karatsuba(a,c)
        ad = karatsuba(a,d)
        bc = karatsuba(b,c)
        bd = karatsuba(b,d)

        product = int((10**num_len *ac + 10**(num_len/2)*(ad + bc) + bd))
    return product


print(karatsuba(999,505))