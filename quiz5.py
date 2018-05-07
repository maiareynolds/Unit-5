#Maia Reynolds
#5/7/18
#quiz5.py - four functions with lists

def penultimate(list1): #takes second to last item in list
    return list1[-2]

def plusEquals(list2,integer): #makes new list with integer added to each item
    newlist=[]
    for item in list2:
        newlist.append(item+integer)#adds new number to newlist
    return newlist

def smallest(list3):#returns smallest number
    list3.sort()#orders list from smallest to largest number
    return list3[0]#takes first number

def decimalRange(num1,num2,num3):#makes list of range from num1 to num2, using intervals of num3
    list4=[]
    while num1<num2:
        list4.append(num1)#adds new number to list
        num1+=num3
    return list4

#test
print(penultimate([3,4,5,6,7]))
print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
print(decimalRange(4,10,0.5))