#Maia Reynolds
#4/24/18
#dictionaryDemo.py - more lists

words=["computer","mortify","dog","firework","yes","python","cat"]

words.sort()

num=int(input("What number word do you want? "))
if num<=0 or num>=len(words)+1:
    print("Invalid Number")
else:
    print(words[num-1])