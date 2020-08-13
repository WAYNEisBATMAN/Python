"""

Conditional statment / Decision making statement 

1. if
2. if else
3. nested if
4. elif or if elif else ladder
5. switch statement


"""
#------------------------------------------------------------------------------------------------------------------------    


"""
 1). if statement --->  It is used to decide whether a certain statement or block of statements 
                        will be executed or not i.e if a certain condition is true 
                        then a block of statement is executed otherwise not.
                        It is also called one-way selection statement.
"""


name = "wayne"
if name=="wayne":                          # example for if statement.
    print("name is",name)


#------------------------------------------------------------------------------------------------------------------------    


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

#------------------------------------------------------------------------------------------------------------------------    


"""
3). nested-if ---> Python allows us to nest if statements within if statements. 
                   i.e, we can place an if statement inside another if statement.
                   The nested if...else statement is used when a program requires 
                   more than one test expression. 
                   It is also called a multi-way selection statement.
                   If any of the condition false then it will bypassed the command to 
                   the else block.

"""

x = 10
if x>5:
    if x>4:
        if x<15:
            print("7")
else:
    print("wrong")        

#------------------------------------------------------------------------------------------------------------------------    


"""
4). if elif else ladder ---> elif is simply short of else if. It's used where one decide among multiple options                           
                             The if statements are executed from top to down. 
                             As soon as one of the conditions controlling the if is true,the statement associated 
                             with that is executed,and the rest of the ladder is bypassed.                              
                             If none of the conditions is true,then the final else statement will be executed.
                            
                                                           
"""

x = 11
if x<12:
    print("greater than 9")
elif x<13:
    print("smaller than 13")
elif x>6:
    print("greater than 6")
else:
    print("out of if block")

#------------------------------------------------------------------------------------------------------------------------    

"""
NOTE:   MAIN DIFFERENCE BETWEEN NESTED IF AND ELIF STATEMENTS IS
     
1. In nested if statements there is a sequence of if conditions.
   In nesting atleast 2 if statements should be there.        
   Statement under nested if block will only execute when all the if conditons are true               
   If any single condition is false then the the whole nested if block will bypassed
   and the else statement will be executed.


2. In elif statement if a single if or elif condition is true then the statement 
   corresponding to that condition will be executed.
   and all other conditions will be bypassed for the if elif block.

"""
#-----------------------------------------------------------------------------------------------------------------------

""" 
                BOTH ARE VERY UNLIKE TO EACH OTHER

1. nested me saari conditions ka true hona jaruri hai agr ek bhi false hui 
   toh else statement execute hogi.

2. elif me koi bhi ek condition true hote hi uske corresponding statement 
   excecute hogi baaki condtions bypassed ho jayengi whether they are true or false.

"""
