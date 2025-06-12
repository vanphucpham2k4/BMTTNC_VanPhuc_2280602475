from Crypto.Hash import SHA3_256

def calculate_sha3_256(input_string):
    h = SHA3_256.new()
    h.update(input_string.encode('utf-8'))
    return h.hexdigest()

text = input("Nhập chuỗi văn bản: ")
print("Chuỗi bạn vừa nhập:", text)

hashed_text = calculate_sha3_256(text)
print("Chuỗi sau khi băm SHA3-256:", hashed_text)
