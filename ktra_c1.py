
# C1
don_gia = float(input("Nhập đơn giá của sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong_tien = don_gia * so_luong
if tong_tien >= 1000000:
    giam_gia = tong_tien * 0.10
    tien_thanh_toan = tong_tien - giam_gia
else:
    tien_thanh_toan = tong_tien

print(f"Số tiền cuối cùng khách phải thanh toán: {tien_thanh_toan}")

# C2
mat_khau_dung = "000000"
so_lan_nhap_sai = 0
while so_lan_nhap_sai < 3:
    mat_khau_nhap = input("Nhập mật khẩu: ")
    if mat_khau_nhap == mat_khau_dung:
        print("Đăng nhập thành công!")
        break
    else:
        so_lan_nhap_sai += 1
        print("Mật khẩu sai, vui lòng nhập lại!")
if so_lan_nhap_sai == 3:
    print("Tài khoản đã bị khóa!")
