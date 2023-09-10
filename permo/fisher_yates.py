#This is fisher yates shuffle algorithm
from random import randint

def shuffle(list=[1,2,3,4]):
    length = len(list)
    pointer = length -1
    
    newlist = []

    for i in range(length):
        r = randint(0,pointer)
        newlist.append(list[r]) 
        list.pop(r) 
        pointer -= 1
    print(newlist)

shuffle()
