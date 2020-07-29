"""
replace() is an inbuilt function in Python programming language that returns a copy of the string 
where all occurrences of a substring is replaced with another substring.

Syntax------->  string.replace(old, new, count)
      
Where,
      old: refers to the old substring we want to replace.
      new: refers to the new substring which replace the old substring.
      count: number of times we want to replace the old substring 
             with the new substring.(Optional)

"""


string = "My name is wane sorry it's wayne not wane."

print(string.replace("wane", "wayne"))   #By default count value will replace all the subsrtings

#------------------------OR-------------------------------

print(string.replace("wane", "wayne", 1 ))


#------------------------OR---------------------------


string = "My name is wane sorry it's wayne not wane.".replace("wane", "wayne")


print(string)



