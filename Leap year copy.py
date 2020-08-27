year=int(input("Enter year: "))
if (year>=1900 and year<=10**5):
    if (year%400==0):
       print("{0} is a leap year".format(year))
    elif (year%4==0):
       print("{0} is a leap year")
    else:
       print("not a leap year :( ")

        
    
   
        
    
   
