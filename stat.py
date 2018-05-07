#Maia Reynolds
#4/27/18
#stat.py - takes list, prints min, max, median, mode, mean


num=input("Enter a list of numbers: ").split(" ")#makes list of numbers

#max
maximum=0
for item in num:#runs through each number and makes maximum the largest number
    if int(item)>=maximum:
        maximum=int(item)
print("Max =",maximum)

#min
minimum=maximum
for item in num:#runs through each number in the list, and makes minumum the smallest number
    if int(item)<=minimum:
        minimum=int(item)
print("Min =",minimum)

#mean
sum=0
for item in num:#adds all the numbers in the list together
    sum+=int(item)
print("Mean =",sum/len(num))#divides sum by the length of the list to find average

#median
num=num.sort()#orders numbers
if len(num)%2==0:
    print("Median =",(int(num[((len(num)/2)-1)])+int(num[((len(num)/2))]))/2)
else:
    print("Median =",num[((len(num)/2)-.5)])

#mode
times=0
for item in num:
    if num.count(item)>=times:
        times=int(item)
print("Mode =",times)