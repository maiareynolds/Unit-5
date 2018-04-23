#Maia Reynolds
#4/23/18
#fWordDemo.py - print words with F

words=input("Type in some words: ").split(" ")
for item in words:
    if "f" in item or "F" in item:
        print(item)
