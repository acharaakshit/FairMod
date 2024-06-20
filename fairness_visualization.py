import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.pyplot import cm
from typing import Tuple

def plot(ax, x1, y1, x2, y2, colors: Tuple, arrow_pos: Tuple or float = (0.5,), scale: float = 15):
    ax.scatter(x1, y1, color=colors[0], marker='s', s=100, zorder=2, clip_on=False, edgecolors="black")
    ax.scatter(x2, y2, color=colors[2], marker='^', s=100, zorder=4, clip_on=False,
    edgecolors="black")
    ax.plot([x1, x2], [y1, y2], color=colors[1], linestyle='--', linewidth=1.5, zorder=3, alpha=0.3, dashes=(10, 2))
    return

def plot_specific(ax, d1, d2, colors):
    x_max = -1
    y_max = -1
    for (x1,y1), (x2,y2), color in zip(d1,d2, colors):
        # x1, y1, x2, y2 = 0.001894, 0.046022, 0.096978, 0.445169
        plot(ax, x1, y1, x2, y2, colors=color) #arrow_pos=(0.4, 0.75)
        if x1 > x_max:
            x_max = x1
        if y1 > y_max:
            y_max = y1
      
    ax.imshow([[.02, .05], [.08, .1]], cmap=cm.Reds, interpolation='bicubic', extent=(0, 0.3,
    0.95, 0),
    aspect="auto", zorder=0, alpha=0.5)
    ax.set_ylabel("|DP|", fontsize=13)
    ax.set_xlabel("|CSP|", fontsize=13)
    return