#   1 
#   2    1 
#   4    2    1 
#   8    4    2    1 
#  16    8    4    2    1 
#  32   16    8    4    2    1 
#  64   32   16    8    4    2    1 
# 128   64   32   16    8    4    2    1

for i in range(128,0,-2i):
    for j in range(i,0,-2*i):
        print(j, end=" ")
    print(" ")    