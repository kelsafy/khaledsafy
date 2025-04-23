
def modlist(lst):
    for i in range(len(lst)):
        lst[i] = 10 * lst[i]
def modvar(number):
    number += 10
lst = [1, 2, 3]
modlist(lst)
print(lst)
x = 0
modvar(x) 
print(x)  