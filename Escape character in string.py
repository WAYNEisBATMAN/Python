                           

"""
Escape Sequence ---> If we want to print a text like He said, "What's there?", we can neither use single quotes 
                     nor double quotes.
                     This will result in a SyntaxError as the text itself contains both single and double quotes.
                     One way to get around this problem is to use triple quotes. 
                     Alternatively, we can use escape sequences.
                     An escape sequence starts with a backslash and is interpreted differently. 
                     If we use a single quote to represent a string, all the single quotes inside the string 
                     must be escaped. 
                     Similar is the case with double quotes. Here is how it can be done to represent the above text.

Escape Characters ---> In Python strings, the backslash "\" is a special character, also called the "escape" 
                       character. 


                       Sometimes we may wish to ignore the escape sequences inside a string. 
                       To do this we can place r or R in front of the string. 
                       This will imply that it is a raw string and any escape sequence inside it will be ignored.
                        
"""

a= '''i'm wayne '''     #escaping by using triple quotes.
print(a) 

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


#---------------------------------USING repr() FUNCTION--------------------------------------
#This function returns a string in its printable format, i.e doesn’t resolve the escape sequences.

a="i am \"wayne"    
print(repr(a))


#-------------------------------------USING r/R-----------------------------------------------
#Adding “r” or “R” to the target string triggers a repr() to the string internally 
#and stops from the resolution of escape characters.

a=r"i am \\wayne"
print(a)

a=R"i am \\wayne"
print(a)
