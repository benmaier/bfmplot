# ===================================================
# Concerning the rest of the code
# ===================================================
# 
# Copyright 2018 Benjamin F. Maier
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import numpy as np

from bfmplot import pl

import matplotlib as mpl

from matplotlib.colors import LinearSegmentedColormap

def convert_color_array_to_cdict(arr):

    cdict = { 'red' : [],
              'green' : [],
              'blue' : [],
              'alpha': [ (0.0, 1.0, 1.0), (1.0, 1.0, 1.0) ],
            }

    N = arr.shape[0]
    X = np.linspace(0,1,N)

    for x, (r,g,b) in zip(X, arr):
        cdict['red'].append( (x, r, r) )
        cdict['green'].append( (x, g, g) )
        cdict['blue'].append( (x, b, b) )

    for k in cdict.keys():
        cdict[k] = tuple(cdict[k])

    return cdict

maier = np.array([
    [79.,168.,140.], 
    [121.,121.,121.],
    [255.,52.,160.],
]) / 255.

maier_cmap = convert_color_array_to_cdict(maier)
maier_linear_segmented = LinearSegmentedColormap('maier', maier_cmap)

pl.register_cmap(cmap=maier_linear_segmented)

def get_maier_colors(N, x_start=0, x_end=1.0):
    """Get a color array of `N` entries, where the `N` entries
    are taken at equidistance from the `cividis` array between
    `n_start` and `n_end`"""



    vals = np.linspace(x_start, x_end, N)
    colors = [ maier_linear_segmented(v) for v in vals ]
    return colors

def make_default():
    """Tell matplotlib to use cividis as default colormap."""
    mpl.rcParams['image.cmap'] = 'maier'

if __name__=="__main__":
    print(get_maier_colors(12))

    x = np.arange(0, 2*np.pi, 0.01)
    y = np.arange(0, 2*np.pi, 0.01)
    X, Y = np.meshgrid(x,y)
    Z = np.cos(X) * np.sin(Y) * 20

    pl.imshow(Z,cmap='maier')
    pl.colorbar()

    pl.show()
