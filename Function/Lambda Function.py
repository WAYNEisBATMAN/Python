"""
Lambda/Anonymous Function ---> In Python, an anonymous function is a function that is defined without a name.
                               While normal functions are defined using the def keyword in Python, anonymous 
                               functions are defined using the lambda keyword.
                               Hence, anonymous functions are also called lambda functions.




How to use lambda Function in Python ---> Lambda functions can have any number of arguments but only one expression. 
                                          The expression is evaluated and returned. 
                                          Lambda functions can be used wherever function objects are required.
                                          
                                          Syntax:  lambda arguments: expression


"""

# lets  make lambda function equivalent to           def Formula(x,y,z):
#                                                        return x + y * z

Formula = lambda x,y,z : x + y * z

print(Formula(1,2,3))



"""
Use of Lambda Function in python ---> We use lambda functions when we require a nameless function for a short period 
                                      of time.
                                      In Python, we generally use it as an argument to a higher-order function 
                                      (a function that takes in other functions as arguments). 
                                 Lambda functions are used with built-in functions like filter(),map(),reduce() etc.

"""



"""
Filter() ---> The filter() function in Python takes in a lambda function and a list as arguments.
              The function is called with all the items in the list and a new list is returned which contains items
              for which the function evaluates to True.


             NOTE: It only returns a new string when the function expression evaluates to True.
"""

# Here is an example use of filter() function to filter out only even numbers from a list.


mylist = [1,2,3,4,57,56]
new_list = list(filter(lambda x : (x%2 != 0), mylist))

print(new_list)



"""
Map() ---> The map() function in Python takes in a function and a list.
           The function is called with all the items in the list and a new list is returned which contains items 
           returned by that function for each item.
           Here is an example showing use of map() function to double all the items in a list.


"""

mylist = [1,2,3,4,57,56]
new_list = list(map(lambda x : x*2, mylist))

print(new_list)









