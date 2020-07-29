"""
5) school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
"""

#QUES SEEMS INCOMPLETE,IF MARKS ARE 25,45,50,60 IN WHICH GRADE THEY ARE CONSIDERED?

M=int(input("Enter marks: "))
if (M<25):
    print("Grade is F")
elif (M>=25 and M<=45):
    print("Grade is E")   
elif (M>=45 and M<=50):
    print("Grade is D")
elif (M>=50 and M<=60):
    print("Grade is C")    
elif (M>=60 and M<=80):
    print("Grade is B")

else:
    print("Grade is A") 