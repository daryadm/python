n = 1000
numbers = range(2, n)
results = []

while len(numbers) > 0:
    results.append(numbers[0])
    i = 0
    while i < len(numbers):

        if numbers[i] % results[-1] == 0:
            numbers.pop(i)

        else:
            pass
        i += 1
print
len(results)
############################################################
slow = 1000
fast = 1
year = 1
while slow > fast:
    slow = slow + slow
    sdie = slow * 0.4
    slow = slow - sdie
    fast = fast + fast
    fdie = fast * 0.3
    fast = fast - fdie
    year += 1
    print
    year, slow, fast
