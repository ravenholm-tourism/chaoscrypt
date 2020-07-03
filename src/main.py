import streamcipher as sc


def main():
  alphabet = [chr(_) for _ in range(256)]       # 256 char ascii
  x_0 = 232323e-6         # initial starting point in interval
  lim = 65532             # ~2^16 or short int
  trans_time = 250        # first ciphertext iteration value must be > than this (lyapunov time)
  # trans_coeff = 0
  trans_coeff = .2        # for character i, transmit if random number in [0,1] >= .2 (~76% chance each try will succeed)
  control_param = 3.8     # parameter for logistic map - alternate chaotic values: 3.56995, 3.82843 (most values between 3.57 and 4 work)
  plaintext = 'hi'

  streamcipher = sc.StreamCipher(trans_time, trans_coeff, lim)
  streamcipher.set_charset(alphabet)
  streamcipher.set_ctrl_param(control_param)
  streamcipher.set_init_val(x_0)
  streamcipher.gen_charmap()

  # print(streamcipher.get_key())
  # cipher_1 = streamcipher.gen_cipherchar('h')
  # print(cipher_1)
  # cipher_2 = streamcipher.gen_cipherchar('i',cipher_1[1])
  # print(cipher_2)

  cipher_state = streamcipher.gen_ciphertext(plaintext)
  ciphertext = cipher_state[0]
  print(ciphertext)


if __name__ == "__main__":
  main()
