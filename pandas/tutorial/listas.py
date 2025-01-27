thislist = ["apple", "banana", "cherry"]
print(thislist)
print('-----------------------------------------------------')

# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print('-----------------------------------------------------')

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print('-----------------------------------------------------')

# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print('-----------------------------------------------------')

# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print('-----------------------------------------------------')

# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


print('-----------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print('-----------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Elimina la primera ocurrencia que sea banana
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Elimina la ultima ocurrencia
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Borra la lista entera con estructura incluida
thislist = ["apple", "banana", "cherry"]
del thislist

# Borra el contenido dela listapero no la estructura
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print('-----------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

print('-----------------------------------------------------')

newlist = [x for x in range(10)]
print(newlist)

print('-----------------------------------------------------')

newlist = [x for x in range(10) if x < 5]
print(newlist)

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

print('-----------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

print('-----------------------------------------------------')

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print('-----------------------------------------------------')

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print('-----------------------------------------------------')

# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

print('-----------------------------------------------------')

# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

print('-----------------------------------------------------')

# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print('-----------------------------------------------------')

# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

print('-----------------------------------------------------')

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print('-----------------------------------------------------')

# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

print('-----------------------------------------------------')

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print('-----------------------------------------------------')

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print('-----------------------------------------------------')

# Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

print('-----------------------------------------------------')

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print('-----------------------------------------------------')

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

print('-----------------------------------------------------')

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

