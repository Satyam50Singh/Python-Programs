# Write a Python script to sort (ascending and descending) a dictionary by value.

d1 = {1: 545, 4: 89, 2: 23, 3: 54, 5: 232, 6: 9}
print("Sorted Dictionary (By Value):")
print(sorted(d1.items(), key=lambda kv: (kv[1], kv[0])))
print("\nSorted Dictionary (Reverse):")
print(sorted(d1.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
