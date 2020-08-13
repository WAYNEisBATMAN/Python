
"""
---------------------------------------------------------STRING DATATYPE------------------------------------------------------------------

Strings are sequence of characters, either as a constant or some kind of variable.
Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. 
We can simply reassign the same string to a different name.

"""
#------------------------------------------------------------------------------------------------------------------------------------------

"""
1. Creating string ---> Strings can be created by enclosing characters inside a single quote or double-quotes. 
                        Even triple quotes can be used in Python for creating strings, 
                        but generally triple quotes are used to represent multiline strings and docstrings.

"""
a=5+3
b="5+3"
print(a)
print(b)

#-----------------------------------------------------------------------------------------------------------------------------------------

"""
2. Accessing characters ---> Accessing characters of strings in python
                             By using square brackets and index of characters.
                             We can access individual characters by using square brackets and index of characters,
                             or a range of characters using slicing.
"""

c='wayne'
print(c[1], c[0], c[4], c[-1]) 

#----------------------------------------------------------------------------------------------------------------------------------

"""
3. String Slicing --->  We can also call out a range of characters from the string, we can do so by creating a slice, 
                        which is a sequence of characters within an original string.

                        Snytax: string_name[start:stop] 
                                         OR
                                string_name[start:stop:step]

                        Here,
                        default values for start&stop are extremeties and for step = 1   
                        Step is also known as stride.                      
"""

d="iamwayneisbatman"
print(d[:], d[1:], d[:-1], d[-5:-1], d[-5:-1:2])

# ------------------------------------------------------------------------------------------------------------------------------

"""

4. Concatenation of 2 or More Strings ---> Joining of two or more strings into a single one is called concatenation
                                           The + operator is used for concatenation in Python.
                                           The * operator can be used to repeat the string for a given number of times.
                                           Also, simply writing two string literals together also concatenates them.

"""

str1 = 'Hello'
str2 ='World!'


print('str1 + str2 = ', str1 + str2)                         # using +


print('str1 * 3 =', str1 * 3)                                # using *

#----------------------------------------------------------------------------------------------------------------------------------

"""
5. Iterating/looping Through a String --->  We can iterate through a string using a for loop. 


"""


count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1

print(count, "l's found in the given string", )    


"""
6. Deleting/updating from a string ---> In Python, Updation or deletion of characters from a String is not allowed.
                                        It will cause an error, because Strings are immutable, 
                                        hence elements of a String cannot be changed once it has been assigned. 
                                        Only new strings can be reassigned to the same name/variable.
"""

#---------------------------------------------------Updating entire string----------------------------------------------------

e="old string"
print(e)
e="new string with same name"
print(e)

#---------------------------------------------------Deletion of entire string---------------------------------------------------

# Syntax: del string_name
f="string"
print(f)
del f
print(f) #Error will show --NameError: name 'f' is not defined



