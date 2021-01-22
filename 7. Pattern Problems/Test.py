"""
Star Pattern 3: Left Half-Pyramid Pattern with Star (asterisk)
        * 
      * * 
    * * * 
  * * * * 
* * * * *         
"""
for i in range(5):
    for j in range(5):
        if j < 5-i-1:
            print(" ", end="")

        else:
            print("*", end="")
    print(" ")
