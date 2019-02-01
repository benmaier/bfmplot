import matplotlib as mpl
import matplotlib.pyplot as pl

from .cividis import *
from .sequences import *
from .tools import *

figwidth = 5 

#mpl.rcParams['font.size'] = 12
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['figure.titlesize'] = 'medium'
mpl.rcParams['axes.titlesize'] = 'medium'
mpl.rcParams['figure.figsize'] = golden_ratio(figwidth)
#mpl.rcParams['xtick.labelsize'] = 'small'
#mpl.rcParams['ytick.labelsize'] = 'small'
mpl.rcParams['xtick.labelsize'] = 'medium'
mpl.rcParams['ytick.labelsize'] = 'medium'
mpl.rcParams['lines.markersize'] = 4
mpl.rcParams['lines.linewidth'] = 1.0



# colors
mpl.rcParams['axes.prop_cycle'] = cycler(color=brewer_qualitative)
mpl.rcParams['image.cmap'] = 'cividis'
