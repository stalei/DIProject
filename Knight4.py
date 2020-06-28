
import numpy as np

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
Moves=3
Board=np.zeros((N,N))
#print(Board)
Probabilities=np.zeros((N,N))#np.ones((N,N))#zeros((N,N))
TotalProbabilities=np.zeros((N,N))
CurrentPosition=np.zeros((N,N))
CurrentPosition[x0,y0]=1
Probabilities[x0,y0]=1
TotalProbabilities[x0,y0]=1
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
                Ptemp=np.zeros((N,N))
                count=FillNextMove(NextMove,x,y)
                for k in range(0,N):
                    for l in range(0,N):
                        if NextMove[k,l] !=0:
                            p=1./count
                            #print("p:%g- probab:%g "%(p,Probabilities[x,y]))
                            Ptemp[k,l]=p*Probabilities[x,y]
                Probabilities[x,y]=0
                print("Next:")
                print(NextMove)
                print("Probabilities:")
                print(Probabilities)
                #TotalProbabilities[x,y]=0
                Probabilities+=Ptemp
    CurrentPosition=NextMove
    M+=1
rExpected=0
#Probabilities=TotalProbabilities
for i in range(0,N):
    for j in range(0,N):
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
