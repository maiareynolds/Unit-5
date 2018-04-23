#Maia Reynolds
#4/23/18
#longestWord.py - prints longest word from list

words=input("Enter a list of words: ").split(" ")
length=0
for item in words:
    if len(item)>=length:
        length=len(item)
        word=item
print("The longest word is",word)