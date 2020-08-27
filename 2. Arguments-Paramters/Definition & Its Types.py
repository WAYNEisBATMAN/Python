"""
----------------------------------------------DIFFERENCE B/W ARGUMENTS & PARAMETERS-------------------------------------------------------

The terms parameter And argument argumentsan be used for the same thing: information that are passed into a function....
But there is major difference among them

From a function's perspective:

■ PARAMETER ---> A parameter is the variable listed inside the parentheses in the function definition.
                   
■ ARGUMENT ---> An argument is the value of the parameter/variable that are sent/given to the function when it is called. 


"""
def example(x,y,z):   # Function definition
    print(x+y+z)

example(1,2,3)        # Function call  

# In  this example x,y,z are Parameters and 1,2,3 are Arguments.

#-----------------------------------------------------------------------------------------------------------------------------------------

"""
---------------------------------------------DIFFERENCE B/W ACTUAL & FORMAL PARAMETERS-------------------------------------------------------

■ FORMAL PARAMETERS ---> A formal parameter is a parameter which is in the function definition.
                         They are simply called parameters.

■ ACTUAL PARAMETERS ---> An actual parameter is a parameter which is in the function call.
                         They are simply called arguments.                         
 
From all the above discussion we can say that  
Parameters = Formal Arguments
Arguments = Actual Arguments

"""
# -----------------------------------------------------------------------------------------------------------------------------------------

"""
-------------------------------------------------------Types Of Arguments and Paramters-----------------------------------------------------------------

https://getkt.com/blog/types-of-function-arguments-in-python/ 
"""
# 1) Default Arguments

def example(x=1, y=2, z="hello")     # function defintion
    -----------
    -----------

example(x,y,z)                       # function call

-----------------------------------------------------------------------------------------------------------------------------------------
#2) Positional Arguments

def example(x,y,z)                   # function defintion
    -----------
    -----------

example(1,2,"hello")                 # function call

-----------------------------------------------------------------------------------------------------------------------------------------

# 3) Keyword Arguments (Useful when we don't know the position of each parameter but actually know the name of it.)

def example(x,y,z)                   # function defintion
    -----------
    -----------

example(y=2, z="hello", x=1)         # function call

-----------------------------------------------------------------------------------------------------------------------------------------
# 4) Positional or Keyword

def example(x,y,z)                   # function defintion
    -----------
    -----------

example(y=2, x=1, "hello")         # function call : Here x and y are keyword, z is positional arguments

-----------------------------------------------------------------------------------------------------------------------------------------

# 5) Variable Length Positional (var-positional, args) 

def example(x,y,z,*args)                   
    print("Regular Positional Arguments", x,y,z)
    print("Variable Length Positional arguments", args)

example(1,2,3,4,5,6,7)
>>>Regular Positional Arguments 1 2 3 
   Variable Length Positional arguments (4,5,6,7)

# 6) Variable Length Keyword  (kwargs)

def example(x,y,z,**kwargs)                   
    print("Regular Positional Arguments", x,y,z)
    print("Variable Length Positional arguments", args)

example(1,2,3, a=4, b=5, c=6, d=7)
>>>Regular Positional Arguments 1 2 3 
   Variable Length Positional arguments {"a":4, "b":5, "c":6, "d":7}  


 
"""
In detail about Variable Length Positional (var-positional, args) and Variable Length Keyword(kwargs)
* is used as an unpacking operator 
we have two types of unpacking operators 
1) *args - it unpacks iterables like list,tuple etc.
2) **kwargs - it unpacks dictionary

Use the below link To know more about unpacking, like why and wher do we even need it. 

https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

 *args and **kwargs --->   Non-Keyworded Arguments - args      (or simply arguments)
                           Keyworded Arguments     - kwargs
                           They are use to pass multiple argument or keyword argument to a function
                           There are a few ways you can pass a varying number of argument to a function. 
                           The first way is often the most intuitive for people that have experience with collections. 
                           Simply pass a list or a set of all the argument to your function, but whenever 
                           we call this function we will also need to create a list of argument to pass to it. 
                           
                           This is where 2nd method *args can be really useful, because it allows you to pass 
                           a varying number of positional argument.  

                           In this we are no longer passing a list to my_sum(), instead, we're passing 
                           three different positional argument.

                           NOTE: args and kwargs are just names. we're not required to use the name args. 
                                 We can choose any name that we prefer. 
                                 ALL THAT MATTERS HERE IS THAT WE USE THE UNPACKING OPERATOR(*).
                                 USE A SINGLE ASTERISK(*) TO UNPACK ITERABLES.
                                 USE TWO ASTERISKS(**) TO UNPACK DICTIONARIES.
                                
"""


def addition(*number):
    l=len(number)
    i = 0
    sum = 0
    while i<l :             
        sum = sum + number[i]
        i=i+1
    print(number)
    print("Total sum is =",sum)

addition(1,2,3,4)



"""
Applications and Important Points of packing & unpacking
1. Used in socket programming to send a vast number of requests to a server.
2. Used in Django framework to send variable arguments to view functions.
3. There are wrapper functions that require us to pass in variable arguments.
4. Modification of arguments become easy, but at the same time validation is not proper, so they must be used with care.
"""


