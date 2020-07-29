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
           
             Syntax ---> for iterator_var in sequence:
                             statements(s)


while loop - The while statement simply loops as long as a condition is satisfied.
             It is mainly used when number of iterations are unknown.
             
             Syntax ---> while expression/condition:            
                             statement(s)


"""


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



















