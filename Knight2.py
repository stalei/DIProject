import datetime as dt
import os
import csv
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
from datetime import timedelta, date
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import chisquare

def FillNextMove(NextMove,x,y):
    c=0
    if (x+1)<n:
        if (y+2)<n:
            NextMove[x+1,y+2]=1
            c+=1
        if (y-2)>=0:
            NextMove[x+1,y-2]=1
            c+=1
    if (x+2)<n:
        if (y+1)<n:
            NextMove[x+2,y+1]=1
            c+=1
        if (y-1)>=0:
            NextMove[x+2,y-1]=1
            c+=1
    if (x-1)>=0:
        if (y+2)<n:
            NextMove[x-1,y+2]=1
            c+=1
        if (y-2)>=0:
            NextMove[x-1,y-2]=1
            c+=1
    if (x-2)>=0:
        if (y+1)<n:
            NextMove[x-2,y+1]=1
            c+=1
        if (y-1)>=0:
            NextMove[x-2,y-1]=1
            c+=1
    return c


N=8
n=N-1
x0=0
y0=0
Moves=10
Board=np.zeros((N,N))
#print(Board)
Probabilities=np.ones((N,N))#zeros((N,N))
CurrentPosition=np.zeros((N,N))
CurrentPosition[x0,y0]=1
M=0
while(M<Moves):
    print("Movement %d Current position:"%M)
    print(CurrentPosition)
    for i in range(0,N):
        for j in range(0,N):
            if CurrentPosition[i,j] !=0:
                x=i
                y=j
                c=0
                NextMove=np.zeros((N,N))
                count=FillNextMove(NextMove,x,y)
                for k in range(0,N):
                    for l in range(0,N):
                        if NextMove[k,l] !=0:
                            p=1./count
                            Probabilities[k,l]=p*Probabilities[x,y]
                Probabilities[x,y]=1
                print("Next:")
                print(NextMove)
                print("Probabilities:")
                print(Probabilities)

    CurrentPosition=NextMove
    #print("%d Next Move:"%count)
    #print(NextMove)
    #print("Final:")
    #print("Probabilities:")
    #print(Probabilities)
    M+=1
rExpected=0
for i in range(0,N):
    for j in range(0,N):
        if Probabilities[i,j]==1:
            Probabilities[i,j]=0
        else:
            rExpected+=np.sqrt(i*i+j*j)*Probabilities[i,j]
print("Final:")
print("Probabilities:")
print(Probabilities)
print("Expecation value of r is:%g"%rExpected)

sigmaExpected=0
sig=0
for i in range(0,N):
    for j in range(0,N):
        r2=i*i+j*j
        sig+=((np.sqrt(r2)-rExpected)**2.)*Probabilities[i,j]
sigmaExpected=np.sqrt(sig)
print("Expected value of standard deviation:%g"%sigmaExpected)

PP=[]*Moves
PP.append([0.0]*20)
PP[0][10]=12
print(PP[0][14])

'''
def IsOpen(px,py,newx,newy):
    return p

matrix2d 0 0 0...0
         0 0 0...0
then fill with probability
if it is possible append struct x,y and count
'''
