"""

                                            OBJECT ORIENTED PROGRAMMING
==============================================================================================================================

Python is an object-oriented programming language. 
It allows us to develop programs and applications using an Object Oriented approach. 
In Python, we can easily create and use classes and objects.


                                                      OBJECT
==============================================================================================================================

An object has two characteristics:

(a) attributes
(b) behavior

Everything in Python is an object, and almost everything has attributes and methods. 
All functions have a built-in attribute,
The method is a function that is associated with an object.



                                                       CLASS
==============================================================================================================================

A class is a blueprint for the objects.
The class can be defined as a collection of objects. 
It is a logical entity that has some specific attributes and methods. 
For example: if we have an employee class then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.

CLASS are created exactly like functions

While defining classes we can write two main things in the body of a class :  1) Attributes --> Variables
                                                                              2) Behaviour ---> Methods(Functions)



"""
       
        
"""
Here when we created 1st object i.e, samsung!
It actually takes 4 arguments instead of 3(brand,color,size)
1st argument called self which is default for any class. It refers to the object itself.
Which automatically assigned to the class so here self means samsung. 

"""


"""
==========================================================CONSTRUCTORS=======================================================

A constructor is a special type of method (function) which is used to instantiating/create the instance members(objects) of the class.
In C++ or Java, the constructor has the same name as its class, but it treats constructor differently in Python. 
The __init__() method is called the constructor in Python and is always called when an object is created.

■ Constructors can be of two types.

1) Parameterized Constructor     : The default constructor is simple constructor which doesn’t accept any arguments.
                                   It’s definition has only one argument which is a reference to the instance being constructed.
2) Non-parameterized Constructor : constructor with parameters is known as parameterized constructor.
                                   The parameterized constructor take its first argument as a reference to the instance being 
                                   constructed known as self and the rest of the arguments are provided by the programmer.


In Python, the method the __init__() simulates the constructor of the class. 
This method is called when the class is instantiated. 
It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.

"""


"""
---------------------------------------------------Types Of Variables In OOPS----------------------------------------------------------------

1)Instance Variables       ---> Which are defined inside a constructor definition and can differnt for each instance/object.
                                It has local scope.

2)Class(Static) Variables  ---> Which are defined inside a class but outside definitions and is same for each instance/object.
                                It has global scope.


"""







