import math
from statistics import mean
import matplotlib
from matplotlib import pyplot as plt
from decimal import Decimal
from fractions import Fraction
import numpy as np

ab = False
gb = False

def menu():
    
    print("Hello, welcome to the sequence Divergence/Convergence Determiner")
    print("What type of sequence will you be looking at today?")
    print("[a]Arithmetic")
    print("[g]Geometric: Expoential, expression rasied to a power") 
    
def Arth():
    
    print("Artithmic sequences are in form of a_n = a_1 + d(n-1) ")
    a_1 = input("a_1 is the first term in the sequance, which is ")
    d = input("d is the common difference, which is ")
    global ab
    ab = True
    return a_1, d
            
def Geometric():
    
    print("Geomtric sequences are in form a_n = ar^(n-1)")
    var_a = input("what is the starting value of the sequence?[value of a)? ")
    var_r = input("what is the common ratio of your geometric sequence? ")
    global gb
    gb = True
    return var_a, var_r
   
def getSeq():
    
    menu()
    answer = input()
    if answer == 'a':
        Arth()
    elif answer == "g":
        Geometric()
    else:
        print("Error- input does not match any of the listed options ")
            
def getL():
    
    x = []  
    y = []
    fig, ax = plt.subplots()
    
    if gb is True:
        i = 1
        sum = 0 
        var_a, var_r = Geometric()
        for i in range(0, i+25):
            sum = sum + (int(var_a)* float(var_r))**(i- 1)
            x.append(i)
            y.append(sum)
            
        plt.scatter(x,y, s = 1.5)
        plt.title('$\sum_{i=1}^\infty' + str(var_a) + '\cdot('+ str(Fraction(var_r)) +')^{i-1} $')
        
        if abs(float(var_r)) < 1:
            ax.text(0.3,0.1,'Since chosen r:  |' + str(var_r) + '| < 1.\n The sequence converges to ' + str(sum)[0:4] +  ' for the first '+ str(np.amax(x)) +' terms',
                    transform=ax.transAxes, fontsize=9, verticalalignment='bottom', horizontalalignment= 'center')
            plt.show()                                                                                                      
        elif abs(float(var_r)) >= 1:
               ax.text(0.3,0.1,'Since chosen r: 1 ≤ |' + str(var_r) + '|. \n The sequence diverges to ' + str(sum)[0:4] +
                    ' for the first '+str(np.amax(x)) +' terms',
                    fontsize=9, transform=ax.transAxes, horizontalalignment='center',verticalalignment='bottom')
        plt.show()
        
    elif ab is True:
        print("this diverges to Infinity. All arithmatic sequences diverge")
                 
def main():
    getSeq()
    getL()
if __name__ == '__main__':
    main()