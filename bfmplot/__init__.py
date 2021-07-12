import matplotlib as mpl
import matplotlib.pyplot as pl

__version__ = "0.0.10"

__author__ = "Benjamin F. Maier"
__copyright__ = "Copyright 2020-2021, " + __author__
__credits__ = [__author__]
__license__ = "MIT"
__maintainer__ = __author__
__email__ = "contact@benmaier.org"
__status__ = "Development"


#from .cividis import *
from .sequences import *
from .tools import *

figwidth = 5

#mpl.rcParams['font.size'] = 12
#mpl.rcParams['legend.fontsize'] = 'medium'
#mpl.rcParams['figure.titlesize'] = 'medium'
#mpl.rcParams['axes.titlesize'] = 'medium'
mpl.rcParams['figure.figsize'] = golden_ratio(figwidth)
##mpl.rcParams['xtick.labelsize'] = 'small'
##mpl.rcParams['ytick.labelsize'] = 'small'
#mpl.rcParams['xtick.labelsize'] = 'medium'
#mpl.rcParams['ytick.labelsize'] = 'medium'
#mpl.rcParams['lines.markersize'] = 4
#mpl.rcParams['lines.linewidth'] = 1.0



# colors
#mpl.rcParams['axes.prop_cycle'] = cycler(color=brewer_qualitative)
mpl.rcParams['axes.prop_cycle'] = cycler(color=epipack)
mpl.rcParams['image.cmap'] = 'cividis'
