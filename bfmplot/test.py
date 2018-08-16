def sin_test(n=8):
    """Test the stuff from the modules"""

    from bfmplot import pl
    import bfmplot as bp
    import numpy as np
    #bp.set_color_cycle(bp.cccs_colors)

    #pl.figure(figsize=bp.phys_rev_column())
    pl.figure(figsize=bp.golden_ratio(5))

    x = np.linspace(0,5*np.pi,100)

    for i in range(n):
        pl.plot(x, 1-np.sin(x[::-1]/np.sqrt(i+1)), marker=bp.markers[i],mfc='w',label='$i=%d$'%i)

    bp.strip_axis(pl.gca())

    leg = pl.legend()
    bp.align_legend_right(leg)


    pl.xlabel('hello')
    pl.ylabel('hello')

    pl.gcf().tight_layout()

    pl.show()

if __name__ == "__main__":
    sin_test(n=4)
