import random
import numpy as np
import matplotlib.pyplot as plt
def rolldice():
    result = [1,2,3,4,5,6]
    roll1 = random.choice(result)
    roll2 = random.choice(result)
    combination = roll1 + roll2 
    return combination

roll = [10000]
counter = np.array([0,0,0,0,0,0,0,0,0,0,0])
for i in range (roll[0]):
    comb = rolldice()
    if comb == 2:
        counter[0] += 1
    elif comb == 3:
        counter[1] += 1    
    elif comb == 4:
        counter[2] += 1
    elif comb == 5:
        counter[3] += 1
    elif comb == 6:
        counter[4] += 1
    elif comb == 7:
        counter[5] += 1
    elif comb == 8:
        counter[6] += 1
    elif comb == 9:
        counter[7] += 1
    elif comb == 10:
        counter[8] += 1
    elif comb == 11:
        counter[9] += 1
    elif comb == 12:
        counter[10] += 1
    
for i in range (0,11):
    print ("probability of rolling {} is {}\n".format(i+2,counter[i]/roll[0]))

probability = counter/roll[0]
x_range = [2,3,4,5,6,7,8,9,10,11,12]
plt.bar(x_range,probability)
plt.show()
