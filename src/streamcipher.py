import numpy as np
from scipy.stats import truncnorm
from src.chaosmaps import logisticmap
# from chaosmaps import logisticmap


def map_tokens (tokens, invl_min, invl_max):
  '''maps tokens to intervals in the order they are stored in the tokens array'''
  eps = (invl_max - invl_min)/len(tokens)
  token_map = {}

  for i,t in enumerate(tokens):
    _min, _max = invl_min + i*eps, invl_min + (i+1)*eps
    token_map[t] = (_min, _max)
  return token_map


class StreamCipher:
  charset = ()      # alphabet
  charmap = {}      # char:interval
  ciphertext = []
  plaintext = ""

  def __init__ (self, min_iter, xmit_coeff = 0, max_iter = 2**16-1):
    self.min_iter, self.max_iter, self.xmit_coeff = min_iter, max_iter, xmit_coeff
  
  def set_charset (self, charset):
    '''array of chars used for plaintext'''
    self.charset = charset
  
  def set_ctrl_param (self, r):
    '''set parameter used by function to make it chaotic'''
    self.r = np.float64(r)
  
  def set_init_val (self, x_0):
    '''set initial value to start iterating from'''
    self.x_0 = np.float64(x_0)
  
  def get_key (self):
    return {
      "x_init": self.x_0,
      "ctrl_param": self.r,
      "charmap": self.charmap
    }
  
  def gen_charmap (self, min = .2, max = .8):
    '''map chars in charset to subintervals in [.2,.8]'''
    _min = np.float64(min)
    _max = np.float64(max)
    self.charmap = map_tokens(self.charset, _min, _max)
  
  def check_xmit (self, i):
    '''
    probabilistically checks if cipher should use current iteration count as
    cipherchar or if it should keep iterating until it's in the correct interval
    again
    
    generates random number rv from normal distribution truncated to [0,1]
    and checks if rv >= class var xmit_coeff
    if so, iteration count is used as cipherchar
    '''
    l,u = 0,1
    mu,sigma = 0.0,1.0
    a,b = (l - mu)/sigma, (u-mu)/sigma  # a,b are endpoints of [0,1]
    rv = truncnorm.rvs(a,b)

    # max of 60 xmit misses (update based on invariant density of map used)
    return False if (rv < self.xmit_coeff) and (i <= 60) else True

  def gen_cipherchar (self, char, prev_x = -1):
    '''generate ciphertext character (number of iterations to get from
       previous x to a value in the interval for plaintext char'''
    x = self.x_0 if prev_x == -1 else prev_x    # -1 if first char in stream
    i = 0                                       # counts total iterations
    ivl = self.charmap[char]
    xmit = False

    # if first char, do min_iter iterations so i > min_iter
    if x == -1:
      for _ in range(self.min_iter):
        x = logisticmap(self.r, x)
        i += 1

    # keep iterating until you find an x value in the right interval
    while xmit == False:
      x = logisticmap(self.r, x)
      i += 1
      if (x >= ivl[0] and x < ivl[1]):
        xmit = self.check_xmit(i)
        # xmit = True
    
    return i, x
  
  def gen_ciphertext (self, plaintext = ''):
    i,x = 0, 0
    xvals = []
    ciphertext = []

    # if len(plaintext) != 0:  self.plaintext = plaintext

    for c in plaintext:
      #TODO: repeated chars in plaintext have 0 cipherchar
      if len(xvals) == 0:
        i, x = self.gen_cipherchar(c)
        # self.ciphertext.append(i)
        ciphertext.append(i)
        xvals.append(x)
      else:
        i, x = self.gen_cipherchar(c, xvals[-1])
        # self.ciphertext.append(i)
        ciphertext.append(i)
        xvals.append(x)

    # return self.ciphertext, xvals
    return ciphertext, xvals
      




