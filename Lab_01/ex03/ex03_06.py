def tao_tuple_tu_lst(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số,các nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple= tao_tuple_tu_lst(numbers)
print("lst sau đi đảo ngược: ",my_tuple)