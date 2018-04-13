#Maia Reynolds
#4/13/18
#listDemo.py - prints first and last words of list

words=input("Enter words: ").split(" ")
print(words)
print("The first word is: ",words[0])
print("The last word is: ",words[-1])

#prints all words
for item in words:
    print(item)