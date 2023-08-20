import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
from fractions import Fraction
import numpy as np

def open_geometric_window():
    label1 = tk.Label(win, text="Enter a_n:")
    label1.pack()
    entry1 = tk.Entry(win)
    entry1.pack()
    label2 = tk.Label(win, text="Enter common ratio:")
    label2.pack()
    entry2 = tk.Entry(win)
    entry2.pack()

    def submit():
        var1 = float(entry1.get())
        var2 = float(entry2.get())
        fig, ax, x = gen_plot(var1, var2)
        clear_window()
        canvas = show_plot(fig)
        restart_button = tk.Button(win, text="Restart", command=main_menu)
        restart_button.pack(pady=10)
        canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    submit_button = tk.Button(win, text="Submit", command=submit)
    submit_button.pack()

def clear_window():
    for widget in win.winfo_children():
        widget.destroy()

def gen_plot(var1, var2):
    fig, ax = plt.subplots()
    x = list(range(1, 30))
    y = [sum(math.pow(var1 * var2, j - 1) for j in range(1, i + 1)) for i in x]
    s = y[-1] 
    ax.axis([0, 30, 0, max(y) + 1])
    ax.scatter(x, y, s=1.8, color="red", label="a_n sequence")
    title = '$\sum_{i=1}^\infty' + str(var1) + '\cdot' + str(Fraction(var2).limit_denominator(10)) +'^{i-1}$'
    plt.title(title, fontsize=7)
    plot_limit_line(ax, s)
    plot_fill_between(ax, s, x)
    annotate_info(ax, var2, s, max(x), max(y), x)
    ax.legend(loc='lower right')
    return fig, ax, x

def plot_limit_line(ax, s):
    ax.axhline(y=s, color='g', alpha=0.8, linestyle='-', label="limit")

def plot_fill_between(ax, s, x):
    ax.fill_between(x, s - s * 0.08, s + s * 0.08, facecolor='plum', alpha=0.3)

def annotate_info(ax, var2, s, max_x, max_y, x):
    if abs(var2) < 1:
        annotation_text = 'Since chosen r, |{}| < 1:\n The sequence converges to {:.4f} for the first {} terms'.format(var2, s, np.amax(x))
        text_position = (max_x - 0.5, max_y + 0.5)
    elif abs(var2) >= 1:
        annotation_text = 'Since chosen r, 1 ≤ |{}|:\n The sequence diverges to {:.4f} for the first {} terms'.format(var2, s, np.amax(x))
        text_position = (max_x - 0.5, max_y + 0.5)

    ax.annotate(
        annotation_text,
        xy=(max_x, max_y),
        xytext=text_position,
        fontsize=7,
        arrowprops={"arrowstyle": "->", "color": "y"},
        bbox={'facecolor': 'white', 'alpha': 0.6, 'pad': 10},
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes
    )

def show_plot(fig):
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    return canvas.get_tk_widget()

def main_menu():
    global win
    win = tk.Tk()
    win.config(bg="#f0f8ff")
    win.geometry("800x400")
    win.minsize(800, 400)
    win.maxsize(800, 400)
    win.title("Sequence Divergence/Convergence Determiner")
    #image_path = os.path.join(os.path.dirname(__file__), 'fig')
    #image = Image.open(image_path)
    #img = ImageTk.PhotoImage(image.resize((600, 180)))
    #label = tk.Label(win, image=img)
    #label.image = img
    #label.pack()
    title_label = tk.Label(win, text="Hello, welcome to the Sequence Divergence/Convergence Determiner", bg="#f0f9fa")
    title_label.pack()
    author_label = tk.Label(win, text="_______________________________________________________@Author Ana-r", bg="#f0f9fa")
    author_label.pack()
    option_label = tk.Label(win, text="What type of sequence will you be looking at today?", bg="#f0f9fa")
    option_label.pack()
    geometric_button = tk.Button(win, text="Geometric", command=open_geometric_window)
    geometric_button.pack(pady=10)
    win.mainloop()

if __name__ == "__main__":
    main_menu()
