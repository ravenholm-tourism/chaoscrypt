import streamcipher as scipher
import plaintext as ptext

alphabet = [chr(_) for _ in range(256)]       # ascii
x_0 = .232323
lim = 65535
trans_time = 250
trans_coeff = 0
map_param = 3.8
streamcipher = scipher.StreamCipher(trans_time, trans_coeff, lim)
streamcipher.set_charset(alphabet)
streamcipher.set_ctrl_param(map_param)
streamcipher.set_init_val(x_0)
streamcipher.gen_charmap()
streamcipher.ciphertext = [1713, 364]
#   plaintext = 'hi'
plaintext = ptext.PlainText(streamcipher, streamcipher.get_key(), alphabet)
print(plaintext.decrypt_ciphertext())
# assert plaintext.decrypt_ciphertext() == "hi"