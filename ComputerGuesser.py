# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 12:47:20 2017

@author: Dbrimmer
"""

#ComputerGuesser

def Computerguesser(lower,upper):
    num = random.randrange(lower,upper)
    possiblerange=[lower,upper]
    numguesses=0
    b= (upper - lower)//2
    print(b)
    while b!=num:
        if b<num:
            possiblerange[0]=b
        elif b>num:
            possiblerange[1]=b
        diff= (possiblerange[1]-possiblerange[0])//2
        b= possiblerange[0]+diff
        numguesses = numguesses + 1
        print(b)
    print("Congratulations, it only took you", numguesses, "tries to get it right!" )
Computerguesser(0,5000)
