"""
Viết một hàm nhận vào một số nguyên và trả về "Dương" 
nếu số đó là số dương, và "Âm" nếu số đó là số âm.
"""
def xet(x):
    if x > 0:
        return "Số Dương"
    elif x < 0:
        return "Số Âm"
    else:
        return "Số 0"

x = int(input("Mời nhập vào một số nguyên : "))
tim = xet(x)
print(f"Số {x} là {tim}")

"""
Viết một hàm nhận vào một danh sách các số,
 trả về tổng của các số trong danh sách.
"""



    
def tinh_tong(danhsach):
    tong = 0
    for so in danhsach:
        tong += so
    return tong

danh_sach_so = input("Mời nhập các số, cách nhau bằng dấu cách : ")
#tách chuổi thành danh sách các chuỗi nhỏ
danh_sach_so = danh_sach_so.split() # tách theo dấu cách 
danh_sach_so = [int(so) for so in danh_sach_so]

             
tong = tinh_tong(danh_sach_so)

print(f"Tổng các phần tử trong danh sach bằng {tong}")