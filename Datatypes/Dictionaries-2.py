"""
1. Accessing elements of dictonary --> In order to access the items of a  refer to its key name.
                                       We can use Keys inside square brackets to get their corresponding values.
                                    
                                        SYNTAX:  dictionary[key]

                                     ■ There is one more way to get elements of a dictionary by using get() method

                                       get() method returns a value for the given key. 
                                       If key is not available then returns user-defined value or none value 
                                       as default.     

                                        SYNTAX:  dictionary.get(key,Default=none)

                                       For nested dictionary:

                                        SYNTAX:  dictionary.get(key1).get(key2).get(key3)   
                                                    
"""

print("\nAccessing elements of d1")

d1={2:2, 3.5:3.5, "hey":"true", False:True, (2,3):(3,30)}

print(d1[3.5]) 
print(d1[False])
print(d1.get(3.5))
print(d1.get(False))

# Access elements of a nested dictionary

d1={2:2, 3.5:{"name":"value", "name1":{"name2":"bruce", "hey":"true", False:True, (2,3):(3,30)}}}
print(d1)
print(d1[3.5])
print(d1[3.5]["name1"])
print(d1[3.5]["name1"]["name2"])
print(d1.get(3.5))
print(d1.get(3,"Not available"))
print(d1.get(3.5).get("name1").get("name2"))




#To list out all the keys
print(d1.keys())

#To list out all the values 
print(d1.values())

#----------------------------------------------------------------------------------------------------------------

"""
2. items() method in Python dictionary ---> This method is used to return the list with all dictionary keys with 
                                            values.
                                            Syntax:   Dictionary.items()

                                                      This method takes no argument.      
                                                      
                                            Returns: A view object that displays a list of a given 
                                                     dictionary’s (key, value) tuple pair.                                    
                                                                        OR
                                                     List of tupples with each tupple consist of 1 key and value.

                                                     If the Dictionary is updated anytime, the changes are reflected
                                                     in the view object automatically.



"""

d2={2:3,"the":"hell","w":"f"}
print(d2.items())
# output:  dict_items([(2, 3), ('the', 'hell'), ('w', 'f')])
print(d1.items())

# NOTE: Everytime items are printed they are not in same order because as we know dictionary in python is an
#       unordered collection of data values  

"""
3. looping inside dictionary ---> We can apply loop in a dictionary by using for and in keywords 
                                  to get all the items, keys, values.

"""

d3={
     "anubhav":"jan",
     "gurpreet":"jan",
     "nikhil":"oct",
     "shyam":"sep"
    }


for key,value in d3.items():
  print("Name  :", key.title())
  print("Month :", value.title(), "\n")


for wtf in d3.keys():
  print("Name  :", wtf.title(),)

print("\t")

for wtf in d3.values():
  print("Month :", wtf.title(),)








                              