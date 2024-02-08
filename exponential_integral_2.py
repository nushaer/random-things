#A python program that can integrate the exponential integral
#input n, x and N (Number of iterations)
#output shows the result
#This method uses monte carlo method
#the infinite limits have been substituted by finite limits by
#using a substitution mu=1/t
###################################################################################

import numpy as np 



def expo_integ(n,x,N):
    
    mu= np.random.uniform(0,1, size = N) 

    y = np.e**(-x/mu) * mu**(n-2)

    integral = 0 
    for i in range (0,N):
        integral += (1/N) * y[i] 

    return integral

def standard_dev(arr, sample):
    variance = 0
    mean = np.mean(arr)
    for i in range(0,sample):
        variance += (1/(sample-1)) * (mean - arr[i])**2

    std_dev = np.sqrt(variance)
    return std_dev


#n,x,N =  [int(x) for x in input("enter n, x and N for the exponential integral\n").split()]
n,x,N = 1,1,1000
L = 20
I = np.zeros(20, dtype=float)
for i in range(L):
    I[i] = expo_integ(n,x,N)

#print(I)
#print(standard_dev(I,L))
#print(np.std(I))
    
print((standard_dev(I,L) - np.std(I))/np.std(I))


