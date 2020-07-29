# Create a Time class and initialize it with hours and minutes.
# 1. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method displayTime which should print the time.
# 3. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.


class Time:
    
    a=5
    b="hello"
    
    def __init__(self,hours,minutes):
        t3=Time(0,0)
        self.hours=hours
        self.minutes=minutes
       
    

    def addTime(self,t1,t2,t3):
        self.t1=t1
        self.t2=t2
        return self.t1 + self.t2
    
    def displayTime(self):
        print("Time is",self.hours,"hours and",self.minutes,"minutes")

    def displayMinute(self):
        print(self.hours*60+self.minutes)


class Phone:
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
        print("inside __init__")
    def show(self):
        print(self.brand, self.color, self.size)


Android=Phone("Google Pixel", "Matte Black", "4.7")
Ios=("Iphone", "Gold", "5.6")

# Phone.show(Android)
# Android.show()
# print(Android.show())  
a=Android.show()
def add(a,b):
    print(a+b)

sum=add(1,1)    

print(sum)