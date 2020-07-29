
        #    """ Python Global, Local and Non-Local Variables """


"""
1. Global Variable ---> In Python, a variable declared outside of the function or in global scope is known as a global 
                        variable. This means that a global variable can be accessed inside or outside of the function.

"""

# Example to show Global variable

x = "hello"

def fun():
    print("Inside The Function", x)

fun()

print("Outside The Function", x)

#------------------------------------------------------------------------------------------------------------------

"""
Now if we want to change the value of the global variable inside a function the output will show an error 
because Python treats x as a local variable and x is also not defined inside fun(). 
To make this work we use the global keyword.
"""

"""
2. global keyword ---> In Python, global keyword allows you to modify the variable outside of the current scope. 
                       It is used to create a global variable and make changes to the variable in a local context.


■ Rules Of Global Keyword

The basic rules for using global keyword in Python are:

1) When we create a variable inside a function, it is local by default.
2) When we define a variable outside of a function, it is global by default. 
   In this case we don't have to use the global keyword.
3) We use global keyword to read and write a global variable inside a function.
4) Use of global keyword outside a function has no effect.

"""

# Changing Global Variable From Inside a Function using global keyword

x = "hello"

def fun():
    global x
    x=x+"2"
    print("Inside The Function", x)

fun()     # Call function 


"""
3. Local Variables ---> A variable declared inside the function's body or in the local scope is a local variable.
  
"""

# (i) Accessing local variable 
 

def local():
    y="lol"
    print(y)   

local() # Function call

# print(y) ---> {accessing local variable in global scope}
# The output shows an error because we are trying to access a local variable y in a global scope 
# whereas the local variable only works inside foo() or local scope. 


#(ii) Creating a local variable ---> Normally, we declare a variable inside the function to create a local variable.



"""
Global variable and Local variable with same name
"""
x=5

def local():
    x=4
    print(x)

local()    
print(x)

"""
We created variables of same name in both local and global scope.
When we first call the function local() it takes the value of x which locally created in the function.
But when we give the print(x) command outside the function then it is the call for global scope for the variable x
 
"""

























