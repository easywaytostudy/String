num1=int(input("Enter first number :- "))
num2=int(input("Enter second number :- "))	
print("Which opertation you want apply 1.add, 2.sub, 3.div")
op=input()
def add():
			c=num1+num2
			print("After Add",c)		
def sub(): 
			c=num1-num2
			print("After sub",c)
def div():
			c=num1/num2
			print("After div",c)
def again():
	print("If you want to perform any other operation")
	print("say Yes or y else NO or n")
	ans=input()
	if ans=="yes" or ans=="y":
		cal()
	else:
		print(" Good Bye")
def cal():
       
	if op=='1' or op=="add" or op=="1.add":
		add()
	elif op=='2' or op=="sub" or op=="2.sub":	
		sub()
	elif op=='3' or op=="div" or op=="3.div":
		div()
	else:
	
		print("Invalid Operation")
		again()
cal()
again()
