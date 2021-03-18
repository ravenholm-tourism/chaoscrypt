import random
# import secrets
import string

class KeyGenerator:
  x_init = None
  ctrl_param = 0e0
  charmap = []

  def __init__(self, key={}):
    if not 'x_init' in key:
      # generate random starting value
      secure_random = random.SystemRandom()
      self.x_init = secure_random.uniform(.2, .8)
    
    if not 'ctrl_param' in key:
      # use known chaotic value
      # insecure but unsure how to generate these in a way that guarantees function is chaotic
      self.ctrl_param = 3.8
    
    if not 'charmap' in key:
      # default to ascii 256 and shuffle them
      alphabet = [chr(_) for _ in range(256)]
      self.charmap = random.SystemRandom().sample(alphabet, len(alphabet))
  
  def get_key(self):
    return {'x_init':self.x_init, 'ctrl_param':self.ctrl_param, 'charmap':self.charmap}
      