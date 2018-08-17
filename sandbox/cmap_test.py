from bfmplot import pl
import numpy as np

x = np.arange(0, 2*np.pi, 0.01)
y = np.arange(0, 2*np.pi, 0.01)
X, Y = np.meshgrid(x,y)
Z = np.cos(X) * np.sin(Y) * 20

pl.imshow(Z)
pl.colorbar()

pl.show()
