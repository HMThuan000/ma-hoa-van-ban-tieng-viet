import hashlib

def MaHoaSha256(data):
    # Tạo đối tượng SHA-256
    sha256 = hashlib.sha256()
    # Cung cấp dữ liệu đầu vào cho đối tượng SHA-256
    sha256.update(data.encode('utf-8'))
    # Lấy mã băm SHA-256
    sha256_hash = sha256.hexdigest()
    return sha256_hash 

def Run():
    data = "Phạm Đức Thành"  # Dữ liệu bạn muốn mã hoá
    sha256_hash = MaHoaSha256(data)
    print("Mã băm SHA-256 của ",data," là:", sha256_hash)

if __name__ =='__main__':
    Run()
