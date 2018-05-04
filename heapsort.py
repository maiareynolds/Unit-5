#Maia Reynolds
#5/3/18
#heapsort.py - heapsort

from random import randint
from time import time

N = 1000 #how many numbers will be sorted

def mySort(A,count):
    heapify(A,count)
    end=count-1
    while end>0:
        numbers[end],numbers[0]=numbers[0],numbers[end]
        end-=1
        siftDown(A,0,end)
    return A

def heapify(A,count):
    start=iParent(count-1)
    while start>=0:
        siftDown(A,start,count-1)
        start-=1

def siftDown(A,start,end):
    root=start
    while iLeftChild(root)<=end:
        child=iLeftChild(root)
        swap=root
        if A[swap]<A[child]:
            swap=child
        if (child+1)<=end and A[swap]<A[child+1]:
            swap=(child+1)
        if swap==root:
            return
        else:
            A[root],A[swap]=A[swap],A[root]
            root=swap

def iParent(i):
    return ((i-1)//2)

def iLeftChild(i):
    return ((2*i)+1)


if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers,N)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
