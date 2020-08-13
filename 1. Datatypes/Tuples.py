"""

A Tuple is an ordered collection of unchangeable Python objects.
A tuple is enclosed in a parentheses and all objects are separated by commas.
A tuple is similar to a list in terms of indexing, nested objects and repetition 
but a tuple is immutable unlike lists which are mutable.
Means they are not liable to change.


List is created by square brackets[] but tuples are created by paranthesis()

"""

x=(2,3,"d",6,8)
print(x)

y=2,3,"d",6,8            # If we just assign values without any paranthesis it will take it as tuple.
print(y)


#--------------------------------Concatenation in Tuples--------------------------------------

z=x+y  
print(z)


#Tuples cant change they can only be be overwritten.

#For loop in tuples

mytuple=(1,4,"halo",44)
for WTF in mytuple:
    print(WTF)
    

#-----------------------------------Nesting of tuples-----------------------------------------

tuple1 = (0, 1, 2, 3) 

tuple2 = (tuple1, 'wayne')  
tuple3 = (tuple2, 4) 
tuple4 = (tuple1, tuple2, tuple3) 
print(tuple1)
print(tuple2)
print(tuple3) 
print(tuple4)

#----------------------------------Repetition in tuples--------------------------------------

"""
Sometime we want to create a tupple with same elements many times, for this we dont have to 
write same element every time.
Just use the repetition method by multiplying the single element tuple by number of time 
we want the element in the tuple.

NOTE: Don't forget to add the comma in the end of the element otherwise it will create a big string0
      instead of a tuple. 

"""

# Notice the difference between this two outputs

mytuple1 = ("wayne", )*5
print(mytuple1)

mytuple2 = ("wayne")*5
print(mytuple2)

#-----------------------------------------------Slicing in Tuples-------------------------------------------------

print("Start")
mytuple4 = (0,3,45)
print(mytuple3[2:4])
mytuple3 = (0,5)


#--------------------------------------------Converting list to a Tuple--------------------------------------------


mylist = [1,2,3,4]
print(tuple(mylist))       # Converting a list into a tuple 
print(tuple("string"))     # Converting a string into a tuple 
print(max(mytuple3))
print(min(mytuple4))
print(min(mytuple4, mytuple3))

#-----------------------------------------------Deleting a tuple-------------------------------------------------
mytuple4 = ( 0, 1) 
del mytuple4 
print(mytuple4) 

#---------------------------------------------------Unpacking of










