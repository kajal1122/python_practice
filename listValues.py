""" Make a list of all even num b/w 1-10 and print it """

list = []
for i in range(1,11):
    if(i % 2 == 0):
        list.append(i)
print(list)

list2 = [x for x in range(1, 11) if x % 2 == 0]
print(list2)
# packing unpacking
