import hashlib

def MaHoaMD5(data):
    # Tạo đối tượng MD5
    md5 = hashlib.md5()
    # Cung cấp dữ liệu đầu vào cho đối tượng MD5
    md5.update(data.encode('utf-8'))
    # Lấy mã băm MD5
    md5_hash = md5.hexdigest()
    return md5_hash 

def Run():
    userName = "Phạm Đức Thành"  # Dữ liệu bạn muốn mã hoá
    password = "Huflit"

    md5_hash = MaHoaMD5(userName)
    print("Mã băm MD5 của ",userName," là:", md5_hash)

    md5_hash = MaHoaMD5(password)
    print("Mã băm MD5 của ",password," là:", md5_hash)

if __name__ == '__main__':
    Run()
