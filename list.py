<<<<<<< HEAD
rick=["hello","bye",1,2,4]
print(rick)
rick.append("hi")	#first
print("after append", rick)

rick.clear() 			#second
print("the data of list get deleted",rick)

list=[1,2,3,"good","bad",1]
print(list)
print(list[4])		# to print the 4th index value
print(list[-1])		# to print the last value of list

x=list.copy()
print("after copy",x)			#3rd

print(list.count(1))			#4th


b=[1,2,37,6,5]
print("First list",list)
print("second List",b)			#5
print(list.extend(b))
print("after combine",b)

print(list.index("good"))		#6

list.insert(2,"bye")		#7
print(list)

print("Before pop",list)
list.pop(1)
print("After pop",list)		#8

print("list before remove",list)		#9
list.remove(1)

print(list)
list.reverse()			#10
print(list)

d=[1,2,6,7,9]
d.sort()			#11
print(d)
=======
list=["hello",'3','5','6']   # 1 create list files
>>> print list
list.append("new")           # 2 add new variable 
>>> print list
list[1]=("hiii")             # 3 change the second item
>>> print list
['hello', 'hiii', '5', '6', 'new']
list = ["apple", "banana", "cherry"]     # 4 list vise output
for x in list:
  print(x)
  list=["apple","mango"]                  # 5 check list
>>> if "apple" in list
print ("yes")
list = ["apple", "banana", "cherry"]       # 6 list integer count
print(len(list))
cars = ['Ford', 'BMW', 'Volvo']            # 7 sort
cars.sort() 
print (cars)
list = ['apple', 'banana', 'cherry']       # 8 remove variable
list.remove("banana") 
fruits = ['apple', 'banana', 'cherry', 'orange']   # 9 listcopy
>>> x = fruits.copy()
>>> print(x)
fruits = ['apple', 'banana', 'cherry']             # 10 index
>>> x = fruits.index("cherry")
>>> print (x)
fruits = ['apple', 'banana', 'cherry']             # 11 reverse
fruits.reverse() 
print (fruits)
list = ["apple", "banana", "cherry"]               # 12 for loop
for x in list:
  print(x)
list = ["apple", "banana", "cherry"]               #13  delete variable in list
del list[0]
print(thislist) 
>>>>>>> 295d02d489417d11cd361461e6b06b0ec8b17952
