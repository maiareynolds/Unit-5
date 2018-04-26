#Maia Reynolds
#4/26/18
#vowelWords.py - how to treat strings as lists

words=input("Enter a list of words: ").split(" ")

for item in words:
    if item[0] in "AEIOUaeiou":
        print(item)
