def digit_sum(n):
  n = str(n)
  sum = 0
  for digit in n:
    sum += int(digit)
  print(sum)

digit_sum(434)
digit_sum(1000)
digit_sum(9)
digit_sum(0)