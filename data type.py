l2= [1,2,3,4,5,6,7,8,9]
l1 =list(range(2,8))
print(l1)
print(l2)
l3 =list(range(1,9,2))
print(l3)
#adding the elements in list
list1 = [1,2,3,4,5]
list1.append(6)
print(list1)

list2 = [1,2,3,4,5]
list2.insert(2,6)
print(list2)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print(a)
b.extend(a)
print(b)

c = [1,2,3,4]
d =sum(c)
print(d)

l5 = [1,2,3,2,3,5,1,3]
print(l5.count(3))
print(l5.remove(1))

print(len(l5))

print(l5.index(5,5))

print(max(l5))
print(min(l5))

List7 = [2.3,4.445,3,5.33,1.054,2.5]
List7.sort()
print(List7)
#print(l5.sort())

List7.sort(reverse= True)
print(List7)

list = [1,2,3,4,5]
list.reverse()
print(list)

List9 = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List9.pop(3))
print(List9)

List8 = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List8[0]
print(List8)

