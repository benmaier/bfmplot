import matplotlib as mpl
import matplotlib.pyplot as pl

from .sequences import *
from .tools import *

figwidth = 5 

mpl.rcParams['font.size'] = 9
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['figure.titlesize'] = 'medium'
mpl.rcParams['axes.titlesize'] = 'medium'
mpl.rcParams['figure.figsize'] = golden_ratio(figwidth)
mpl.rcParams['lines.markersize'] = 4
