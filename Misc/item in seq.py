def count(sequence, item):
  counter = 0
  for i in sequence:

    if i == item:
      counter +=1
    else:
      counter == 0
  print(counter)


count([1,2,"ff",4,"ffff",3,"ff",3,], "ff")