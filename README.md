# bfmplot

A collection of snippets for plots to make my life easier. The name is a nod to the great [Burkhard Bunk](http://people.physik.hu-berlin.de/~bunk/bbplot/).

## Install

Clone this repository

    git clone git@github.com:benmaier/bfmplot.git

Install as development version (such that you don't have to reinstall after updating the repository)

    pip install -e ./bfmplot --no-binary :all:
    cd bfmplot; make

Alternatively, install normally

    pip install ./bfmplot
    cd bfmplot; make install

## Examples

### First Example

```python
from bfmplot import pl
import bfmplot as bp
import numpy as np

def sin_test(n=8,text_position='start'):

    # new figure in the golden ratio
    pl.figure(figsize=bp.golden_ratio(5))

    x = np.linspace(0,5*np.pi,100)

    # plot several functions with different markers
    for i in range(n):
        pl.plot(x, 1-np.sin(x[::-1]/np.sqrt(i+1)), marker=bp.markers[i],mfc='w',label='$i=%d$'%i)

    # remove right and top axis
    bp.strip_axis(pl.gca())

    # order legend items to align to the right
    leg = pl.legend()
    bp.align_legend_right(leg)

    # draw an arrow
    bp.arrow(pl.gca(), r'$i$', (6, 0.8), (3, 1.8), text_position=text_position)

    pl.xlabel('this is the x-label')
    pl.ylabel('this is the y-label')

    pl.gcf().tight_layout()


sin_test(n=4,text_position='start')

pl.show()
```

![one](https://github.com/benmaier/bfmplot/raw/master/sandbox/one.png "first")

### Color cycle scans


```python
for colors,name in zip([
                bp.mpl_default_colors,
                bp.new_colors,
                bp.brewer_qualitative,
                bp.cccs_colors,                
               ],
               [
                'bfmplot.mpl_default_colors',
                'bfmplot.new_colors',
                'bfmplot.brewer_qualitative',
                'bfmplot.cccs_colors',
               ],
               ):

    bp.set_color_cycle(colors)
    sin_test(n=8,text_position='start')
```

![](https://github.com/benmaier/bfmplot/raw/master/sandbox/bfmplot.mpl_default_colors.png "")
![](https://github.com/benmaier/bfmplot/raw/master/sandbox/bfmplot.new_colors.png "")
![](https://github.com/benmaier/bfmplot/raw/master/sandbox/bfmplot.brewer_qualitative.png "")
![](https://github.com/benmaier/bfmplot/raw/master/sandbox/bfmplot.cccs_colors.png "")
![](https://github.com/benmaier/bfmplot/raw/master/sandbox/bfmplot.get_cividis_colors_8_.png "")
