# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for index, room in enumerate(house):
    print("the " + str(house[index][0]) + " is " + str(house[index][1]) + " sqm")