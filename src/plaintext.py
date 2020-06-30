import numpy as np
import math
# import string
from chaosmaps import logisticmap

class PlainText:
  ivl = [.2, .8]

  def __init__ (self, charset = (), msg = ""):
    self.set_message (charset, msg)
  
  def __init__ (self, keystream = None, key = None, charset = ()):
    ''' private key is initial x val, control parameter, and charset mapping '''
    self.keystream = keystream
    self.key = key
    self.charset = charset
  
  def set_message (self, charset = (), msg = ""):
    self.charset = charset
    self.msg = msg
  
  def decrypt_ciphertext (self):
    x = self.key["x_init"]
    r = self.key["ctrl_param"]
    rev_charmap = dict(map(reversed, self.key["charmap"].items()))
    rev_charmap = sorted(rev_charmap.items())
    eps = (self.ivl[1] - self.ivl[0]) / np.float64(len(self.charset))
    # print eps
    self.msg = ""

    for c in self.keystream.ciphertext:
      for i in range(c):
        x = logisticmap(r, x)
      # print x
      for i in range(len(rev_charmap)):
        if rev_charmap[i][0][0] <= x and rev_charmap[i][0][1] > x:
          self.msg += rev_charmap[i+1][1]
          # print self.msg
          break

    return self.msg