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

def karatsuba(num1, num2):
    num_len = max(len(str(num1)), len(str(num2)))
    if num_len == 1:
        product = num1 * num2
    else:
        half_len = num_len // 2

        a = num1 // 10**(half_len)
        b = num1 % 10**(half_len)
        c = num2 // 10**(half_len)
        d = num2 % 10**(half_len)

        ac = karatsuba(a,c)
        ad = karatsuba(a,d)
        bc = karatsuba(b,c)
        bd = karatsuba(b,d)

        product = (10**(half_len*2)*ac) + (10**(half_len)*(ad + bc)) + bd
    return product


print(karatsuba(one,two))
