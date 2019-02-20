from bfmplot import pl
from bfmplot import mpl
from cycler import cycler
import numpy as np

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def strip_axis(ax,horizontal='right'):
    """Remove the right and the top axis"""
    if horizontal == 'right':
        anti_horizontal = 'left'
    else:
        anti_horizontal = 'right'
        ax.yaxis.set_label_position("right")

    ax.spines[horizontal].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.yaxis.set_ticks_position(anti_horizontal)
    ax.xaxis.set_ticks_position('bottom')

def golden_ratio(figwidth=5):
    """Return the figure size (width, height) following the golden ratio given the width figwidth (default = 5)"""

    Phi = 1.61803
    a = figwidth / Phi

    return [ figwidth, a ]

def phys_rev_column(scale=1):
    """Return the Phys. Rev. figure size (3.375, 3) scaled witth scale (default = 1)"""

    return [3.375*scale, 3.*scale]

def set_figsize(figsize):
    mpl.rcParams['figure.figsize'] = figsize


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

    if ny is not None:
        pl.locator_params(axis='y', nbins=ny)

    if nx is not None:
        pl.locator_params(axis='x', nbins=nx)

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
    #return f'{num/1000.0**m:.{precision}f}{suffixes[m]}'
    return "%.{}f{}".format(precision,suffixes[m]) % (num/1000.0**m)

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

def set_fontsize(fs):

    mpl.rcParams['font.size'] = 9

def add_curve_label(ax,
                    curve_x,
                    curve_y,
                    label,
                    label_pos_abs=None,
                    label_pos_rel=None,
                    bbox_pad=1.0,
                    bbox_facecolor='w',
                    angle=None,
                    x_offset=0.0,
                    y_offset=0.0,
                    **kwargs):
    """
    Add a label to a curve according to the curve's slope
    on the displayed figure.

    Parameters
    ----------
    ax : matplotlib.Axes
        The ax object where to put the label on. Use
        `pyplot.gca()` to get the current focal axes.
    curve_x : numpy.ndarray
        The curve's x-data.
    curve_y : numpy.ndarray
        The curve's y-data.
    label : str
        The label.
    label_pos_abs : float, default : None
        The absolute x-position at which to pose the label. 
        Must be smaller than `curve_x`'s last element.
        If None, `label_pos_rel` must be given.
    label_pos_rel : float, default : None
        The relative x-position at which to pose the label. 
        Must be 0 <= label_pos_rel < 1.
        If None, `label_pos_abs` must be given.
    bbox_pad : float, default : 1.0
        Padding of the bounding box around the label.
    bbox_facecolor : matplotlib color, default : 'w'
        Color of the bounding box around the label.
    angle : float, default : None
        Usually, the angle is calculated from the displayed
        curve's slope, but it can be adjusted manually
        with this parameter (angle in degrees).
    x_offset : float, default : 0.0
        offset in x-direction (IN AXES COORDINATES)
    y_offset : float, default : 0.0
        offset in y-direction (IN AXES COORDINATES)
    **kwargs
        Will be passed to pyplot.text.
    """

    if label_pos_abs is None and label_pos_rel is not None:

        # get xmin and xmax in display coordinates
        xmin = ax.transData.transform(np.array( [ curve_x[1],  curve_y[1]  ] ))[0]
        xmax = ax.transData.transform(np.array( [ curve_x[-1], curve_y[-1] ] ))[0]

        # compute label x-position in display coordinates according to
        # demanded relative label position
        new_display_x = xmin + label_pos_rel * (xmax - xmin) 

        # convert back to data coordinates and save absolute position    
        new_data_x = ax.transData.inverted().transform(np.array([new_display_x,1.0]))
        label_pos_abs = new_data_x[0]

    elif label_pos_abs is None and label_pos_rel is None:
        raise ValueError('Please provide either `label_pos_abs` or `label_pos_rel`.')
    elif label_pos_abs is not None and label_pos_rel is not None:
        raise ValueError('Please provide either `label_pos_abs` or `label_pos_rel`, not both.')

    # find ndx in data for demanded label position
    ndx = np.where(curve_x < label_pos_abs)[0][-1]

    # convert data at this point to display coordinates
    x0, y0 = ax.transData.transform( np.array( [ curve_x[ndx], curve_y[ndx] ] ))
    x1, y1 = ax.transData.transform( np.array( [ curve_x[ndx+1], curve_y[ndx+1] ] ))

    # compute slope and angle at this point in display coordinates
    dx = x1 - x0
    dy = y1 - y0

    if angle is None:
        angle = np.arctan2(dy,dx) / np.pi * 180

    # convert back to data coordinates
    x0 = label_pos_abs
    y0 = np.interp(x0, curve_x, curve_y)

    # convert to absolute coordinates
    x0, y0 = ax.transData.transform( np.array( [ x0, y0 ] ))
    # convert to Axes coordinates
    x0, y0 = ax.transAxes.inverted().transform( np.array( [ x0, y0 ] ))

    # add the offset in axes coordinates
    x0 += x_offset
    y0 += y_offset

    x0, y0 = ax.transAxes.transform( np.array( [ x0, y0 ] ))
    x0, y0 = ax.transData.inverted().transform( np.array( [ x0, y0 ] ))

    # define bounding box for label
    bbox = dict(facecolor=bbox_facecolor, alpha=1, edgecolor='none', pad=bbox_pad)

    if not ('ha' in kwargs or 'horizontalalignment' in kwargs):
        kwargs['ha'] = 'center'

    if not ('va' in kwargs or 'verticalalignment' in kwargs):
        kwargs['va'] = 'center'

    # add label
    ax.text(x0, 
            y0, 
            label, 
            rotation=angle, 
            rotation_mode='anchor',
            bbox=bbox,
            transform=ax.transData,
            **kwargs
            )

def get_inset_axes(ax,width="40%", height="18%",loc='best'):
    """Add an inset axes to the axes `ax` and return it."""

    inset = inset_axes(ax,
                    width=width, # width = 30% of parent_bbox
                    height=height, # height : 1 inch
                    loc=loc)

    return inset


if __name__ == "__main__":


    import numpy as np
    import bfmplot as bp
    fig, ax = pl.subplots(1,1)

    x = np.linspace(1,10,100)
    mus = np.linspace(1,4,4)

    for mu in mus:
        y = x**mu
        pl.plot(x,y,c=bp.brewer_qualitative[0])

    #pl.xscale('log')
    bp.strip_axis(ax,horizontal='left')
    pl.yscale('log')
    ax.set_xlabel('x')
    ax.set_ylabel('y')


    pl.gcf().tight_layout()
    pl.xlim([1,10])

    for mu in mus:
        label = r'$\mu={:d}$'.format(int(mu))
        y = x**mu
        add_curve_label(ax,x,y,label,label_pos_rel = 0.5 + mu/50)


    print(human_format(112345,precision=2))


        
    pl.show()

