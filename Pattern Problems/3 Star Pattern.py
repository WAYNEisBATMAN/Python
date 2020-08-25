"""
Star Pattern 1: Equilateral triangle pattern with Star (asterisk)
            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  * 
"""

"""
Star Pattern 2: Half pyramid pattern with Star (asterisk)
* 
* * 
* * * 
* * * * 
* * * * *
"""
for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print(" ")
# -------------------------------------------------------------------------------------------------------------------------------------


"""
Star Pattern 3: Left Half-Pyramid Pattern with Star (asterisk)
        * 
      * * 
    * * * 
  * * * * 
* * * * *         
"""

"""
Star Pattern 4: Downward Half-Pyramid Pattern with Star (asterisk)
      * * 
    * * * 
  * * * * 
* * * * * 
"""

"""
Star Pattern 5: Print Right start Pattern with Star (asterisk)
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print(" ")

for i in range(4, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print(" ")

"""
Star Pattern 6:  Downward star Pattern
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             *
"""


"""
Star Pattern 7: display two pyramids with stars in one pattern
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*
"""
rows = 7
for i in range(rows):
    for j in range(i):
        print("*", end=" ")
    print(" ")

print(" ")

for i in range(rows, 1, -1):
    for j in range(i, 1, -1):
        print("*", end=" ")
    print(" ")
# -------------------------------------------------------------------------------------------------------------------------

"""
Diamond Shaped Pattern using stars
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      *
"""

"""
Star Pattern 8: Display men’s pant style pattern with stars
****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*

"""

"""
Combination of numbers and stars in a pattern
1 * 2 * 3 * 4 

1 * 2 * 3 

1 * 2 

1
"""
for i in range(5, 0, -1):

    for j in range(1, i):

        if i == j+1:
            print(j, end=" ")
        else:
            print(j, "*", end=" ")

    print("\n")
