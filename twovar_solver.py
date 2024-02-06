def twotwosolver (a1,b1,c1,a2,b2,c2):
    if b1==0:
        x = -c1/a1
        y = (-c2-a2*x)/b2
        return [x,y]
    else:
        x = (b1*c2-b2*c1)/(a1*b2-a2*b1)
        y = (-c1-a1*x)/b1
        return [x,y]

print('Enter the co-efficients for a set of simultaneous equations. \n Remember to use the form ax + by + c = 0 ')

A1,B1,C1 = [int(x) for x in input("enter the coefficients for the first equation\n").split()]
A2,B2,C2 = [int(x) for x in input("enter the coefficients for the second equation\n").split()]

print('The solution to \n',A1,'x + ',B1,'y + ',C1,' = 0 \n ',A2,'x + ',B2,'y + ',C2,' = 0 is: \n ',twotwosolver(A1,B1,C1,A2,B2,C2))
