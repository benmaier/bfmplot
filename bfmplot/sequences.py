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

new_colors = [ '#187960', '#bd9550', '#118390', '#d34d42', '#369c8d' ]

brewer_qualitative = [  
            '#666666',
            '#1b9e77',
            '#e7298a',
            '#7570b3',
            '#d95f02',
            '#66a61e',
            '#e6ab02',
            '#a6761d',
          ]

cccs_colors=[   
                "#4a4e4d",  
                "#0e3ca7",  
                "#fe8a71",
                "#3da4ab", 
                #"#f6cd61", 
                '#e6ab02',
            ]

colors = brewer_qualitative

epipack = [ '#'+s for s in ['365663','ee6f51','2a9d8f','83e377','e9c46a','646464','ff9de4','52b7dc','b75b9e','ff9de4','47829a','ff9f92','45dbc8','a4ffbb','ffee9d','a1a1a1','b0dff0','ffcaf0',]]

colors = epipack

class simple_cycler(list):
    """Simplest implementation of a list with periodic boundary conditions"""
    def __init__(self,items):
        self.items = items

    def __getitem__(self,i):
        return self.items[i%len(self.items)]

    def __getitem__(self,i):
        return self.items[i%len(self.items)]


#markers = simple_cycler(['s','d','o','v','*','^','.','>','h','p','P','<','8','H','X'])
markers = simple_cycler(['s','d','o','v','*','^','>','h','p','P','<','8','H','X'])

