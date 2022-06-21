import time
import random
import sys
import os
print("multiplication table generator ver 1 ")

print("сколько примеров")
long = int(input(">>>"))

right = 1
left = 9

#print("сложность 1 - 3")
#lvl = int(input())
#if(lvl == 1):
    #r = 1
    #l = 9
#if(lvl == 2):
    #r = 1
    #l = 50
#if(lvl == 3):
    #r = 1
    #l = 99


yes = 0
no = 0

for i in range (long):
    x = random.randint(right, left)
    y = random.randint(right, left)
    n = x * y
    print(x,"*",y)
    r = int(input(">>>"))
    if (r == n):
        yes = yes +  1
    elif (r == ''):
        no = no + 1
    else:
        no = no +  1
print("%",100 * yes / long )
print('правелно',yes ,"неправельно", no )
