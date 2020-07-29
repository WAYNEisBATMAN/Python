 """
The slice object is used to slice a given sequence (string, bytes, tuple, list or range) 
or any sequential type objects.

Syntax -------->  slice(start,stop,step)  
           
       -------->  sequence[start:stop:step] 

Where:
     start: Starting index from where the slicing of object starts.
     stop: Ending index to where the slicing of object stops.
     step: It is an optional argument that determines the increment between each index for slicing.



"""


#There are two methods for slicing any sequential data type.




a=[1,2,3,4,5]            #List
b=(1,2,3,4,5)            #Tuple
c="WAYNEisBATMAN"        #string


#1st method is by using slice function.

x=slice(0,5,-2)
a[x]
print(a)


#2nd is by using indices in square bracekts

print(a[2:5:2])





















