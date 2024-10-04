#lệnh if-else
"""
age = 23
if age < 18:
    print("Bạn là vị thành niên! ")
elif age < 30:
    print("Bạn là thanh niên! ")
else:
    print("Bạn đã trưởng thành! ")
"""
age = 23
if age < 18:
    print("Bạn là vị thành viên.")
elif age < 30:
    print("Bạn là thanh niên.")
else:
    print("Bạn là người trưởng thành>")


#vòng lập for

for i in range(1,6):
    print(f" Số: {i}")


#vòng lập while

i = 1
while i <= 6:
    print(f"Số : {i}")
    i += 1


i = 1
while i <= 10:
    print(f"Số: {i}")
    i += 2 


#Bài tập 1 
""""
Viết chương trình nhập tuổi của người dùng, sau đó in ra:

"Bạn là vị thành niên" nếu tuổi nhỏ hơn 18.
"Bạn là thanh niên" nếu tuổi từ 18 đến 30.
"Bạn đã trưởng thành" nếu tuổi lớn hơn 30.
"""
tuoi = int(input("Mời bạn nhập tuổi : "))
if tuoi < 18:
    print("Bạn là vị thành niên.")
elif tuoi < 30:
    print("Bạn là thành niên. ")
else:
    print("Bạn đã trưởng thành.")


#Bài tập 2
"""Viết một vòng lặp for để in các số lẻ từ 1 đến 10."""
"""for i in range (10):
    if i % 2 != 0:
        print(i)

# Cách cải tiến cho bài 2 
for i in range (1,10,2):
    print(i)"""



for i in range (1,10,2):
    print(f"Số: {i}")
