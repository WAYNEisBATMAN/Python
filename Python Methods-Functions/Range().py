"""
range() is a built-in function of Python. 
It is used to perform an action for a specific number of times or we can say 
it is used to generate a sequence of numbers.
range() in Python(3.x) is just a renamed version of a function called xrange in Python(2.x). 

range() is commonly used in FOR looping hence, 
knowledge of same is key aspect when dealing with any kind of Python code. 

Most common use of range() function in Python is to iterate sequence type (List, string etc.. ) 
with for and while loop.


Syntax --------> range(start, stop, step)  
    
Where, 
      start: An integer number specifying at which position to start. Default is 0
      stop: An integer number specifying at which position to end.
      step: An integer number specifying the incrementation. Default is 1 

      Start and Step are Optional 
      Stop is Required
 
\\\\ Remember the last value or the stop value is excluded \\\\



"""

for WTF in range(5):
     print(WTF)

for WTF in range(5,55,5):
     print(WTF)

     

# Make lists using range function

#1
mylist = list(range(1,5))
print(mylist)

#2
evenlist = list(range(0,20,2))
print(evenlist)

#3
squares = []
for value in range(1,10):
	square=value**2
	squares.append(square)
	print(squares)


	





