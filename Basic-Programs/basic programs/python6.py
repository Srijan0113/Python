#list and its methods
l1=[3,5,234,456,678,"hello"]

print(type(l1))
print(l1)
#string is immutable,non modifiable but list is mutable
l1.remove("hello")
print(l1)
print(l1.count(234))
l1.sort()
print(l1)
l1.pop()
print(l1)
l1.append(78)
print(l1)
#l1.clear()
l1.extend([78,34,89])
print(l1)
l1.sort()
print(l1)
l2=[2,5,7,3,4]
l2.sort()
print(l2)
print(l1[0:4])
l1[2]="srijan"
print(l1)