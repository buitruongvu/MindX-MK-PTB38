# def <function name> (<parameters>):
#     ...Code to be executed...
# def: là từ khoá để khai báo một hàm
# function name: là tên do người dùng đặt, thoả mãn các quy tắc đặt tên của python


#Hàm không có giá trị trả về (A function with no return value (often called a "void function" or "procedure"))
# Example calculate two numbers 
def calculate_sum(number1, number2):
  sum = number1 + number2
  print(f"Sum of {number1} and {number2} is {sum}")

calculate_sum(50, 100)


# Example Hello() no parameter
def Hello():
  my_name = input("Enter your name: ")
  print(f"Hello everyone ! my name is {my_name} ")
Hello()

# Ví dụ 3: Viết hàm nhập vào một số nguyên, xuất ra màn hình giá trị tuyệt đối của số nguyên vừa nhập
# Example 3: Write a function that takes an integer as input and outputs the absolute value of the entered integer to the screen.
def absolute_value():
  number = int(input("Enter an integer: "))
  if number < 0:
    absolute = -number
  else: 
    absolute = number
  print(f"The absolute value of {number} is {absolute}")

# Ví dụ 4: Viết hàm nhập vào một số nguyên dương, tính tổng các số chẵn từ 1 đến n và xuất ra màn hình.
# Example 4: Write a function that takes a positive integer as input, calculates the sum of the even numbers from 1 to n, and outputs it to the screen.

def sum_even_numbers():
  positive_number = int(input("Enter a positive integer: "))
  even_sum = 0
  for number in range(2, positive_number + 1, 2):
    even_sum += number
  print(f"the sum of the even numbers from 1 to {positive_number} is {even_sum}")
# 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 
sum_even_numbers()
# Hàm có giá trị trả về (A function with return value)
# for odd number (tổng các số lẻ từ 1 đến n)
def odd_even_numbers(positive_number):
  odd_sum = 0
  for number in range(1, positive_number + 1, 2):
    odd_sum += number
  return odd_sum
  #yield (học sau)
 # 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100
 #                              Đối số (Argument)
sum_odd_numbers = odd_even_numbers(20)
print(sum_odd_numbers)
# Lúc viết/tạo hàm -> Cần Tham số (Parameter)
# Lúc dùng/gọi hàm -> Truyền Đối số (Argument)

# Phạm vi sử dụng biến (Scopes)
# 1. Local Scope (Phạm vi Cục bộ)
# Biến cục bộ: 
def sum():
  a = 3
  b = 5
  print(a+b)
sum()
# print(a + b)
# 3. Global Scope (Phạm vi Toàn cục)
a = 10
b = 5
c = 3
def sum2():
  b = 2
  global c
  c = 7
  print(a + b)  # 12
  print(a + c) # 17
sum2() 
print(a + b) # 15
print(a + c) # 17