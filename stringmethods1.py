str=' arti '
str1='arti'
print("1.first letter will be capital=", str1.capitalize())   
print(" ")
print("-----------------------------------------------------------------")
print("2.it will add 10 spaces at first and last to the string =", str1.center(10))  

print(" ")
print("-----------------------------------------------------------------")

str2='kit kat kitkitkat katkit'
print("3.it will count that how many times 'kat' is repeated in the string =" , str2.count("kat")) 

print(" ")
print("-----------------------------------------------------------------")

print("4.it checks that the string is ends with '.' if yes it give true otherwise false =", str2.endswith('.'))

print(" ")
print("-----------------------------------------------------------------")

str3='h\te\tl\tl\to'
print("5.it will generate tabs instead of \t and gives 2 spaces at every tab as assigned in its parameter =", str3.expandtabs(2))

print(" ")
print("-----------------------------------------------------------------")

print("6.it finds the position of 'kat' in string =", str2.find("kat"))	
print(" ")
print("-----------------------------------------------------------------")


print("7.it will finds th position of 'kat' in the string = ", str2.index("kat"))	
print(" ")
print("-----------------------------------------------------------------")
 
print("8.it returns true if string contains alphanumeric items like 0-9 and a-z and false if string contains !@#$%^& type of symbols =", str2.isalnum())
print(" ")
print("-----------------------------------------------------------------")

		 
str4='arti'
print("9.it returns true if string contains only alphabets otherwise it returns false =", str4.isalpha())
print(" ")
print("-----------------------------------------------------------------")

		 
str5='7'
print("10.return true if all characters in string are digits else it returns false =", str4.isdigit())
print(" ")
print("-----------------------------------------------------------------")

		 
print("11.return true if all characters in string in lower case else returns false =" , str4.islower())	
print(" ")
print("-----------------------------------------------------------------")
	 
print("12.return true if all characters in string in upper case else returns false =", str4.isupper())		
print(" ")
print("-----------------------------------------------------------------")

print("13.return true if string is numeric else returns false =", str5.isnumeric())
print(" ")
print("-----------------------------------------------------------------")
		 
print("14.return true if string contains only space else return false =", str2.isspace())	
print(" ")
print("-----------------------------------------------------------------")

print("15.return true if first character of every word in string is in upper case else return false =", str2.istitle())	
print(" ")
print("-----------------------------------------------------------------")

str6=('a','b','c','y','z')
print("16.it joins all items into single string =", ' '.join(str6))
print(" ")
print("-----------------------------------------------------------------")

print("17.it add number of spaces at the last of the string =", str1.ljust(10))	
print(" ")
print("-----------------------------------------------------------------")
	 
print("18.it return string in lower case =", str1.lower())
print(" ")
print("-----------------------------------------------------------------")
	
print("19.it remove all spaces present at starting of string =", str1.lstrip())
print(" ")
print("-----------------------------------------------------------------")
	
print("20.it remove all spaces present at last of the string =", str1.rstrip())	
print(" ")
print("-----------------------------------------------------------------")

print("21.it divide string into 3 parts main selected part,part before selected part , and part after selected part =", str2.partition("ka"))
print(" ")
print("-----------------------------------------------------------------")

print("22.it replace the particular part of string with desired part =", str4.replace('a','k')) 
print(" ")
print("-----------------------------------------------------------------")

print("23.if finds position of particular part of string from right side =", str2.rfind('r'))
print(" ")
print("-----------------------------------------------------------------")

print("24.it parts the string from right side =", str2.rpartition('kat')) 
print(" ")
print("-----------------------------------------------------------------")
	
print("25.it spits the string when space arises =", str2.split(" "))
print(" ")
print("-----------------------------------------------------------------")

str7 ='arti\n aries'
print("26.it splits the string into different stings when \n is used =", str7.splitlines())
print(" ")
print("-----------------------------------------------------------------")

print("27.return true if string started with assigned characted else return false =", str7.startswith("k")) 
print(" ")
print("-----------------------------------------------------------------")

print("28.it swaps lower case into upper case and upper case to lower case =", str7.swapcase())
print(" ")
print("-----------------------------------------------------------------")
		
print("29.converts the first character of each word to upper case =", str2.title())  
print(" ")
print("-----------------------------------------------------------------")

print("30.converts the whole srting into upper case =", str2.upper())	
print(" ")
print("-----------------------------------------------------------------")

print("31.it adds zeros in the beginning of string and make length of string as assigned =", str5.zfill(10))		 
print(" ")
print("-----------------------------------------------------------------")

	
