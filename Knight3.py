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

def IsOnBoard(x,y):
    c=0
    if (x+1)<n:
        if (y+2)<n:
            c=1
        if (y-2)>=0:
            c=1
    if (x+2)<n:
        if (y+1)<n:
            c=1
        if (y-1)>=0:
            c=1
    if (x-1)>=0:
        if (y+2)<n:
            c=1
        if (y-2)>=0:
            c=1
    if (x-2)>=0:
        if (y+1)<n:
            c=1
        if (y-1)>=0:
            c=1
    return c
def CountMoves(x,y):
    c=0
    if (x+1)<n:
        if (y+2)<n:
            c+=1
        if (y-2)>=0:
            c+=1
    if (x+2)<n:
        if (y+1)<n:
            c+=1
        if (y-1)>=0:
            c+=1
    if (x-1)>=0:
        if (y+2)<n:
            c+=1
        if (y-2)>=0:
            c+=1
    if (x-2)>=0:
        if (y+1)<n:
            c+=1
        if (y-1)>=0:
            c+=1
    return c


N=8
n=N-1
x0=0
y0=0
Moves=4
count=1
x=x0
y=y0
X=[]*Moves
Y=[]*Moves
P=[]*Moves
PP=[]*Moves
Size=[0]*Moves
Size[0]=1
X.append(x)
Y.append(y)
P.append(1)
PP.append(1)
#PP.append([0.0]*20)
#PP[0][10]=12
#print(PP[0][14])
i=0
for i in range(0,Moves-1):
#while(i<Moves-1):
    print("Size in the beginning:%d"%Size[i])
    for j in range(0,Size[i]):
        if i==0:
            x=x0
            y=y0
        else:
            x=X[i][j]
            y=Y[i][j]
        c=CountMoves(x,y)
        Size[i+1]+=c
        print("c:%d-size:%d"%(c,Size[i+1]))
    c2=0
    for j in range(0,Size[i]):
        if i==0:
            x=x0
            y=y0
        else:
            x=X[i][j]
            y=Y[i][j]
        c=Size[i+1]
        print("c %d-Size%d"%(c,Size[i+1]))
        X.append([0]*c)
        Y.append([0]*c)
        P.append([1./c]*c)
        if i==0:
            prob=1./c
        else:
            prob=(PP[i][0]/c)
        PP.append([prob]*c)
        if (x+1)<n:
            if (y+2)<n:
                X[i+1][c2]=x+1
                Y[i+1][c2]=y+2
                c2+=1
            if (y-2)>=0:
                X[i+1][c2]=x+1
                Y[i+1][c2]=y-2
                c+=1
        if (x+2)<n:
            if (y+1)<n:
                X[i+1][c2]=x+2
                Y[i+1][c2]=y+1
                c2+=1
            if (y-1)>=0:
                X[i+1][c2]=x+2
                Y[i+1][c2]=y-1
                c2+=1
        if (x-1)>=0:
            if (y+2)<n:
                X[i+1][c2]=x-1
                Y[i+1][c2]=y+2
                c2+=1
            if (y-2)>=0:
                X[i+1][c2]=x-1
                Y[i+1][c2]=y-2
                c2+=1
        if (x-2)>=0:
            if (y+1)<n:
                print("in if c2:%d-i+1:%d"%(c2,i+1))
                X[i+1][c2]=x-2
                Y[i+1][c2]=y+1
                c2+=1
            if (y-1)>=0:
                X[i+1][c2]=x-2
                Y[i+1][c2]=y-1
                c2+=1
        print("C2 is:%d- i+1 is:%d"%(c2,i+1))
    #i+=1
    print(X)
    print(Y)
    print(P)
    #print(PP)
    #print(Size)
rExpected=0
for i in range(0,Size[Moves-1]-1):
    #print(i)
    print(X[Moves-1][i])
    r2=X[Moves-1][i]**2.+Y[Moves-1][i]**2.
    pr=np.sqrt(r2)*PP[Moves-1][i]
    rExpected+=pr
print("rExpected=%g"%rExpected)




'''
NextMove=np.zeros((N,N))
count=FillNextMove(NextMove,x0,y0)

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

                for k in range(0,N):
                    for l in range(0,N):
                        if NextMove[k,l] !=0:
                            p=1./count
                            Probabilities[k,l]=p*Probabilities[x,y]
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




def IsOpen(px,py,newx,newy):
    return p

matrix2d 0 0 0...0
         0 0 0...0
then fill with probability
if it is possible append struct x,y and count
'''
