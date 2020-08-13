"""

Conditional statment / Decision making statement 

1. if
2. if else
3. nested if
4. elif or if elif else ladder
5. switch statement


"""
#_____________________________________________________________________________________________________

"""
 1). if statement --->  It is used to decide whether a certain statement or block of statements 
                       will be executed or not i.e if a certain condition is true 
                       then a block of statement is executed otherwise not.
                       It is also called one-way selection statement.
"""


name = "wayne"
if name=="wayne":                          # example for if statement.
    print("name is",name)

#-------------------------------------------------------------------------------------------------

""" 
2). if else ---> This statement adds one more functionality to if statements where execution takes place 
                only if a statement is true and no action if it is false.
                Here comes the use of else statement with if statement/block
"""


name = "wayne"
if name=="wayne":                          
    print("name is",name)                  # example for if else statement.
else:
    print("name is not",name)

#----------------------------------------------------------------------------------------------------

"""
3). nested-if ---> Python allows us to nest if statements within if statements. 
                  i.e, we can place an if statement inside another if statement.
                  The nested if...else statement is used when a program requires 
                  more than one test expression. 
                  It is also called a multi-way selection statement.

"""



x = 10
if x>5:
    print("1")
    if x<4:
        print("2") 
    if x<15:
             print("7")
else:
    print("wrong")        

#-------------------------------------------------------------------------------------------------------

"""
4). if elif else ladder ---> elif is simply short of else if. It's used where one decide among multiple options                           
                            The if statements are executed from top to down. 
                            As soon as one of the conditions controlling the if is true,the statement associated 
                            with that if is executed,and the rest of the ladder is bypassed.                              
                            If none of the conditions is true,then the final else statement will be executed.
                            
                                                           
"""

x = 11
if x>12:
    print("greater than 9")
elif x<13:
    print("smaller than 13")
elif x>6:
    print("greater than 6")
else:
    print("out of if block")

