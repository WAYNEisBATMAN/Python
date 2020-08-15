"""
https://pynative.com/print-pattern-python-examples/

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5

"""

# Here each rows has no. of entries equal to its value like in 3rd row there are 3 entries.
# And all the entries are same
# for num in range(5):
rows = 6
for num in range(6):
    for i in range(num):
        print(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")


# rows = int(input("give"))
for num in range(6):
    for i in range(num):
        print(i, end=" ")
    print(" ")


print(" ")
for num in range(5):
    for i in range(num):
        print(num, end=" ")
    print(" ")    

print(" ")
for num in range(5):
    for i in range(num):
        print(i, end=" ")
    print(" ")        

print()



# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

print(" ")
for i in range(7):
    for j in range(1,i):
        print(j,end=" ")
    print(" ")    
print(" new ")

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

for i in range(6):
    for j in range(i,-1):
        print(j, end=" " )
    print(" ")







