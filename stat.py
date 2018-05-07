#Maia Reynolds
#4/27/18
#stat.py - takes list, prints min, max, median, mode, mean


num=input("Enter a list of numbers: ").split(" ").sort()#makes list of numbers and sorts it from smallest to largest

#Max
print("Max =",num[-1])#since the list is sorted by number size, this prints the last number, which is the max

#Min
print("Min =",num[0])#since the list is sorted by number size, this prints the first number, which is the min

#Mean
sum=0
for item in num:#adds all the numbers in the list together
    sum+=int(item)
print("Mean =",sum/len(num))#divides the sum by the amount of numbers in the list to find average

#Median
if len(num)%2==0:#if even amount of numbers in the list
    print("Median =",(int(num[((len(num)/2)-1)])+int(num[((len(num)/2))]))/2)#prints two middle numbers as median
else:#if odd amount of numbers in the list
    print("Median =",num[((len(num)/2)-.5)])#prints middle number as median

#Mode
times=0
for item in num:#runs through each number to see how many times it shows up in the list
    if num.count(item)>=times:#number that appears in the list the most will end up as variable times
        times=int(item)
print("Mode =",times)