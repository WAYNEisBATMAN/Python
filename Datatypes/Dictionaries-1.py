"""
Dictionary ---> Dictionary is an unordered collection of data values, used to store data values like a map, 
                which unlike other data Types that hold only single value as an element,  holds key:value pair. 

                keys and values both can be boolean,integer,string,float,tuple
                
                are identified by curly braces d={2:2, 3.5:3.5, "hey":"hey", (2,3):(3,30), true:true}

                keys are case sensitive, same name but different cases of Key will be treated distinctly

                "Values in a  can be of any datatype and can be duplicated, whereas keys can’t be repeated 
                 must be immutable."


■ Nested Dictionary ---> A dictionary can contain another dictionary, 
                         which in turn can contain dictionaries themselves.
                         This is known as nested dictionary.
                                                

"""
#---------------------------------------------------------------------------------------------------------------

"""
1. Creating dictionary ---> In python dictionaries can be created by putting sequence of elements within curly 
                            braces {}  each of them are separated by 'comma'. 
                            Values can be empty or spacebar.
 
                           for example:    "key" : "   

NOTE: False  True are keywords which means they are already defined in Python.
      so we dont have to use the quotes to make them string
      They are also known as boolean values.

"""
print("\nCreating dictionary D")

D={2:2, 3.5:3.5, "hey":"true", False:True, (2,3):(3,30)}

print(D)


#-----------------------------------------------------------------------------------------------------------------


"""
2. Adding elements to dictionary --->  We can add elements in an existing  or we can first create 
                                          an empty dictionary and then add elements in it.
                                    
(i) Adding elements one at a time : 
       d1[key] = value 
    Note: This is also use to update value of keys.

(ii) Another way of updating value of keys :
       d1.update({'name':'batman'})

(iii) Adding nested key value to    
       d1[key] = d1

     In nesting some other  is used as a value for a key in another (More in detail about nested dictionary later)

"""
print("\nAdding elements to  d1")

d1={}  
print(d1)

d1[55] = 2
print(d1)   

d1[True] = False                 
print(d1)

d1["true"] = "false"
print(d1)

d1.update({"true":"try"})
print(d1)

#-----------------------------------------------------------------------------------------------------------------

"""
3. Deletion in dictonary  ---> In Python , deletion of keys as well as whole  can be done 
                               by using the del keyword.                               
                             
                               Items in a Nested  can also be deleted by using del keyword.

                               SYNTAX:   For deletion of key                --->  del [key]
                                         For deletion of whole              --->  del dictionary

"""
print("\ndeletion in W")

W={2:2, 3.5:3.5, "hey":"true", False:True, (2,3):(3,30)}

del W[2]
print(W)

del W[(2,3)]
print(W)

del W[False]
print(W)

#-------------------------------------------------------------------------------------------------------------

"""
4. Length of dictionary:           len(dictionary)        
                        

"""

DY={2:3,"the":"hell"}
print(len(DY))














