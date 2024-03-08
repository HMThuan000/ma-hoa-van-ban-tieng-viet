from cryptography.fernet import Fernet
class CAES:
    # Mã hóa văn bản bằng AES
    def MaHoa(self, plaintext):
        key = Fernet.generate_key()
        f = Fernet(key)
        encrypted_text = f.encrypt(plaintext.encode())
        return encrypted_text, key

    # Giải mã văn bản bằng AES
    def GiaiMa(self, ciphertext, key):
        f = Fernet(key)
        decrypted_text = f.decrypt(ciphertext).decode()
        return decrypted_text

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Ví dụ sử dụng
def Run():
    # Văn bản gốc
    plaintext = input("Mời nhập văn bản cần mã hoá: ")

    # Tạo đối tượng
    cAES = CAES() 
    # Mã hóa văn bản
    encrypted_text, aes_key = cAES.MaHoa(plaintext)
    print("Văn bản sau khi mã hoá: ", encrypted_text)

    # Giải mã văn bản
    decrypted_text = cAES.GiaiMa(encrypted_text, aes_key)
    print("Văn bản đã được giải mã: ", decrypted_text)


#=========================================
if __name__ == "__main__":
    Run()
    
