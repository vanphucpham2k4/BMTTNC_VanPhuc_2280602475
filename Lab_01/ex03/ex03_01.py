def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num in lst:
            if num % 2 == 0:
                tong += num
    return tong

input_list = input("Nhập danh sách các số,các nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print("tổng các số chẵn trong lst là: ", tong_chan)