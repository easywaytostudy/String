a="hello World"     
b="Good Morning"

print(a,b)
x=a.capitalize 	#First method       
print(a)

y=b.casefold()  #second method
print(b)

x=a.center(30)	#third method
print(x)		

y=b.count('o')  # 4th 
print(y)

x=a.encode()   #5th
print(x)

b="good day"
y=b.endswith("g")  #6th
print(y)
y=b.endswith("day",5,8)
print(y)

c="h\te\tl\tl\to"  #7th 
y=c.expandtabs(2)
print(y)

b="good day"        #8th
y=b.find("da")        
print(y)

d="hello123"		#9th
x=d.isalnum()
print(x)

x=d.isspace()		#10
print(x)



