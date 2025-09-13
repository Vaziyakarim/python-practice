# n=[1,3,5,3,2]
# n.append(20) #adding at end
# print(n)
# n.insert(1,34)#particular index inserting
# print(n)
# n.remove(34)#removal
# print(n)
# n.pop()#removes last
# print(n)
# print(5 in n)#returns true or false if present ot not
# print(n.index(2))#prints index of num 2
# print(n.count(2))#prints how many times 2 is present
# n.sort()#sorting
# print(n)
# n.reverse()#reverses
# print(n)
# n1=n.copy()#copy
# print(n1)
# n.duplicate()
# print()
# n.clear()#all clear
# print(n)

#Ex:2 removal of duplicates
num=[2,3,1,4,1,2,4,2]
unique=[]
for n in num:
    if n not in unique:
        unique.append(n)
print(unique)        