#Maia Reynolds
#4/23/18
#middleWord.py - prints middle word

words=input("Enter a list of words: ").split(" ")
if len(words)%2==0:
    print(words[((len(words)/2)-1)])
    print(words[((len(words)/2))])
else:
    print(words[((len(words)/2)-.5)])