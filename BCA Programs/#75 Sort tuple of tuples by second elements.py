# Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
t2 = sorted(tuple1, key=lambda tuple1: tuple1[1])

print("Sorted Tuple: ", t2)
