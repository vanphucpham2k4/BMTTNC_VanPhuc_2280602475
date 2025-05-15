def dao_nguoc_lst(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số,các nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

lst_dao_nguoc= dao_nguoc_lst(numbers)
print("lst sau đi đảo ngược: ",lst_dao_nguoc)