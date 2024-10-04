import math
"""
Viết một hàm nhận vào một danh sách các số,
 trả về tổng của các số trong danh sách.
"""



    
def tinh_tong(so):
    if len(so) == 0:
        print("Không có giá trị.")
    elif len(so) != 0:
        total = sum(so)
             
n = int(input("Nhập số lượng số nguyên :"))
so = []
for i in range(n):
    so = int(input(f"Mời nhập số nguyên thứ {i+1}: "))
    so.append(so)
tong = tinh_tong(so) 
print(f"Tổng các phần tử trong danh sach bằng {tong}")