"""
strip() is an inbuilt function in Python programming language 
that returns a copy of the string with both leading and trailing characters 
removed (based on the string argument passed).

If the leading and trailing characters are whitespace then only whitespace can be remove
we cant remove any other character or substring in that case.


Syntax----------->  string.strip([chars])
                    By default strip arguments will only remove the whitespace at the both ends of the string.

                    Based on that it has 2 types lstrip and rstrip, left side strip and right side strip respectively.

"""



string = "   my name is wayne my    "   # CASE-1: Where end characters are whitespaces


print(string.strip())

#--------------------OR----------------------

print(string.lstrip())

#---------------------OR----------------------------

print(string.rstrip())

#-------------------------OR----------------------

print(string.strip("my"))

#-----------------------------OR----------------

print(string.lstrip("my"))

#-----------------------------------OR---------------

print(string.rstrip("my"))




string = "my name is wayne my"  # CASE-2: Where end characters are substrings.

print(string.strip())

#--------------------OR----------------------

print(string.lstrip())

#---------------------OR----------------------------

print(string.rstrip())

#-------------------------OR----------------------

print(string.strip("my"))

#-----------------------------OR----------------

print(string.lstrip("my"))

#-----------------------------------OR---------------

print(string.rstrip("my"))