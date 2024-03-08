import hashlib

data = "Hello, World!"  # Dữ liệu bạn muốn mã hoá

def MaHoaSha3(data):
    # Tạo đối tượng SHA-3 với độ dài mã băm là 256 bits (SHA-3-256)
    sha3_256 = hashlib.sha3_256()
    # Cung cấp dữ liệu đầu vào cho đối tượng SHA-3
    sha3_256.update(data.encode('utf-8'))
    # Lấy mã băm SHA-3
    sha3_256_hash = sha3_256.hexdigest()
    return sha3_256_hash

def Run():
    data = "Phạm Đức Thành"  # Dữ liệu bạn muốn mã hoá
    sha3_256_hash = MaHoaSha3(data)
    print("Mã băm SHA-3-256 của ",data," là:", sha3_256_hash)
    data = "Huflit"  # Dữ liệu bạn muốn mã hoá
    sha3_256_hash = MaHoaSha3(data)
    print("Mã băm SHA-3-256 của ",data," là:", sha3_256_hash)
if __name__ == "__main__":
    Run()
