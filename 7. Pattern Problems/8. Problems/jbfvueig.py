"""
A List in Python is a kind of Collection that allows us to put many values in a single “variable”.

Lists need not be homogeneous always which makes it a most powerful tool in Python. 
A single list may contain different DataTypes like Integers, Strings, as well as Objects. 
Lists are mutable, and hence, they can be altered even after their creation.

■ List is An ordered set of values:

1)Ordered: elements are assigned to index values in the list.

2)Index: Always start with zero from left and -1 from right.

3)Values: can be any datatype like integers, strings, other lists

4)List values are called elements.

A string is an ordered set of characters so it is “like” a list but not exactly the same thing.

The list of all functions which can be use with Python Lists:
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
'__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__','__repr__', '__reversed__', '__rmul__',
 '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
 ■ All the following functions have a syntax as  
 listname.functionname()
 'append', 
 'clear'-- empty the list as [] on the other hand del listname will delete the list and the 
 list name is also become undefined. 

 'copy', 'count', 'extend', 'index', 'insert', 
 'pop', 'remove', 'reverse', 'sort']

"""
print("\nLISTS")

"""
1. Accessing elements of a list ---> There are two ways to access elements from a list.
                                     ■ By using name of list and index in square bracket
                                     ■ Using pop(index) method, By default index will be random.            
"""  
print("\nAccessing elements")
y = [1,2,"no",3,4,5,6,"yes"]                  
print(y)
print(y[0])
print(y.pop())          
print(y.pop(2))


#---------------------------------------------------------------------------------------------------------------

"""
2. Add or update element ---> There are two methods two add/insert elements in a list.
                              ■ append
                              ■ insert 
                              The main difference between both functions is that:
                              In insert we have a freedom to insert the element at any index in the list we liked.
                              In append the element will add at the end of the list.

                              Syntax --->   list_name.append(element)
                                            list_name.insert(index, element)
 
"""

print("\nAdd or update elements")
x=[0,1,0,2,0,3]
x.append(4)
x.insert(2, "dvd")
print(x)

x[0]=1              #Update elements
print(x)

#----------------------------------------------------------------------------------------------------------------

"""
3. Remove/delete element 

"""
print("\nRemove/delete elements")
x.remove(0)
print(x)

del x[0]
print(x)

# --------------------------------------------------------------------------------------------------------------

"""
4. Sorting a list ---> There are two ways of sorting a list0 
                       1st is permanent sorting by using sort() or sort(inverse=True)

                       sort()     sorts list in ascending order
                       sort(reverse=True)    sorts in descending order

                       There is one more method like sort(reverse=True)    which is reverse()
                       In this method list will just reverse without any order the last element will be 1st
                       and 1st will be last and so on.
                       

"""
print("\nSorting a list")
mylist=["jan", "nov", "sep", "feb"]
print(mylist)

mylist.sort()  
print(mylist)  

mylist.sort(reverse=True)
print(mylist)

mylist=["jan", "nov", "sep", "feb"]

mylist.reverse()
print(mylist)


"""
2nd is temporary sorting by using sorted(listname)  
Note: syntax here is different, we can also use it inside the print command.

"""
mylist=["jan", "nov", "sep", "feb"]
print(sorted(mylist))                        # Temporary Sorted list
print(mylist)                                # Gives the orginal list

#---------------------------------------------------------------------------------------------------------------

"""
5. Copying a list ---> To make a copy of a list a and create a new list b

                                     b=a[:]

"""
print("\ncopying a list")
a=[1,2,3,4,5] 
b=a[:]
print(b)

#---------------------------------------------------------------------------------------------------------------

"""
6. Merge/join two lists ---> There are different ways to do this
                             ■ Simple concatenation by using addition symbol " + "
                             ■ For loop + append
                             ■ Extend() method
                             

"""
print("\nMerge/Join lists")
x = [1,2,3,4,4]
y = ["hello", 3,4,5,6,7]
print(x+y)
# or
z = x + y
print(z)

#---------------------------------------------------------------------------------------------------------------

"""
7. Using Loop inside a list ---> 

"""

mylist = [1, 2, 3, 4, 5, 6]

print("\nFor loop")
for WTF in mylist:
    print(WTF)

print("For loop + slice ")

for WTF in mylist[-3::2]:
    print(WTF)

#---------------------------------------------------------------------------------------------------------------

"""
8. Some extra methods used in lists

"""
print("\nmax. min, sum, length in list")
print(min(mylist))
print(max(mylist))
print(sum(mylist))
print("length of the list = ", len(mylist) )

#---------------------------------------------------------------------------------------------------------------




