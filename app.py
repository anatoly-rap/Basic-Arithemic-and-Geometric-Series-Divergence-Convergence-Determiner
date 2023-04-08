import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import ttk
import matplotlib.pyplot as plt;
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math;
from fractions import Fraction
import numpy as np;

def open_geometric_window():
    win = tk.Toplevel()
    win.geometry("400x200")
    win.title("Geometric Sequence")
    label1 = tk.Label(win, text="Enter a_n: ")
    label1.pack()
    entry1 = tk.Entry(win)
    entry1.pack()
    label2 = tk.Label(win, text="Enter common ratio: ")
    label2.pack()
    entry2 = tk.Entry(win)
    entry2.pack()
    def submit():
        var1 = float(entry1.get())
        var2 = float(entry2.get())
        fig,ax = gen_plot(var1, var2);
        fig_canvas = FigureCanvasTkAgg(fig, master=win)
        fig_canvas.draw()
        fig_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        win.geometry(f"{fig.get_figwidth()*80:.0f}x{fig.get_figheight()*80:.0f}")
    submit_button = tk.Button(win, text="Submit", command=submit)
    submit_button.pack()
    
def gen_plot(var1, var2):
    fig, ax = plt.subplots();
    s = 0
    for i in range(1, 30):
        s += math.pow((var1*var2), i-1)
        x = [i for i in range(1, 30)]
        y = [sum(math.pow(var1 * var2, j-1) for j in range(1, i+1)) for i in range(1, 30)]
    ax.axis([0, 30, 0, max(y)+ 1])
    ax.scatter(x,y, s = 1.8, color = "red", label = "a_n sequence")
    plt.title('$\sum_{i=1}^\infty' + str(var1) + '\cdot'+ str(Fraction(var2).limit_denominator(10)) +'^{i-1}$', fontsize=7)
    plt.axhline(y = s, color = 'g', alpha = 0.8, linestyle = '-', label = "limit")
    ax.fill_between(x, s - s*0.08, s + s*0.08, facecolor='plum',alpha=0.3)
    ax.legend(loc='lower right')
    if abs((var2)) < 1:
        ax.text(0.9,0.9,'Since chosen r, |' + str(var2) + '| < 1:\n The sequence converges to ' + str(s)[0:4] +' for the first '+ str(np.amax(x)) +' terms', 
            verticalalignment='top',
            horizontalalignment='right',
            fontsize=7,
            bbox={'facecolor':'white', 'alpha':0.6, 'pad':10},
            transform= ax.transAxes)
        ax.annotate('({:.2f},{:.2f})'.format(max(x),max(y)),
            xy=(max(x),max(y)), xytext=(max(x) - .5, max(y) + .5),
            fontsize= 7, 
            arrowprops={"arrowstyle":"->", "color":"y"})                                                                                           
    elif abs((var2)) >= 1:
        ax.text(0.3,0.1,'Since chosen r, 1 ≤ |' + str(var2) + '|:\n The sequence diverges to ' + str(s)[0:4] +' for the first '+ str(np.amax(x)) +' terms',
            horizontalalignment='right',
            verticalalignment='top',
            fontsize=7,
            bbox={'facecolor':'white', 'alpha':0.6, 'pad':10},
            transform= ax.transAxes)
    return fig, ax;

def main_menu():
    win = tk.Tk()
    win.config(bg="#f0f8ff")
    win.geometry("800x400")
    win.minsize(800,400)
    win.maxsize(800,400)
    win.title("Sequence Divergence/Convergence Determiner")
    title_label = tk.Label(win, text="Hello, welcome to the sequence Divergence/Convergence Determiner", bg="#f0f9fa")
    title_label.pack()
    author_label = tk.Label(win, text="_______________________________________________________@Author Ana-r", bg="#f0f9fa")
    author_label.pack()
    base_folder = os.path.dirname(__file__);
    image_path = os.path.join(base_folder, 'fig');
    image = Image.open(image_path);
    img = ImageTk.PhotoImage(image.resize((600, 180))) 
    label = tk.Label(win, image=img);
    label.image = img;
    label.pack();
    option_label = tk.Label(win, text="What type of sequence will you be looking at today?",bg="#f0f9fa")
    option_label.pack()
    geometric_button = tk.Button(win, text="Geometric", command=open_geometric_window)
    geometric_button.pack(pady=10)
    win.mainloop()

if __name__ == "__main__":
    main_menu()
