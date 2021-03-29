from ..maps.onedim import logisticmap

class PlainText:
  ivl = [.2, .8]
  
  def __init__ (self, key = {}):
    '''
    key is dict with initial x val, control parameter,
    and charset mapping (dict of chars:intervals)
    '''
    self.key = key
    self.charset = [*key.keys()]
  
  def decrypt_ciphertext (self, ciphertext):
    '''
    ciphertext is a list of integers indicating how many times to iterate to 
    get the interval corresponding to the plaintext char
    '''
    x = self.key["x_init"]
    r = self.key["ctrl_param"]
    rev_charmap = dict(map(reversed, self.key["charmap"].items()))
    rev_charmap = sorted(rev_charmap.items())
    self.msg = ""

    for c in ciphertext:
      for i in range(c):
        x = logisticmap(r, x)
      print(x)
      for i in rev_charmap:
        # check that x is in interval
        if i[0][0] <= x and i[0][1] > x:
          self.msg += i[1]   # add char mapped to interval to msg
          break

    return self.msg