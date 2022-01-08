# Program to check whether a list contain a sublist.
lst = [1, 2, 1, 1, 3, 4, 4, 4, 3, 6, 4, 5]

sub_lst = [1, 3, 4]

res = False

if sub_lst == []:
    res = True
elif sub_lst == lst:
    res = True
elif len(sub_lst) > len(lst):
    res = False
else:
    for i in range(len(lst)):
        if lst[i] == sub_lst[0]:
            n = 1

            while((n < len(sub_lst)) and (lst[i+n] == sub_lst[n])):
                n += 1

            if n == len(sub_lst):
                res = True

print("1st Way - Without methods :", res)

# 2nd Way
print("2nd Way - With methods :", set(sub_lst).issubset(set(lst)))
