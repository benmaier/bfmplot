def sin_test(n=8):
    from bfmplot import pl
    import bfmplot as bp
    import numpy as np

    x = np.linspace(0,5*np.pi,100)

    for i in range(1,n+1):
        pl.plot(x, np.sin(x/np.sqrt(i)), marker=bp.markers[i],mfc='w')

    bp.strip_axis(pl.gca())

    pl.show()

if __name__ == "__main__":
    sin_test(n=3)
