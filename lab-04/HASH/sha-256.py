import hashlib

def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

text = input("Nhập chuỗi cần băm SHA_256: ")
print("giá trị hash SHA-256:", calculate_sha256(text))

