from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

def encrypt_blowfish(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_EAX)
    nonce = get_random_bytes(8)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return nonce + ciphertext + tag

def decrypt_blowfish(key, ciphertext):
    nonce = ciphertext[:8]
    ciphertext = ciphertext[8:-16]
    tag = ciphertext[-16:]
    cipher = Blowfish.new(key, Blowfish.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

# Example usage
key = b'SuperSecretKey'
data = b'Hello, Blowfish!'
ciphertext = encrypt_blowfish(key, data)
print("Ciphertext:", ciphertext)
plaintext = decrypt_blowfish(key, ciphertext)
print("Decrypted:", plaintext.decode('utf-8'))
