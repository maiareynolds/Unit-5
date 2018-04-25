#Maia Reynolds
#4/25/18
#warmUp13.py - list of 20 random numbers, find sum, min, max, etc.

from random import randint
numbers=[]
i=0
while i<20:
    numbers.append(randint(1,100))
    i+=1
print(numbers)
print("The sum is ",sum(numbers))
print("The minimum number is",min(numbers))
print("The maximum number is ",max(numbers))
