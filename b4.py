# danh sách (list ) giống mảng array


my_list = [1, 2, 3, 4] # Danh sách số nguyên

print(my_list)

my_list = [1, "Hello", 3.14, True] # Danh sách chứa các phần tử thuộc nhiều kiểu dữ liệu khác nhau 
print(my_list) 

print(my_list[1]) # truy cập từng giá trị

my_list[1] = "Xin chào" # Thay đổi phần tử tại chỉ số 1

my_list.append(44) # thêm số vào cuối danh sách

# my_list.remove("Hello") xóa phần tử "Hello"
# my_list.pop() xóa phần tử cuối cùng

# duyệt qua danh sách
for item in my_list:
    print(item)



#Bài tập 1
"""
Tạo một danh sách chứa 5 số nguyên.

Thay đổi giá trị của phần tử thứ 3 trong danh sách.
Thêm một số mới vào cuối danh sách.
Xóa phần tử thứ 2 trong danh sách.
"""
"""
my_list = [1,2,3,4,5]
my_list[3] = 9 
my_list.append(66) 
my_list.remove(2)

for item in my_list:
    print(item)

"""


list = [1,2,3,4,5]
list[3] = 9
list.append(66)
list.pop(1) 
#Bài tập nâng cao 

"""
Tạo danh sách các chuỗi (strings) và thực hiện các thao tác như:

Thay đổi giá trị của một phần tử.
Thêm một chuỗi mới vào danh sách.
Xóa một chuỗi khỏi danh sách.
Sử dụng phương thức sort() để sắp xếp danh sách 
số nguyên theo thứ tự tăng dần
và in ra danh sách sau khi sắp xếp.
"""

my_list = [3,"Thắng", 1 , "Xin chào", 6 , "Nha"]
my_list[2] = 9 
my_list.append("NHÉ")
my_list.pop(5)
#my_list = sorted(my_list, key=str)
# chia thành từng phần của số và chuỗi 
nums = [item for item in my_list if isinstance(item,int)]
strings = [item for item in my_list if isinstance(item,str)]
#sắp xếp từng phần 
nums.sort()
"""strings.sort()"""
#gộp lại
my_list = nums + strings
print(my_list)
for item in my_list:
    print(item)


