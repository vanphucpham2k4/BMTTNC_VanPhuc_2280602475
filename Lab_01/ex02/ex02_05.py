So_gio_lam =float(input("Nhập số giờ làm mỗi tuần: "))
Luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, So_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * Luong_gio + gio_vuot_chuan * Luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")