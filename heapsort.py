#Maia Reynolds
#5/3/18
#heapsort.py - heapsort

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def mySort(A):
    N=len(A)
    heapify(A,N)
    end=N-1
    while end>0:
        numbers[-1],numbers[0]=numbers[0],numbers[-1]
        end-=1
        siftDown(A,0,end)




def heapify(A,N):
    end=1
    while end<N:
        siftUp(A,0,end)
        end+=1









def siftUp(A,start,end):
    child=end
    while child>start:
        parent=iParent(child)
        if numbers[parent]<numbers[child]:
            numbers[parent],numbers[child]=numbers[child],numbers[parent]
            child=parent
        else:
            return

def iParent(i):
    return ((i-1)//2)



if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
