"""
Functions ---> In simple words functions are group of statements within a program which perform specific tasks.

               The idea is to put some commonly or repeatedly done task together and make a function, 
               So that instead of writing the same code again and again for different inputs, 
               we can just call the function.   

               Functions avoids repetition and makes the code reusable.
               Python provides built-in functions like print(), input(), min() etc. 
               But we can also create our own functions, these functions are called user-defined functions
  
               A function can be of two types ---> 1) Built-in function
                                              ---> 2) User-defined function

"""

"""
1. Creating a Function ---> In Python a function is defined using the def keyword, followed by the function name 
                            and parentheses ( ( ) ).
                            The first statement of a function can be an optional statement - the documentation 
                            string of the function or docstring.
                            The statement return [expression] exits a function, optionally passing back an expression 
                            to the caller. 
                            A return statement with no argument is the same as return None.

                            Snytax --->  def function_name(parameters):
                                             """ docstring """   
                                             statement(s)  
"""

def greet():                                            # Function with no argument
    print("Hey there, How are you !")
    

greet()

def add(a,b,c=0,d=0,e=0,f=0,g=0,h=0,i=0):
    
    print(a+b+c+d+e+f+g+h+i)

add(1,2)


def subtract(a,b,c=0,d=0,e=0,f=0,g=0,h=0,i=0):
    print(a-b-c-d-e-f-g-h-i)

subtract(1,2)


def multiply(a,b,c=1,d=1,e=1,f=1,g=1,h=1,i=1):
    print(a*b*c*d*e*f*g*h*i)
      
multiply(1,2)   

def divide(a,b,c=1,d=1,e=1,f=1,g=1,h=1,i=1):  
    print(a/b/c/d/e/f/g/h/i)

divide(1,2)


"""
2. *args and **kwargs ---> They are use to pass multiple argument or keyword argument to a function
 (unpacking operator (*))  There are a few ways you can pass a varying number of argument to a function. 
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

















