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

def arrow(ax,
          text,
          xy_start,
          xy_end,
          text_position = 'end',
          coords = 'data',
          angleA = 10,
          angleB = -80,
          linewidth=None,
          lw=None,
          color=None,
          c=None,
          facecolor=None,
          fc=None,
          edgecolor=None,
          ec=None,
          text_kwargs={},
          arrow_kwargs={},
          ):
    """Draw a curved arrow on a plot

    Parameters
    ----------
    ax : matplotlib.axis
        Axis to draw on.
    test : string
        Text to put on one end of the arrow.
    xy_start : tuple of float
        (x,y)-coordinates where the arrow starts.
    xy_end : tuple of float
        (x,y)-coordinates where the arrow end.
    text_position : str (default : 'end')
        Where to put the text, either the 'end' of the
        arrow or the 'start' of the arrow.
    coords : str (default : 'data')
        Coordinate system of the provided coordinates, possibilities:
        'data' : coordinates of the data in plots
        'axes fraction' : fraction of the axis in [0,1]
        'figure fraction' : fraction of the figure in [0,1]
        Other styles:
        https://matplotlib.org/api/_as_gen/matplotlib.pyplot.annotate.html
    angleA : float (default : 10)
        Angle on the beginning of the arrow in degrees.
    angleB : float (default : 10)
        Angle on the end of the arrow in degrees.
    linewidth or lw : float (default : 1.0)
        Width of the arrow in points.
    color or c : any matplotlib color (default : '#4a4e4d')
        color of the whole arrow (overridden by `facecolor`
        and `edgecolor`)
    facecolor or fc : facecolor of the arrow (default : '#4a4e4d')
        facecolor of the arrow
    edgecolor or ec : edgecolor of the arrow (default : '#4a4e4d')
        edgecolor of the arrow
    text_kwargs : dict (default : {})
    arrow_kwargs : dict (default : {})
    """
    
    arrowstyle = '<|-'

    if text_position == 'start':
        arrowstyle = '-|>'
        xy_start, xy_end = xy_end, xy_start
        angleA, angleB = angleB, angleA

    if color is not None:
        c = color

    if c is None:
        c = "#4a4e4d"  

    if facecolor is not None:
        fc = facecolor

    if fc is None:
        fc = c

    if edgecolor is not None:
        ec = edgecolor

    if ec is None:
        ec = c

    if linewidth is not None:
        lw = linewidth

    if lw is None:
        lw = 1.0

    ax.annotate(text,
                xy = xy_start, 
                xycoords = coords,
                xytext = xy_end, 
                textcoords = coords,
                arrowprops = dict(arrowstyle = arrowstyle,
                                  connectionstyle = "angle3,angleA={0},angleB={1}".format(angleA, angleB),
                                  facecolor = fc,
                                  edgecolor = ec,
                                  **arrow_kwargs
                                 ),
                **text_kwargs
                )
