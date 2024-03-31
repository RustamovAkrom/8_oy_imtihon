from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import base64


def encryption(values: str):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(values.encode("utf-8"), AES.block_size))
    iv = base64.b64encode(cipher.iv)
    ct = base64.b64encode(ct_bytes)
    return key, iv, ct


def decryption(key, iv, ct):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    output = unpad(cipher.decrypt(ct), AES.block_size).decode("utf-8")
    return output
