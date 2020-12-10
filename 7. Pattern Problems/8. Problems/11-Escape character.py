                               

#-----------------------------------------#Escape character----

"""In Python strings, the backslash "\" is a special character, also called the "escape" character.
   Escape characters are characters that are generally used to perform certain tasks 
   and their usage in code directs the compiler to take a suitable action mapped to that character."""

a='i\'m wayne '     #escaping single quote
print(a) 

a="i am \"wayne"    #escaping double quote
print(a)

#lets print escape character in the string 
a="i am \wayne"
print(a)
a="i am \\wayne"
print(a)

#In both cases output will be same as in 2nd case one of the backslash is used as a escape character 


#-----------------------------#USING repr() FUNCTION-----
#This function returns a string in its printable format, i.e doesn’t resolve the escape sequences.

a="i am \"wayne"    
print(repr(a))


#-----------------------------#USING r/R----
#Adding “r” or “R” to the target string triggers a repr() to the string internally 
#and stops from the resolution of escape characters.

a=r"i am \\wayne"
print(a)

a=R"i am \\wayne"
print(a)

