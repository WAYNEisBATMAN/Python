"""
https://pynative.com/print-pattern-python-examples/

"""

"""
Numbers Pattern 1: using a for loop and range function
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5

"""
# Here each rows has no. of entries equal to its value like in 3rd row there are 3 entries.
# And all the entries are same(so, 2nd range parameter(i) will be print instead of j)


for i in range(6):
    for j in range(i):
        print(i, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")

print(" ")

# -------------------------------------------------------------------------------------------------------------------------------------
"""
Number Pattern 2: Half pyramid pattern with numbers
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
for i in range(7):
    for j in range(1,i):
        print(j,end=" ")
    print(" ") 

# -------------------------------------------------------------------------------------------------------------------------------------

"""
Numbers Pattern 3: Inverted Pyramid pattern with numbers
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
"""


# -------------------------------------------------------------------------------------------------------------------------------------

"""
Numbers Pattern 4: Inverted Pyramid pattern with same number
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""
for i in range(6,-1,-1):
    for j in range(i,0,-1):
        print(5, end=" ")

    print(" ")

# -------------------------------------------------------------------------------------------------------------------------------------

"""
Numbers Pattern 5: Display descending order of number
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
"""
for i in range(5,-1,-1):
    for j in range(i,0,-1):
        print(i, end=" ")
    print(" ")    

# -------------------------------------------------------------------------------------------------------------------------------------

"""
Number Pattern 6: Inverted half pyramid pattern with number
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
"""
for i in range(6,-1,-1):
    for j in range(i):
        print(j, end=" ")
    print(" ")   

# -------------------------------------------------------------------------------------------------------------------------------------

"""
Number Problem 7: Display Reverse number pattern
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""
for i in range(6):
    for j in range(i,0,-1):
        print(j, end=" ")
    print(" ")    

# -------------------------------------------------------------------------------------------------------------------------------------
"""
Number Pattern 8: Double the number
  1 
  2    1 
  4    2    1 
  8    4    2    1 
 16    8    4    2    1 
 32   16    8    4    2    1 
 64   32   16    8    4    2    1 
128   64   32   16    8    4    2    1
"""

# -------------------------------------------------------------------------------------------------------------------------------------

"""
Number Pattern 9
1 
1    2    1 
1    2    4    2   1 
1    2    4    8   4    2    1 
1    2    4    8   16   8    4   2    1 
1    2    4    8   16   32   16  8    4    2    1 
1    2    4    8   16   32   64  32   16   8    4    2    1 
1    2    4    8   16   32   64  128  64   32   16   8    4    2    1
"""
# -------------------------------------------------------------------------------------------------------------------------------------
"""
Number Pattern 10: Display 1 to 10 number in Pattern
1 
2 3 4 
5 6 7 8 9
"""
# -------------------------------------------------------------------------------------------------------------------------------------








































