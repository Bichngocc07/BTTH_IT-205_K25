# Câu 1: Khởi động - Tính tiền thanh toán 
# Viết chương trình tính tiền mua hàng cho khách.
# Yêu cầu người dùng nhập vào Đơn giá của một sản phẩm và Số lượng mua.
# Tính Tổng tiền = Đơn giá * Số lượng.
# Áp dụng logic khuyến mãi:
# Nếu Tổng tiền >= 1.000.000, giảm giá 10% trên Tổng tiền.
# Nếu Tổng tiền < 1.000.000, không giảm giá.
# In ra màn hình số tiền cuối cùng khách phải thanh toán.

don_gia = float(input("Nhập đơn giá của sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong_tien = don_gia * so_luong
if tong_tien >= 1000000:
    giam_gia = tong_tien * 0.10
    tien_thanh_toan = tong_tien - giam_gia
else:
    tien_thanh_toan = tong_tien

print(f"Số tiền cuối cùng khách phải thanh toán: {tien_thanh_toan}")

# Câu 2: Vận dụng - Hệ thống đăng nhập bảo mật 
# Mô phỏng chức năng đăng nhập trước khi vào phần mềm. Giả sử mật khẩu đúng được lưu sẵn trong một biến là 123456.
# Sử dụng vòng lặp để yêu cầu người dùng nhập mật khẩu.
# Nếu nhập đúng, in ra "Đăng nhập thành công!" và kết thúc chương trình.
# Nếu nhập sai, in ra "Mật khẩu sai, vui lòng nhập lại!".
# Ràng buộc: Khách hàng chỉ được phép nhập sai tối đa 3 lần. Nếu quá 3 lần, in ra thông báo "Tài khoản đã bị khóa!" và buộc thoát chương trình.
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