"""
A loop is a sequence of instructions that is repeated until a certain condition is reached.

Mainly there are two types of loops in Python  ---> 1) for 
                                                    2) while

We can use them with conditional statements like if,else.


""
-------------------------------------Main difference between for and while loop -------------------------------

for loop - The for statement iterates through a collection of data.
           it is mainly used when we know how many times the code needs to be in loop, 
           i.e, the number of iterations.
           
             Syntax ---> for variable in Iteration:
                             statements(s)


while loop - The while statement simply loops as long as a condition is satisfied.
             It is mainly used when number of iterations are unknown.
             
             Syntax ---> while expression/condition:            
                             statement(s)


"""



"""

-------------------------------------Loop Control Statements-----------------------------------------------

sometimes, there may arise a condition 
where we want to exit the loop completely, skip an iteration or ignore that condition and more situations like this. 

1. Break statement: The break statement is used to terminate the loop or statement in which it is present.
                    Whenever it is encountered in the loop it passes the control to the statement next to the 
                    break statement.

                    Syntax---->      break



2. Continue statement: The continue statement is opposite to that of break statement, instead of terminating the 
                       loop, it forces to execute the next iteration of the loop and skips the iteration 
                       for which continue statement is used.

                       Syntax--->    continue



3. Pass statement:  Also known as null statement
                    The pass statement in Python is used when a statement is required syntactically 
                    but we do not want any command or code to execute.
                      
                    Understand the meaning of syntactically here by this example
                    
                    For example: for i in range(10):
                                      if i == 3:
                     
                                      else:
                                          ("hello")
                    Now this will show syntax error as there is not statement to execute 
                    after if statement condition.
                    So in these cases where we don't want to execute anything 
                    after defining a condition, function, classes, and to avoide this syntax error 
                    we can use the pass statement.
                    
                    The pass statement is useful when we don’t write the implementation of a function 
                    but we want to implement it in the future.
                    
                    Pass statement can also be used for writing empty loops, empty control statement, 
                    function and classes.
                    
                    The difference between a comment and a pass statement in Python is that 
                    while the interpreter ignores a comment entirely, pass is not ignored.
                    
                    Snytax --->   pass                    


"""


for num in range(10):
    
    if num==3:
        pass
    if num==5:
        continue   
    if num==7:
        break            
    print(num)





# Looping is useful in many problems
# If there are multiple numbers of same objects/elements in a list, tuple, dictionary etc
nums = [0, 1, 2, 1, 4, 1, 6, 1]


while 1 in nums:       
    nums.remove(1)
    print(nums)



for num in nums:
    if num == 1:
        nums.remove(1)
        print(nums)



















