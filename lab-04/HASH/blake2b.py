import hashlib

def calculate_blake2b(input_string):
    h = hashlib.blake2b()
    h.update(input_string.encode('utf-8'))
    return h.hexdigest()


text = input("Nhập chuỗi văn bản: ")
print("Chuỗi bạn vừa nhập:", text)
print("Chuỗi sau khi băm BLAKE2b:", calculate_blake2b(text))
