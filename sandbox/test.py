from bfmplot import pl
import bfmplot as bp
import numpy as np

def sin_test(n=8,text_position='start'):

    pl.figure(figsize=bp.golden_ratio(5))

    x = np.linspace(0,5*np.pi,100)

    for i in range(n):
        pl.plot(x, 1-np.sin(x[::-1]/np.sqrt(i+1)), marker=bp.markers[i],mfc='w',label='$i=%d$'%i)

    bp.strip_axis(pl.gca())

    leg = pl.legend()
    bp.align_legend_right(leg)

    bp.arrow(pl.gca(), r'$i$', (14, 0.8), (10, 0.15), text_position=text_position, rad=0.3)    

    pl.xlabel('this is the x-label')
    pl.ylabel('this is the y-label')

    pl.gcf().tight_layout()


sin_test(n=4,text_position='start')
pl.savefig('one.png',dpi=150)

bp.set_color_cycle(bp.new_colors)

sin_test(n=4,text_position='end')
pl.savefig('two.png',dpi=150)

pl.show()
