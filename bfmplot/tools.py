from bfmplot import pl
from bfmplot import mpl
from cycler import cycler

def strip_axis(ax):
    """Remove the right and the top axis"""
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

def golden_ratio(figwidth=5):
    """Return the figure size (width, height) following the golden ratio given the width figwidth (default = 5)"""

    Phi = 1.61803
    a = figwidth / Phi

    return [ figwidth, a ]

def phys_rev_column(scale=1):
    """Return the Phys. Rev. figure size (3.375, 3) scaled witth scale (default = 1)"""

    return [3.375*scale, 3.*scale]


def align_legend_right(legend):
    """Align the items of the legend to the right side."""

    vp = legend._legend_box._children[-1]._children[0]

    for c in vp._children:
        c._children.reverse()

    vp.align = "right"

def set_color_cycle(colors):
    """Set the matplotlib color cycle with the given colors"""
    mpl.rcParams['axes.prop_cycle'] = cycler(color=colors)

def arrow(ax,text):
    ax[iN].annotate(r'$\beta$',
    xy=(0.3, 1e-3), xycoords='data',
    xytext=(1, 1e-7), textcoords='data',
    arrowprops=dict(arrowstyle="->",
    connectionstyle="angle3,angleA=10,angleB=-80"))
