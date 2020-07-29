"""
Module ---> A module is a file containing Python definitions and statements. 
            A module can define functions, classes and variables. 
            A module can also include runnable code. 
            Modules provide reusability of code.
            Grouping related code into a module makes the code easier to understand and use.

            Modules can be built-00`   
            in and user-defined both. 

"""

"""
Import Statement ---> We can use any Python source file as a module by executing an import statement 
                      in some other Python source file.


                      Syntax --->  import filename 

"""

# import Function


"""
Import With Renaming ---> We can import a module by renaming it as follows
"""

import Function as F
F.greet()

from Function import *
from Function import greet


"""
Python Module Search Path ---> While importing a module, Python looks at several places. 
                               Interpreter first looks for a built-in module. 
                               Then(if built-in module not found), Python looks into a list of 
                               directories defined in sys.path. 
                               The search is in this order.
                               1. The current directory 
                               2. PYTHONPATH
                               3. The installation-dependent default directory.

"""



"""
Reloading a module ---> The Python interpreter imports a module only once during a session. 
                        This makes things more efficient. Here is an example to show how this works.
                        Suppose we have the following code in a module named my_module
                        print("This code got executed")

                        >>> import my_module
                        This code got executed
                        >>> import my_module
                        >>> import my_module

                        We can see that our code got executed only once. 
                        Which means our module was imported only once.
                        

"""








