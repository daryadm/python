from math import floor
from operator import index, indexOf

coins = [1, 2, 5]  # sorted
totalMethods = 0
amt = 7

"""
Concept: find out how many times the small elements fit into the bigger ones,
`then find the biggest possible parts of amount and add the possible combinations. 
Sort
Get number of times the el1 fits into el2, el3
Getn number of times el2 fits into el3
Get num of times el1 fits into amt + leftover
Get num of times el2 fits into amt + leftover
Get num of tiems el3 fits into amt + leftover. Check if leftover is bigger than el2, if yes

"""


def numberOfEls(el1, el2):
    n = floor(el2 / el1)
    leftover = el2 % el1
    return (n, leftover)


methods_num = 0
for i in range(0, len(coins)):
    while coins[i] != coins[-1]:
        numb, leftover = numberOfEls(coins[i], coins[i+1])
        if i == 0:
            methods_num = methods_num + numb
        else:
            methods_num = methods_num + numb + leftover % coins[i-1]
        i = i+1

        print(methods_num)


# print(numberOfEls(2, 7))
