from bfmplot import mpl
from bfmplot import pl

from cycler import cycler

mpl_default_colors = [ '#1f77b4', 
               '#ff7f0e', 
               '#2ca02c', 
               '#d62728', 
               '#9467bd', 
               '#8c564b', 
               '#e377c2', 
               '#7f7f7f', 
               '#bcbd22', 
               '#17becf',
              ]

new_colors_1 = [ '#187960', '#bd9550', '#118390', '#d34d42', '#369c8d' ]

brewer_qualitative = [  
            '#666666',
            '#1b9e77',
            '#d95f02',
            '#7570b3',
            '#e7298a',
            '#66a61e',
            '#e6ab02',
            '#a6761d',
          ]

mpl.rcParams['axes.prop_cycle'] = cycler(color=brewer_qualitative)

markers = ['s','d','o','X','v','<','^','.','>','h','p','P','*','8','H']

