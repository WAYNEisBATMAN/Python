"""
3)A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user."""


N=int(input("Enter number of items: "))
C=100*N

if (N>10):

    TC=0.9*C
    print("After 10% off Total Cost is: ",TC,"\n Come back again :)")
else:
    print("Total Cost is:",C,"\nCome back again :)")
