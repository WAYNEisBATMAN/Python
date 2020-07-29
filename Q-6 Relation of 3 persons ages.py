#6.Take input of age of 3 people by user and determine oldest and youngest among them.

a=int(input("Enter age of 1st person: "))
b=int(input("Enter age of 2nd person: "))
c=int(input("Enter age of 3rd person: "))

if(a>b and a>c):
    print("a is Older")

if(a<b and a<c):
    print("a is Younger")  

if(b>a and b>c):
    print("b is Older")

if(b<a and b<c):
    print("b is Younger")
     
if(c>b and c>a):
    print("c is Older")

if(c<a and c<a):
    print("c is Younger")

if(a==b):
    print("a and b are of same age")
if(c==b):
    print("b and c are of same age")    
if(c==a):
    print("a and c are of same age")
if(a==b and b==c):
    print("All have same ages")    

