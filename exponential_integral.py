#A python program that can integrate the exponential integral
#input n, x and N (Number of iterations)
#output shows the result
#This method uses monte carlo method
#the infinite limits have been substituted by finite limits by
#using a substitution mu=1/t
###################################################################################

import numpy as np 

n,x,N =  [int(x) for x in input("enter n, x and N for the exponential integral\n").split()]

mu= np.random.uniform(0,1, size = N) 

y = np.e**(-x/mu) * mu**(n-2)

integral = 0 
for i in range (0,N):
    integral += (1/N) * y[i] 

print(integral)