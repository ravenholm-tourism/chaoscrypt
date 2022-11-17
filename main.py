from chaoscrypt.cipher.streamcipher import map_tokens, StreamCipher
from chaoscrypt.cipher.plaintext import PlainText
import sys
import argparse


def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument("-x0", type=float, help="initial position of iterator value - should be between .2 and .8")
  parser.add_argument("-b", type=float, help="control parameter for dynamical system - determines if behavior is chaotic or not")
  parser.add_argument("-text", type=str, help="plaintext message to encrypt")
  parser.add_argument("--xmit", type=float, help="coefficient to determine probability of transmission. Value in [0,1]; 0 means transmission guaranteed on first try")
  # parser.add_argument("-d", help="use default dictionary, which is extended ASCII chars (256 chars) mapped to the interval [.2,.8]", action="store_true")
  parser.add_argument("--generate-key", type=None, help="generate a new key")
  args = parser.parse_args(argv)

  x0 = args.x0
  control_param = args.b if args.b else 3.78  # value needs to create a chaotic system
  plaintext = args.text
  lim = 65532             # ~2^16, 16 bit int
  trans_time = 250        # first ciphertext iteration value must be > than this (lyapunov time)
  trans_coeff = args.xmit if args.xmit else 0
  alphabet = [chr(_) for _ in range(256)]       # 256 char ascii

  streamcipher = StreamCipher(trans_time, trans_coeff, lim)
  streamcipher.set_ctrl_param(control_param)
  streamcipher.set_init_val(x0)
  streamcipher.set_charset(alphabet)
  streamcipher.gen_charmap()
  cipher_state = streamcipher.gen_ciphertext(plaintext)
  ciphertext = cipher_state[0]
  return ", ".join([str(_) for _ in ciphertext])


if __name__ == "__main__":
  ciphertext = main(sys.argv[1:])
  print(ciphertext)
