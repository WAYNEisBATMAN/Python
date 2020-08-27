"""

A Set is an unordered collection of different data types with no duplicate elements.
Sets have no order and also Sets do not support indexing.(Unordered and Non-indexing)
Duplicate elements are eliminated automatically at the time of inizialitation.
Sets are identified by curly braces set={1,"d",2} ,  or like set=set((1, "d", 2)) 
Sets are immutable just like tuples.
 
Sets in Python can also be be used to perform mathematical set operations 
like union, intersection, difference and symmetric difference.
 
"""

a={1,2,"set","set","set1"}
#or
a=set((1,2,"set","set","set1"))
print(a,"\n")
print(len(a))

# Convert list into set.  set_name = set([1,2,3])

x=set([1,"dog",4])

#To add a single value in the set  use     set.add(value)


a.add("hey")
a.add(6)

print("\n",a)
print("\n",a)

#To add multiple values in the set use     set.update([value1,value2,,,,])

a.update([4,5.5,"hmm"])
print(a)


b={1,2,"set",5,7}

# Just like all mathematical set operations we can perform 
# all those operations in python too.

#For union by using the or(|) opertaor.

print(a | b)
print(a.union(b))

#For intersection by using the and(&) opertaor.

print(a & b)
print(a.intersection(b))

#Difference between sets  a-b means it results those 
#elements which are in a but not in b.

print(a-b)
print(a.difference(b))

# Symmetric difference elements which are in a but not in a
# and elements which are in b but not in a.
 
print(a^b)
print(b^a) #Result will be same in both cases. 

print(a.symmetric_difference(b)) 
print(b.symmetric_difference(a))#Result will be same in both cases.


# pop() removes a random value from the set and the give the value as result.
# set.pop()
  

print(a.pop())
print(a.pop())
print(a.pop())


#To remove elements from the set.
#There are two ways to do that 1) set.remove(value)  2) set.discard(value)
#The only difference between remove and discard is that when removing
#the element which is not in the set  the remove function shows the error
#but discard function won't shows any error.

print(a.discard(100))

# print(a.remove(100)) will shows error and stops the program here.



# Clear a set
print(a.clear())

print(a)

del a

print(a)





