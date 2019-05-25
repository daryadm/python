shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 2,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 5,
    "pear": 3
}


# Write your code below!

def compute_bill(food):
    global total
    total = 0
    for i in food:
        if stock[i] > 0:
            total += prices[i]
            stock[i] -= 1
    return total


compute_bill(shopping_list)
print
total
print
stock
print

compute_bill(shopping_list)
print
total
print
stock
print

compute_bill(shopping_list)
print
total
print
stock
print