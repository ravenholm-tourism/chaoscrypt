import numpy as np
from chaosmaps import logisticmap
import scipy.stats as sp
import matplotlib.pyplot as plt


#SEED = np.float64(.1)
#MAP_PARAM = np.float64(4)
#ITER = 65536
#BINS = 100

SEED = np.float64(.43203125)
MAP_PARAM = np.float64(3.78)
ITER = 65536
BINS = 256


def iterate ():
  s = SEED
  #y = np.zeros(ITER, dype=np.float64)
  y = np.zeros(ITER)
  for i in xrange(ITER):
      y[i] = s
      s = logisticmap(MAP_PARAM, s)

      #if i % 10 == 0: print("iteration %d value %f" % (i,s))
  return y


vals = iterate()
min = min(vals)
min_ix = np.argmin(vals)
print("min value at %d = %f" % (min_ix, min))
max = max(vals)
max_ix = np.argmax(vals)
print("max value at %d = %f" % (max_ix, max))
eps = np.float64(1)/np.float64(256)
#print eps
bin = np.arange(0,1,eps, dtype=np.float64)
#print len(bin)
binct = np.zeros(len(vals), dtype=np.float64)

#print np.where((vals >= .1953125) & (vals < .1953125 + eps))
#print len(np.where((vals >= .1953125) & (vals < .1953125 + eps))[0])
#print vals[65468]

for i,v in np.ndenumerate(bin):
    ct = len(np.where((vals >= v) & (vals < v+eps))[0])

    if i % 10 == 0: print("bin ix %d ct %d" % (i,ct))

    #ct = len(np.where((vals >= v) & (vals < v + eps)))
    binct[i] = ct

#print binct
print binct.sum()
print np.average(binct)


binct, binarr = np.histogram(vals, bins=np.arange(BINS), range=(0,1))

print binct


rbinct = binct[::-1]
binct_asc = np.sort(rbinct)
# for ix,v in np.ndenumerate(binct_asc):
#   print(ix,v)
for ix,v in np.ndenumerate(binct_asc):
  print("bin %d = %f" % (ix[0],v))
plt.hist(vals, normed=True, bins=BINS)
plt.show()
