"""

-------------------------------------Loop Control Statements-----------------------------------------------

Sometimes, there may arise some conditions, where we want to 
(i) exit the loop completely, 
(ii) skip an iteration or ignore that condition and more situations like this. 

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





