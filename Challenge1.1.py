# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 17:21:02 2018

@author: Ankit Goyal
"""

import numpy as np
import pandas as pd
# Method to get the maximum rope size after breaking at 2 internal points
def get_rope(N):
    arr=np.array(range(N))
    arr=arr[1:N]
    rand=np.random.choice(arr,2,replace=False)
    rand=np.array(rand)
    l1=np.amin(rand)
    l2=(N-np.amax(rand))
    l3=abs(rand[0]-rand[1])
    ropes=np.array([l1,l2,l3])
    return(np.amax(ropes))

## This is method to do T operations
def iterat(T,N):
    S=np.zeros(T)
    for var in range(T):
        if N<=2:
            break
        else:
            S[var]=get_rope(N)
            N=S[var].astype(int)
            #print(S[var])
            if N==2:
                return(S[var])
    return(S[T-1])

#we simulate this over a large sample size. (Can turn this into a method if required, with arguments T, N and sample size)
prr=np.zeros(100000)
mrr=np.zeros(100000)
for i in range(100000):
    prr[i]=iterat(5,64)
avg=format(np.average(prr),'.10f')
print(avg)
print(np.std(prr))

## Method to get conditional probability based on matrix generated above for specific question 
def get_probab(prr,cond1,cond2):
    count=0
    for i in range(100000):
        if prr[i]>=cond1:
            mrr[i]=prr[i]
            count=count+1
    print(count)
    count1=0
    for i in range(100000):
        if mrr[i]>=cond2:
            count1=count1+1
    print(count1)
## Probability of S>8 given it is >4 is 
    return(float(count1)/count)
#print(get_probab(prr,6,12))
        
        
        
        