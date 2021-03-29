import numpy as np
import functools

def logisticmap (r, x):
  ''' assumes r,x are type np.float64
      truncate to 14 digits
  '''
  r = np.float64(r)
  x = np.float64(x)
  x = r * x * (1-x)
  return x

def chaotic_map (fn, r):
  '''
    wrapper for 1d chaotic maps
  '''
  # TODO add additional chaotic maps after testing
  return functools.partial(fn,r)