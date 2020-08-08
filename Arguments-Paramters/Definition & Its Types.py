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

1) Default Argument

def example(x=1, y=2, z="hello")     # function defintion
    -----------
    -----------

example(x,y,z)                       # function call

-----------------------------------------------------------------------------------------------------------------------------------------
2) Positional Arguments

def example(x,y,z)                   # function defintion
    -----------
    -----------

example(1,2,"hello")                 # function call

-----------------------------------------------------------------------------------------------------------------------------------------
3) Keyword Arguments

def example(x,y,z)                   # function defintion
    -----------
    -----------

example(y=2, z="hello", x=1)         # function call

-----------------------------------------------------------------------------------------------------------------------------------------
4) Positional or Keyword

def example(x,y,z)                   # function defintion
    -----------
    -----------

example(y=2, x=1, "hello")         # function call : Here x and y are keyword, z is positional arguments

-----------------------------------------------------------------------------------------------------------------------------------------

5) Variable Positional (var-positional)
   





Variable Keyword

"""
 








