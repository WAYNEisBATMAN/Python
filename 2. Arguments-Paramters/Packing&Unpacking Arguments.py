"""

-------------------------------------------------------Packing & Unpacking Arguments-------------------------------------------------------

https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

Background :

Consider a situation where we have a function that receives four arguments. 
We want to make call to this function and we have a list of size 4 with us that has all arguments for the function. 
If we simply pass list to the function, the call doesn’t work.
We can use * to unpack the list so that all elements of it can be passed as different parameters.

"""

"""
Unpacking Arguments ---> We can use * to unpack the list so that all elements of it can be paased as different parameters.
                         Similarly, we can use ** to unpack the dictionary so that all elements of it can be paased as different parameters.

"""

def fun(a, b, c): 
    print(a, b, c) 

# A call with unpacking of a list
d = [1,2,3]  
fun(*d)

# A call with unpacking of dictionary 
d = {'a':2, 'b':4, 'c':10} 
fun(**d) 

"""
Packing Arguments ---> When we don’t know how many arguments need to be passed to a python function, we can use Packing to pack all arguments 
                       in a tuple. 
                       So the final result of this packing is a tuple.
                       If we want to edit/update elements then first we have to convert it into list.
"""

# A Python program to demonstrate both packing and unpacking. 
# A sample python function that takes three arguments and prints them 
def fun1(a, b, c): 
	print(a, b, c) 

# Another sample function. This is an example of PACKING. All arguments passed to fun2 are packed into tuple *args. 
def fun2(*args): 

	# Convert args tuple to a list so we can modify it 
	args = list(args) 

	# Modifying args 
	args[0] = 'Geeksforgeeks'
	args[1] = 'awesome'

	# UNPACKING args and calling fun1() 
	fun1(*args) 

# Driver code 
fun2('Hello', 'beautiful', 'world!') 


#----------------------------------------------------------------------------------------------------------------------------------------

"""
Applications and Important Points of Packing and Unpacking : 

1. Used in socket programming to send a vast number of requests to a server.
2. Used in Django framework to send variable arguments to view functions.
3. There are wrapper functions that require us to pass in variable arguments.
4. Modification of arguments become easy, but at the same time validation is not proper, so they must be used with care.

"""