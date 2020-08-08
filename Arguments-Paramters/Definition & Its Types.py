"""
----------------------------------------------DIFFERENCE B/W ARGUMENTS & PARAMETERS-------------------------------------------------------

The terms parameter And argument argumentsan be used for the same thing: information that are passed into a function....
But there is major difference among them

From a function's perspective:

■ PARAMETER ---> A parameter is the variable listed inside the parentheses in the function definition.
                   
■ ARGUMENTS ---> An argument is the value of the parameter/variable that are sent/given to the function when it is called. 


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
-------------------------------------------------------Types Of Arguments-----------------------------------------------------------------

1) Positional Arguments : 



2) Keywords Arguments : Keyword arguments are passed by their names instead of their positions as opposed to positional arguments in the 
                        function call. As a result we don’t have to mind about position of arguments when calling a function

3) Default arguments : 







