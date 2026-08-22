# Cú pháp của hàm có giá trị trả về
# def <Tên hàm>(<Tham số>):
    #<Khối lệnh>
    #return <Giá trị trả về>
# def: Từ khóa để khai báo một hàm
# Tên hàm: Tên do người dùng đặt, thỏa mãn các quy tắc đặt tên của Python
# Tham số: Dữ liệu được truyền từ bên ngoài vào bên trong hàm để thực hiện các xử lý
# Khối lệnh: Là một hoặc nhiều câu lệnh
# return: Từ khóa dùng để chỉ giá trị trả về
# Giá trị trả về: Kết quả sau khi thực hiện khối lệnh bên trong hàm
def sum(a, b):
  sum = a + b
  return sum

result = sum(1, 2)
print(result)

#Thực hành 1: Viết hàm truyền vào hai số nguyên a và b, trả về a luỹ thừa b
# Dùng input nhập vào 2 số nguyên dương a và b sau đó tính a mũ b
def exponentiation(a, b):
  return a ** b
# a = int(input("Enter a positive integer: "))
# b = int(input("Enter a positive integer: "))
# print(exponentiation(a, b))

# Thực hành 2: Viết hàm truyền vào một số nguyên, trả về giá trị tuyệt đối của số nguyên đó
# dùng input nhập vào số nguyên rùi tính giá trị tuyệt đối bằng hàm trên
# Cách 1:
def absolution(number):
  if number >= 0:
    return number
  else:
    return - number

# int_num = int(input("Enter number: "))
# print(f"absolute value of {int_num} is {absolution(int_num)}")

# # Cách 2:
# print(f"Absolute value of {int_num} is {abs(int_num)}")

# Thực hành 3: Viết hàm truyền vào một danh sách, trả về tổng các phần tử của danh sách đó
number_list = [12, 1, -3, 5, -6, 11, 8, 2] 

def calculate_total(num_list: list):
  total = 0
  for number in num_list:
    total += number
  return total

print(calculate_total(number_list))

# Các kiểu dữ liệu python trả về
# 1: int
# 2: float
# 3: str
# 4: bool
# 5: list 
# Math Libraries
import math
a = 15
b = 12
print(f"UCLN của {a} và {b} là: {math.gcd(a, b)}")
print(f"BCNN của {a} và {b} là: {math.lcm(a, b)}")

c = 2
d = 3
print(f"{c} mũ {d} là {math.pow(2, 3)}")

my_name = "Vu Le Anh"
print(my_name.lower())
print(my_name.upper())

name = "pham nhat minh"
print(name.swapcase())
print(name.title())

# Random Libraries
import random
print(random.randint(0, 100))
