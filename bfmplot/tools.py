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
          rad = 0.3,
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
    rad : float (default : 0.3)
        Curvature on the arrow. Can be negative
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
        rad *= -1

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
                                  connectionstyle = "arc3,rad={0}".format(rad),
                                  facecolor = fc,
                                  edgecolor = ec,
                                  **arrow_kwargs
                                 ),
                **text_kwargs
                )

def stupid_strip_ticks(ax):
    """Don't use this."""

    X = ax.get_xticks(), ax.get_xticklabels()
    Y = ax.get_yticks(), ax.get_yticklabels()

    for i, (loc, lab) in enumerate([ X, Y ]):
        
        indices = [ 0, -1 ]

        new_loc = []
        new_lab = []

        for ndx in indices:
            new_loc.append(loc[ndx])
            new_lab.append(lab[ndx])

        if i == 0:
            ax.set_xticks(new_loc)
            #ax.set_xticklabels(new_lab)
        else:
            ax.set_yticks(new_loc)
            #ax.set_yticklabels(new_lab)
        

def set_n_ticks(ax=None,nx=3,ny=2):
    """Set the number of major ticks for each axis"""
    if ax is None:
        ax = pl.gca()
    old_ax = pl.gca()
    pl.sca(ax)
    pl.locator_params(axis='y', nbins=nx)
    pl.locator_params(axis='x', nbins=ny)
    pl.sca(old_ax)

def human_format(num, precision=2):
    """Return numbers rounded to given precision and with sensuous suffixes.

    Parameters
    ==========
    num : float
        The number to humanify.
    precision : int, default : 2
        Number of decimal places.

    Return
    ======
    s : String
        Human readable string.
    """
    suffixes=['', 'k', 'M', 'G', 'T', 'P']
    m = sum([abs(num/1000.0**x) >= 1 for x in range(1, len(suffixes))])
    return f'{num/1000.0**m:.{precision}f}{suffixes[m]}'

def humanify_xticks(ax,precision=2):
    """Make the xticks human readable.

    Parameters
    ==========
    ax : matplotlib.Axes
        The instance to modify.
    precision : int, default: 2
        Number of decimal places after contraction.
    """

    xt = ax.get_xticks()
    ax.set_xticklabels([human_format(x,precision) for x in xt])

def humanify_yticks(ax,precision=2):
    """Make the xticks human readable.

    Parameters
    ==========
    ax : matplotlib.Axes
        The instance to modify.
    precision : int, default: 2
        Number of decimal places after contraction.
    """

    yt = ax.get_yticks()
    ax.set_yticklabels([human_format(y,precision) for y in yt])

def humanify_ticks(ax,precision=2,):
    """Make the ticks human readable.

    Parameters
    ==========
    ax : matplotlib.Axes
        The instance to modify.
    precision : int, default: 2
        Number of decimal places after contraction.
    """

    humanify_xticks(ax,precision)
    humanify_yticks(ax,precision)
