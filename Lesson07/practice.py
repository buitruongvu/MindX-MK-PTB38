# Nhập vào nguyên n
# In tất cả các số từ n đến 100
# Bắt nhập lại nếu người dùng nhập -1
n = int(input("Enter interger n: "))
while n == -1:
  n = int(input("Please enter interger n (with n not 1): "))
for i in range(n, 101):
  print(i)
