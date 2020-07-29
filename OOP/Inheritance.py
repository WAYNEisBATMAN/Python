"""
------------------------------------------------------INHERITANCE------------------------------------------------------------

Inheritance is the capability of one class to derive or inherit the properties from another class.
                                            OR
Inheritance allows us to define a class that inherits all the methods and properties from another class.                                            

(i)  Parent Class :  is the class being inherited from, also called base class.

(ii) Child Class  : is the class that inherits from another class, also called derived class.

"""
# ----------------------------------------------------------------------------------------------------------------------------

"""

■  Advantages of Inheritance  ■


1. The main advantage of the inheritance is that it helps in the reusability of the code. 
   The codes are defined only once and can be used multiple times.  

2. It improves the program structure which can be readable.

3. The codes are easy to debug, Inheritance allows the program to capture the bugs easily.

4. Inheritance makes the application code more flexible to change.

5. Inheritance results in better organization of codes into smaller, simpler and simpler compilation units.

6. Also, it allows us to add more features to a class without modifying it.

7. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B 
   would automatically inherit from class A.

"""

#----------------------------------------------------------------------------------------------------------------------------

"""

■  TYPES OF INHERITANCE   ■


1) Single Inheritance : Single inheritance enables a derived class to inherit properties from a single parent class only.
                        
                                     _____
                                     | A |              A is Base class for B 
                                     |___|
                                       ↓
                                      _↓_
                                     | B |              B is Sub class of A 
                                     |___| 


2) Multiple Inheritance : When a class is derived from more than one base classes this type of inheritance is called multiple inheritance. 
                          In multiple inheritance, all the features of the base classes are inherited into the derived class.
         
                                     _____                            _____                               
                                     | A |                            | B |            
                                     |___|                            |___|   
                                       ↓                                ↓
                                       ↓                                ↓
                                       ↓                                ↓
                                       ↓---------------→-←---------------         C inherits properties of both A and B     
                                                        ↓
                                                        ↓                    
                                                        ↓
                                                       _↓_
                                                      | C | 
                                                      |___|


3) Single Level Inheritance : When there is only one superclass(base/parent class) and one subclass(derived/child class).

                                     _____
                                     | A |              A is Base class for B 
                                     |___|
                                       ↓
                                      _↓_
                                     | B |              B is Sub class of A 
                                     |___| 


4) Multi Level Inheritance : When there is more than 1 superclass and subclass
                                      
                                     _____
                                     | A |              A is Base class for B 
                                     |___|
                                       ↓
                                      _↓_
                                     | B |              B is Sub class of A and Base class for C
                                     |___|  
                                       ↓
                                     __↓__
                                     | C |              C is subclass of B but B is subclass of A so C inherit properties of 
                                     |___|              both A and B                         

"""

# ----------------------------------------------------------------------------------------------------------------------------

"""

■ How Constructor Behaves in Inheritance ■ 
* (https://www.youtube.com/watch?v=6P-P879BcHQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=60)

When we create an object of SubClass but it doesn't have any constructors then it will call the constructor of superclass.
But when our subclass already have a constructor then it will only call constructor of subclass and it won't call constructor 
of superclass.

If both the super and sub classes have their own constructors,
and if we want to call constructor of superclass alongwith constructor of subclass.
For this purpose a keyword   "super.__init__()"  is used. 

Now there arises another case what if we have two super classes, then which super class constructor is called by 
super.__init__() keyword ???

Answer is MRO(Method Resolution Order)




"""

class SuperClass():
  
  def __init__(self):
    print("in init SuperClass")

  def definition1(self):
    print("definition1 is working")

  def definition2(self):
    print("definition2 is working")

class SubClass(SuperClass):
  
  @staticmethod
  def definition3():
    print("definition3 is working")
  
  def definition4(self):
    print("definiton4 is working")

S1=SubClass() 
S1.definition3()


# 












