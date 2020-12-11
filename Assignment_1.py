# 1.

def nmbr(n):
    if(n%7==0 and n%5!=0):
        return True
    return False


for i in range(2000, 3201):
    if nmbr(i):
        print(i, ",", end='')

# 2.

first = input("Enter First Name")
last = input("Enter Last Name")

first = first[::-1]
last = last[::-1]

print(first,last)



#3.

import math
radius=12
py=math.pi

volume=(4/3)*py*radius**3
print(volume)