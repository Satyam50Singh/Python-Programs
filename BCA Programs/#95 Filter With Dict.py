# Write a Python program to filter a dictionary based on values. Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre
# Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox':190)

d1 = {
    'Cierra Vega': 175,
    'Alden Cantrell': 180,
    'Kierra Gentry': 165,
    'Pierre Cox': 190
}

for i in d1:
    if d1[i] > 170:
        print(d1[i], "  ", i)
