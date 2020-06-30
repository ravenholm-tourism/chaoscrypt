import numpy as np
from chaosmaps import logisticmap
x = np.float64(.232323)
r = np.float64(3.8)

for i in xrange(1713):
    x = logisticmap(r,x)
print x
print np.float64("{0:.14f}".format(x))