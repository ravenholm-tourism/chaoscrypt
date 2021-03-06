import src.streamcipher as sc
import src.plaintext as pt
# import streamcipher as sc
# import plaintext as pt
import sys
import argparse


def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument("x0", type=float, help="initial position of iterator value - should be between .2 and .8")
  parser.add_argument("b", type=float, help="control parameter for attractor - determines if behavior is chaotic or not")
  parser.add_argument("text", type=str, help="plaintext message to encrypt")
  # parser.add_argument("-d", help="use default dictionary, which is extended ASCII chars (256 chars) mapped to the interval [.2,.8]", action="store_true")
  # parser.add_argument("xmit", type=float, help="coefficient to determine probability of transmission - value in [0,1], 0 means transmission guaranteed on first try")
  args = parser.parse_args(argv)

  x0 = args.x0
  control_param = args.b
  plaintext = args.text
  lim = 65532             # ~2^16 or short int
  trans_time = 250        # first ciphertext iteration value must be > than this (lyapunov time)
  trans_coeff = 0       # let first iteration
  alphabet = [chr(_) for _ in range(256)]       # 256 char ascii

  streamcipher = sc.StreamCipher(trans_time, trans_coeff, lim)
  streamcipher.set_ctrl_param(control_param)
  streamcipher.set_init_val(x0)
  streamcipher.set_charset(alphabet)
  streamcipher.gen_charmap()
  cipher_state = streamcipher.gen_ciphertext(plaintext)
  ciphertext = cipher_state[0]
  return ", ".join([str(_) for _ in ciphertext])


if __name__ == "__main__":
  # argv = [".232323","3.8","hi"]
  # ciphertext = main(argv)
  ciphertext = main(sys.argv[1:])
  print(ciphertext)
