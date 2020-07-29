
""" 
String Formatting --> Formatting means arrange or put into a format.
                      Python uses c style string formatting to create new, formatted strings or to get formatted output. 
                      The '%'(modulo) operator is used to format a set of variables enclosed in a "tuple"
                      together with a format string which contains normal text together with "argument/format 
                      specifiers", special symbols for different data types like "%s","%d","%f" for string, integer
                      ,float variables respectively.
"""

#Case 1 --> Only one variable. for example name only....

name="Wayne"
print("Hello %s" %name )

#Case 2 --> Multiple variables. for example name and age...

age=22
print("Hello %s! \nAre you %d years old?" %(name,age))

#Try float data type

print("Hello %s! \nAre you %f years old?" %(name,age))

#Now try to limit the decimal values by replacing %.nf with %f where n is the no. of decimal values we want...

print("Hello %s! \nAre you %.2f years old?" %(name,age))


"""
Format Method ---> The format() method that is available with the string object is very versatile and powerful 
                   in formatting strings. 
                   Format strings contain curly braces {} as placeholders or replacement fields which get replaced.
                   We can use positional arguments or keyword arguments to specify the order.
                   Syntax : { } .format(value)           
                   OR        
                   string_name.format("value1", "value2", "value3")
                  
                   Where --->
                             value      : Can be an integer, float values, string, characters or even variables.
                             Returntype : Returns a formatted string with the value passed as parameter in the 
                                          placeholder position.

"""

 
print("My number is {one} and my name is {two} , more number is {one}".format(one=name, two=age))




