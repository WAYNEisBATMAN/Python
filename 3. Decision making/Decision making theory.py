"""There comes situations in real life when we need to make some decisions and based on these decisions, 
we decide what should we do next. Similar situations arises in programming also where we need to make 
some decisions and based on these decision we will execute the next block of code.

Decision making statements in programming languages decides the direction of flow of program execution.
Decision making statements available in python are:"""

#1) if statement
#2) if..else statements
#3) nested if statements
#4) if-elif-else ladder

#-------------------------KEEP IN MIND INDENTATION PLAYS A BIG ROLE-------------------

#---------------------------Syntax of each statement-------------

#1)If statement

"""
if (condition):
    statements to execute if condition is true.
    .
    .
    .

"""
print("\nIF OUTPUT BELOW\n ")

#Python code
i = 20
if (i>=15): 
   print("20 is more than 15") 

print("This is not in if block")


#2) if-else

"""
if (condition):
    statements to execute if condition is true.
    .
    .

else:
    statements to execute'
    .
    .
"""

print("\nIF ELSE OUTPUT BELOW\n ")
#Python code

i = 20
if (i<=15): 
   print("20 is less than 15") 
   

else:
    print("20 is greater than 15")



#3) Nested if 

"""
if (condition1):
    Executes when condition1 is true
    if (condition2): 
       Executes when condition2 is true
    if (condition3):
       Executees when condition3 is true 
    
"""


#Python code

print("\n NESTED IF OUTPUT BELOW\n ")

i = 10
if (i == 10): 
	if (i < 15): 
		print ("i is smaller than 15") 
	if (i >12): 
		print ("i is smaller than 12 too") 
	else: 
		print ("i is greater than 15") 


#4) If-elif-else ladder

"""
Syntax:-

if (condition1):
    statement
elif (condition2):
    statement
elif (condition3):
    statement    
.
.
else:
    statement

"""

print("\nIF-ELIF-ELSE LADDER OUTPUT BELOW\n")
#Python code

# Python program to illustrate if-elif-else ladder 
#!/usr/bin/python 

i = 20
if (i == 10): 
	print ("i is 10") 
elif (i == 15): 
	print ("i is 15") 
elif (i == 20): 
	print ("i is 20") 
else: 
	print ("i is not present") 











