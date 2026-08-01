a = "MindX"
print(len(a)) #lenght
print(a[0])

A = ["a", "b", "c", "d", "e"]
A[2] = "i"
print(A)

B = "abcde"
# B[2] = "i"

C = "MindX Technology"
for i in range(len(C)):
  print(C[i])
print("----------------------------")

D = "Bui Truong Vu"
for letter in D:
  print(letter)
#Tìm vị trí xâu con thông qua toán tử in
print("Vu" in D)
print("Trung" in D)

#Tìm vị trí xâu con thông qua hàm find()

#Cú pháp: <Xâu mẹ>.find(<xâu con>)
print(D.find("Truong"))
print(D.find("Trung"))
print(D.find("Vu")) #output: 11

D = "Bui Truong Vu"
#Cú pháp đầy đủ: <Xâu mẹ>.find(<xâu con>, <start>, <stop>)
print(D.find("Vu", 2, 10)) #output: -1
print(D.find("Vu", 10, 13)) #output: 11

#Tách một xâu thành mảng các ký tự
#cú pháp: <xâu>.split(<Ký tự tách>)
std_str = "PhamNhat-Minh,Name"
std_list = std_str.split(",")
print(std_list)

#replace()
std2_str = "Vu Le Anh"
new_name = std2_str.replace("Le", "Nhat")
print(new_name) #output: Vu Nhat Anh

std3_str = "Hoang Quoc Quoc Trieu"
new_name2 = std3_str.replace("Quoc", "", 1)
print(new_name2) #output: Hoang  Quoc Trieu



