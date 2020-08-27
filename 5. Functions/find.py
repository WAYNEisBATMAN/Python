"""
The find() method returns the lowest index of the substring if it is found in given string. 
If it is not found then it returns -1.

Syntax ----------->   str.find(sub)    
       ----------->   str.find(sub,start,end)               
Here, 
     Sub: refers to the substring we want to find/search in the string.
     Start: refers to the starting position/index from where the search is begin.(optional)
     End: refers to the ending position/index where search ends(optional)

     Where start is included and end is not included.

     In 1st syntax by default the start and end values are 0 and the L respectively 
     where L is the length of the string.

"""

mystring="become millionare in 30 days"

Result=mystring.find("millionare",0,30)

print(Result)

"""-------------------OR-------------------------"""


print(mystring.find(millionare))

"""---------------------OR-----------------------"""


mystring="become millionare in 30 days".find("millionare",0,30)

print(mystring)
