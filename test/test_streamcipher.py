from src import streamcipher as sc
import pytest

# @pytest.mark.skip()
def test_ciphertext():
  alphabet = [chr(_) for _ in range(256)]       # 256 char ascii
  x_0 = 232323e-6         # initial starting point in interval
  lim = 65532             # ~2^16 or short int
  trans_time = 250        # first ciphertext iteration value must be > than this (lyapunov time)
  trans_coeff = 0       # let first iteration in char's interval be cipherchar
  # trans_coeff = .2        # for character i, transmit if random number in [0,1] >= .2 (~76% chance each try will succeed)
  control_param = 3.8     # parameter for logistic map - alternate chaotic values: 3.56995, 3.82843 (most values between 3.57 and 4 work)
  plaintext = 'hi'

  streamcipher = sc.StreamCipher(trans_time, trans_coeff, lim)
  streamcipher.set_charset(alphabet)
  streamcipher.set_ctrl_param(control_param)
  streamcipher.set_init_val(x_0)
  streamcipher.gen_charmap()

  # print(streamcipher.get_key())

  cipher_state = streamcipher.gen_ciphertext(plaintext)
  # print(cipher_state)
  ciphertext = cipher_state[0]
  #   print(ciphertext)
  assert ciphertext == [2077,5]


def test_ciphertext_xmit():
  alphabet = [chr(_) for _ in range(256)]       # 256 char ascii
  x_0 = 232323e-6         # initial starting point in interval
  lim = 65532             # ~2^16 or short int
  trans_time = 250        # first ciphertext iteration value must be > than this (lyapunov time)
  trans_coeff2 = .5        # for character i, transmit if random number in [0,1] >= .2 (~76% chance each try will succeed)
  control_param = 3.8     # parameter for logistic map - alternate chaotic values: 3.56995, 3.82843 (most values between 3.57 and 4 work)
  plaintext = 'hi'

  streamcipher = sc.StreamCipher(trans_time, trans_coeff2, lim)
  streamcipher.set_charset(alphabet)
  streamcipher.set_ctrl_param(control_param)
  streamcipher.set_init_val(x_0)
  streamcipher.gen_charmap()

  # print(streamcipher.get_key())

  cipher_state2 = streamcipher.gen_ciphertext(plaintext)
  # print(cipher_state)
  ciphertext2 = cipher_state2[0]
  #   print(ciphertext)
  assert ciphertext2[0] >= 2077 and ciphertext2[1] >= 5


