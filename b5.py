#Tuple (Bộ giá trị không thay đổi)
my_tuple = (1,2,3) #tuple chứa các số nguyên
my_tuple = (1,"Xin chào", 3.14)
print(my_tuple[1])
print(len(my_tuple)) #đếm số lượng phần tử 
nested_tuple = ((1,2),(3,4)) #Lồng Tuple
print(nested_tuple[0])


#Dictionary (từ điển-lưu trữ từ khóa/giá trị)
my_dict = {"name":"Nguyễn Thắng" , "age" : 23, "is_student" : True}

person = {
    "name" : "Nguyễn Thắng",
    "age" : 23,
    "is_student" : True
}
print(person["name"])

person["city"] = "Hà Nội" #thêm một cặp khóa/giá trị mới
person["age"] = 26 #thay đổi giá trị của khóa age

del person["is_student"] #xóa cặp khóa/giá trị với khóa is_student

for key, value in person.items(): #duyệt qua các phần tử trong Dictionary
    print(f"Khóa: {key}, Giá trị: {value}")



keys = person.keys() # lấy tất cả khóa
values = person.values() # lấy tất cả giá trị 




#Bài tập 
"""
Tuple:

Tạo một Tuple chứa 5 phần tử (có thể là số, chuỗi, hoặc hỗn hợp).
In ra phần tử thứ 2 của Tuple.
Thử đếm số lượng phần tử trong Tuple.
"""
myTuple = (1, " Thắng" , "Thiên", "Bình" , 6)
print(myTuple[1])
print(len(myTuple)) 


"""
Dictionary:

Tạo một Dictionary để lưu thông tin của một người (bao gồm tên, tuổi, địa chỉ).
Thêm một cặp khóa/giá trị mới vào Dictionary.
Thay đổi giá trị của một khóa có sẵn.
Duyệt qua các phần tử trong Dictionary và in ra từng cặp khóa/giá trị.
"""
nguoi = {
    "tên" : "Thắng",
    "tuổi" : 23,
    "Địa chỉ" : "Vĩnh Long"
}

nguoi["Sở thích"] = "Thể thao"
nguoi["tuổi"] = 26
for key,value in nguoi.items():
    print(f"Khóa  = {key} , Giá trị = {value}")