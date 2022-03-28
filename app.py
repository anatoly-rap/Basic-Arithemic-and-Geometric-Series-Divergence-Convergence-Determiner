import math
from statistics import mean
import matplotlib
from matplotlib import pyplot as plt
from decimal import Decimal
from fractions import Fraction
import numpy as np

gb = False
ab = False 

def Menu():
    print("Hello, welcome to the sequence Divergence/Convergence Determiner")
    print("What type of sequence will you be looking at today?")
    print("[a]Arithmetic")
    print("[g]Geometric: Expoential, expression rasied to a power") 
               
def grabSeqence(answer):
    
    if answer == 'g':
        
        global gb
        gb = True
        print("Geomtric sequences are in form a_n = ar^(n-1)")
        inputNumbers = list(map(float, input("Please type your numbers here (comma separated): ").split(",")))
        print("a_1 is: " + str(inputNumbers[0]))
        print("Common Ratio is: " + str(inputNumbers[1]))
        return inputNumbers
    
    elif answer == 'a':
        
        global ab
        ab = True
        print("Artithmic sequences are in form of a_n = a_1 + d(n-1) ")
        inputNumbers = list(map(float, input("Please type your numbers here (comma separated): ").split(", ")))
                
        print("a_1 is: " + str(inputNumbers[0]))
        print("Common difference is: " + str(inputNumbers[1]))
        return inputNumbers
    
def getSeq():
    Menu()
    answer = input("[g]eometric or [a]rithemtic?")
    if answer == 'a':
        return answer
    elif answer == "g":
        return answer
    else:
        print("Error- input does not match any of the listed options ")
            
def Determiner(var1,var2):
    x = []  
    y = []
    if gb is True:
        fig, ax = plt.subplots()
        i = 1
        sum = 0
        for i in range(1, i+24):
            sum = sum + ((var1)*(var2))**(i- 1)
            x.append(i)
            y.append(sum)
            
        ax.axis([0, 25, 0, 10])
        ax.scatter(x,y, s = 1.5)
        plt.title('$\sum_{i=1}^\infty' + str(var1) + '\cdot'+ str(Fraction(var2)) +'^{i-1} $')
        
        if abs((var2)) < 1:
            ax.text(0.3,0.1,'Since chosen r,  |' + str(var2) + '| < 1:\n The sequence converges to ' + str(sum)[0:4] +  ' for the first '+ str(np.amax(x)) +' terms',
                    transform=ax.transAxes, fontsize=9, verticalalignment='bottom', horizontalalignment= 'center')
            ax.annotate("sum conversion", xy=(0.3,0.1), xytext=(0.3, 0.1), arrowprops={"arrowstyle":"->", "color":"black"})
            plt.show()                                                                                                      
        elif abs((var2)) >= 1:
               ax.text(0.3,0.1,'Since chosen r, 1 ≤ |' + str(var2) + '|:\n The sequence diverges to ' + str(sum)[0:4] +
                    ' for the first '+ str(np.amax(x)) +' terms',transform=ax.transAxes, fontsize=9, horizontalalignment='center',verticalalignment='bottom')
        plt.show() 
         
    else:
        print("This diverges to infinity. All arithmatic sequences diverge")
        
                 
def main():
    user_input = getSeq()
    Determiner(*grabSeqence(user_input))
    
if __name__ == '__main__':
    main()