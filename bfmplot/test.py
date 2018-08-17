def sin_test(n=8,text_position='start'):
    """Test the stuff from the modules"""

    from bfmplot import pl
    import bfmplot as bp
    import numpy as np
    #bp.set_color_cycle(bp.cccs_colors)

    #pl.figure(figsize=bp.phys_rev_column())
    pl.figure(figsize=bp.golden_ratio(5))

    x = np.linspace(1,5*np.pi,100)

    for i in range(n):
        pl.plot(x, 1-np.sin(x[::-1]/np.sqrt(i+1)), marker=bp.markers[i],mfc='w',label='$i=%d$'%i)

    bp.strip_axis(pl.gca())

    leg = pl.legend()
    bp.align_legend_right(leg)

    bp.arrow(pl.gca(), r'$i$', 
             (3, 1.8), 
             (6, 0.8), 
             text_position=text_position)


    pl.xlabel('hello')
    pl.ylabel('hello')

    bp.set_n_ticks(pl.gca(), 3, 2)

    #pl.xscale('log')

    pl.gcf().tight_layout()


if __name__ == "__main__":
    from bfmplot import pl
    from bfmplot import mpl
    sin_test(n=4,text_position='start')

    import bfmplot as bp
    bp.set_color_cycle(bp.new_colors)

    sin_test(n=4,text_position='end')
    pl.show()
