from bfmplot import pl
import bfmplot as bp
import numpy as np

def sin_test(n=8,text_position='start',with_legend=True):

    pl.figure(figsize=bp.golden_ratio(5))

    x = np.linspace(0,5*np.pi,100)

    for i in range(n):
        pl.plot(x, 1-np.sin(x[::-1]/np.sqrt(i+1)), marker=bp.markers[i],mfc='w',label='$i=%d$'%i)

    bp.strip_axis(pl.gca())

    if with_legend:
        leg = pl.legend()
        bp.align_legend_right(leg)

    pl.xlabel('this is the x-label')
    pl.ylabel('this is the y-label')

    pl.gca().set_title(name)
    pl.gcf().tight_layout()


for colors,name in zip([
                bp.mpl_default_colors,
                bp.new_colors,
                bp.brewer_qualitative,
                bp.cccs_colors,                
                bp.get_cividis_colors(8),
                bp.wong,
               ],
               [
                'bfmplot.mpl_default_colors',
                'bfmplot.new_colors',
                'bfmplot.brewer_qualitative',
                'bfmplot.cccs_colors',
                'bfmplot.get_cividis_colors(8)',
                'bfmplot.wong',
               ],
               ):

    bp.set_color_cycle(colors)
    sin_test(n=8,text_position='start',with_legend=False)
    bp.set_n_ticks(pl.gca(),nx=4,ny=4)

    name = name.replace('(','_')
    name = name.replace(')','_')

    pl.gcf().savefig(name+".png",dpi=100)

pl.show()
