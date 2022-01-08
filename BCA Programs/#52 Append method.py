# WAP to append a list to second list..
# ---------------- WAY 1 ----------------------------
lst = [10, 20, 30, 40]
lst2 = [80, 30, 23, 19]

lst2.append(lst)

print("List lst2 after appending (append()) :", lst2)

# ---------------- WAY 2 ----------------------------

lst = [10, 20, 30, 40]
lst2 = [80, 30, 23, 19]

lst2.extend(lst)

print("List lst2 after appending (extend()) :", lst2)
