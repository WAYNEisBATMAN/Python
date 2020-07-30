#strings are sequence of characters, either as a constant or some kind of variable.
#Creating string- string in python can be created by using single, double or triple #quotes.

a=5+3
b="5+3"
print(a)
print(b)

#-------------------------------------------Accessing characters of strings in python--------------------------------
#By using square brackets and index of characters.

c='wayne'
print(c[1], c[0], c[4], c[-1])  

#------------------------------------------------String Slicing--------------------------------------------
#string name[start:stop] here start character is included and stop character is not.
#default values are extremeties.

d="iamwayne"
print(d[:], d[1:], d[:-1], d[-5:-1])

#--------------------------------------------Deleting/updating from a string.----------------------------------------
"""In Python, Updation or deletion of characters from a String is not allowed. It will cause an error 
#because item assignment or item deletion from a String is not supported.
#Strings are immutable, hence elements of a String cannot be changed once it has been assigned. 
#Only new strings can be reassigned to the same name."""


print(d)  #Error will show--TypeError: 'str' object does not support item assignment

#---------------------------------------------Updating entire string---------------------------------------------------

e="old string"
print(e)
e="new string with same name"
print(e)

#--------------------------------Some inbuilt functions use with strings-----------
x="wayne"
print(x.capitalize())
print(x.lower())
print(x.lstrip())
print(x.rfind("a"))


#-----------------------------------------Deletion of entire string---------------
#del string name
f="string"
print(f)
del f
print(f) #Error will show --NameError: name 'f' is not defined

