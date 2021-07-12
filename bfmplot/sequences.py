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


epipack = [ '#'+s for s in ['365663','ee6f51','2a9d8f','83e377','e9c46a','646464','ff9de4','52b7dc','b75b9e','ff9de4','47829a','ff9f92','45dbc8','a4ffbb','ffee9d','a1a1a1','b0dff0','ffcaf0',]]

wong = [
            '#333333', # black
            '#D55E00', # red (orange-ish)
            '#E69F00', # orange
            '#56B4E9', # light blue
            '#0072B2', # blue
            '#F0E442', # yellow
            '#CC79A7', # red (wine-ish)
            '#009E73', # green
        ]

wong_orig = [
            '#333333', # black (original is #000000, but it's too harsh on my eye)
            '#E69F00', # orange
            '#56B4E9', # light blue
            '#009E73', # green
            '#F0E442', # yellow
            '#0072B2', # blue
            '#D55E00', # red (orange-ish)
            '#CC79A7', # red (wine-ish)
        ]

wong_order = [
            '#333333', # black (original is #000000, but it's too harsh on my eye)
            '#E69F00', # orange
            '#009E73', # green
            '#D55E00', # red (orange-ish)
            '#56B4E9', # light blue
            '#F0E442', # yellow
            '#0072B2', # blue
            '#CC79A7', # red (wine-ish)
        ]


colors = epipack


class simple_cycler(list):
    """Simplest implementation of a list with periodic boundary conditions"""
    def __init__(self,items):
        self.items = items

    def __getitem__(self,i):
        return self.items[i%len(self.items)]


#markers = simple_cycler(['s','d','o','v','*','^','.','>','h','p','P','<','8','H','X'])
markers = simple_cycler(['s','d','o','v','*','^','>','h','p','P','<','8','H','X'])


if __name__ == "__main__":

    import numpy as np

    seq = wong_order

    ncol = int(np.ceil(np.sqrt(len(seq))))
    fig, ax = pl.subplots(ncol,ncol,figsize=(8,8))
    ax = ax.flatten()

    x = np.linspace(0,2*np.pi,1000)

    for i in range(len(seq)):
        for j in range(i+1):
            ax[i].plot(x,np.sin(x*np.sqrt(j+1)),c=seq[j],lw=3)

    pl.show()

