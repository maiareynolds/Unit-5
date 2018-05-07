#Maia Reynolds
#5/7/18
#quiz5.py - 

def penultimate(list1):
    return list1[-2]

def plusEquals(list2,integer):
    newlist=[]
    for item in list2:
        newlist.append(item+integer)
    return newlist

def smallest(list3):
    list3=list3.sort()
    return smallest

def decimalRange(num1,num2,num3):
    list4=[]
    while num1<=num2:
        list4.append(num1)
        num1+=num3
    return list4

print(penultimate([3,4,5,6,7]))
print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
print(decimalRange(4,10,0.5))