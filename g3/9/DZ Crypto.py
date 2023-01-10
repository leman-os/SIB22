from Crypto.Cipher import AES
import hashlib

cipher_text = b'q\x051\x81\xe9W\x15\xc9\x1c\x8b\x8b\x8bz\xe0\x90\x9fZ\x9f\x89"cD3d<;1V11\xfet\x94\n.\x7f\x07#d\xfe\x8f!9\x1a\xfb\xbf\x96\xbe'


for i in range(100, 999):
    key = hashlib.sha256(bytes(str(i), encoding="utf-8")).digest()
    BS = AES.block_size
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    cipher_text = cipher_text
    iv = cipher_text[:BS]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(cipher_text[BS:]))
    if (plain_text == b""): continue
    print(i,":", plain_text)