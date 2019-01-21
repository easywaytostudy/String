a="hello"     
b="Harsimran Singh"

print(a,b)
x=a.capitalize 	#1      
print(a)
y=b.casefold()  #2
print(b)
x=a.center(30)	#3
print(x)
y=b.count('o')  #4
print(y)
x=a.encode()   #5
print(x)
c="h\te\tl\tl\to"  #6
y=c.expandtabs(2)
print(y)
b="good morning"  #7
y=b.find("od")        
print(y)
x = txt.isdecimal()   #8
print(y)
x=d.isspace()		#9
print(x)
a = ("har", "sim", "ran")     #10
x = "#".join(a)
print(x) 
x = txt.ljust(20)              #11
print(x, "is my favorite fruit.")
a="hello"                        #12
>>> x=a.lower()
>>> print(x)
a="apple"                        #13
x = a.lstrip()
print("of all fruits", x, "is my favorite") 
txt = "my fav "                   #14
x = txt.partition("apple")
print(x)
txt "I like bananas"              #15
x = txt.replace("bananas", "apples")
print(x)
a = "hi har, my namr is mohari."       #16
x = a.rfind("har")
print(x) 
a= "ruck, knuck."                        #17
x = a.rindex("uck")
print(x)
a = "I love mohali "                      #18
x = a.rpartition("IT")
print(x)
txt = "apple, banana, cherry"              #19
x = txt.rsplit(", ")
print(x)
a = "welcome to patiala"                   #20
x = a.split()
print(x) 
a = "Thank you \nfor music"                 #21
x = a.splitlines()
print(x) 
a = "Hello, welcome to my world."           #22
x = a.startswith("Hello")
print(x)
a = "Hello, welcome to my world."           #23
x = a.startswith("Hello")
print(x)
a = "Hello My Name Is HARSIMRAN"          #24
x = a.swapcase()
print(x)
a = "Hello, welcome to my world."         #25
x = a.startswith("Hello")
print(x)
a = "Hello my friends"                    #26
x = a.upper()
print(x)
a= "50"                                  #27
x = a.zfill(10)
print(x) 
