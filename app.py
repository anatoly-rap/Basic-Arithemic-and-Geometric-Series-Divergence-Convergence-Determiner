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
    print("_______________________________________________________@Author Anatoly Rapport")
    print("   _oo_")
    print("   \                             This program evaluates if a geometric sequence")                                 
    print("        _1_                      converges or diverges, plotting the results")
    print("   /    n^2                      for i-iterations.")
    print("   ___")
    print("  n = 0")
    print("What type of sequence will you be looking at today?")
def grabSeqence(answer):
    if answer == 'g':
        global gb
        gb = True
        print("Geomtric sequences are in form a_n = ar^(n-1)")
        inputNumbers = list(map(float, input("Please type your geoemtric variables here(format: a_n,r): ").split(",")))
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
    if gb is True:
        fig, ax = plt.subplots()
        sum = 0
        for i in range(1, 30):
            sum += math.pow((var1*var2), i-1)
            x = [i for i in range(1, 30)]
            y = [sum(y[:i]) for i in range(1, 30)]
        ax.axis([0, 30, 0, max(y)+ 1])
        ax.scatter(x,y, s = 1.8, color = "red", label = "a_n sequence")
        plt.title('$\sum_{i=1}^\infty' + str(var1) + '\cdot'+ str(Fraction(var2).limit_denominator(10)) +'^{i-1}$')
        plt.axhline(y = sum, color = 'g', alpha = 0.8, linestyle = '-', label = "limit")
        ax.fill_between(x, sum - sum*0.08, sum + sum*0.08, facecolor='plum',alpha=0.3)
        ax.legend(loc='lower right')
        if abs((var2)) < 1:
            ax.text(0.9,0.9,'Since chosen r, |' + str(var2) + '| < 1:\n The sequence converges to ' + str(sum)[0:4] +' for the first '+ str(np.amax(x)) +' terms', 
                    verticalalignment='top',
                    horizontalalignment='right',
                    fontsize=7,
                    bbox={'facecolor':'white', 'alpha':0.6, 'pad':10},
                    transform= ax.transAxes)
            ax.annotate('({:.2f},{:.2f})'.format(max(x),max(y)),
                        xy=(max(x),max(y)), xytext=(max(x) - .5, max(y) + .5),
                        fontsize= 7, 
                        arrowprops={"arrowstyle":"->", "color":"y"})
            plt.show()                                                                                              
        elif abs((var2)) >= 1:
               ax.text(0.3,0.1,'Since chosen r, 1 ≤ |' + str(var2) + '|:\n The sequence diverges to ' + str(sum)[0:4] +' for the first '+ str(np.amax(x)) +' terms',
                    horizontalalignment='right',
                    verticalalignment='top',
                    fontsize=7,
                    bbox={'facecolor':'white', 'alpha':0.6, 'pad':10},
                    transform= ax.transAxes)
        plt.show();
    else:
        print("This diverges to infinity. All arithmatic sequences diverge")
def main():
    user_input = getSeq()
    Determiner(*grabSeqence(user_input))
if __name__ == '__main__':
    main()
