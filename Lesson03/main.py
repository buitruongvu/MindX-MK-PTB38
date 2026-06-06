# Warm up !!!!
# print()
# Data Type: string, int, float, boolean
# Quy tắc đặt tên biến: 
# - bao gồm chữ hoa, chữ thường, số, và dấu _ (Underscore)
# - Tên biến không bắt đầu bằng số
# - Tên biến không trùng với từ khoá
# - Biến phân biệt chữ hoa chữ thường
# input()
# ép kiểu vd: int(input())
#-------------------------------------------------------------
# Operators
# 1. Toán tử số học: + - * / // % **
print(1 + 3) # output: 4  Toán tử cộng 
print(12 - 15) #output: -3 Toán tử trừ
print(12 * 10) #output: 120 Toán tử nhân
print(15 / 5) #output: 3.0 Toán tử chia
print(17 // 4) #output: 4 chia lấy phần nguyên
print(17 % 4) #output: 1 Chia lấy phần dư
print(2 ** 3) #output: 8 Luỹ thừa

print(2 ** 2 ** 3) #output: 256 QT1: thực hiện từ phải qua trái
# Còn các loại toán tử khác, thì thực hiện từ trái qua phải
# QT2: Ưu tiên theo thứ tự: luỹ thừa (**) -> nhân chia (* / // %) -> cộng trừ(+ -)
print(1 + 4 * 3 ** 2) # output: 37
#QT3: toán tử thao tác được trên xâu ký tự
print("Hello" + "World") # output: Hello World
print("hi" * 3) # output: hihihi
print("hi" * 0) # output: chuỗi rỗng
# 2. Toán tử quan hệ
# so sánh bằng ( == ) trả về True hoặc False
print(4 == 5) # output: False
print(5 == 5) # output: True
# so sánh bằng ( != ) trả về True hoặc False
print(4 != 5) # output: True
print(5 != 5) # output: False
# Lớn hơn (>) và lớn hơn hoặc bằng (>=)
print(12 >= 12) # output: True
print(12 > 25) #output: False
# Bé hơn (<) và Bé hơn hoặc bằng (<=)
print(12 <= 12) # output: True
print(12 < 25) #output: True

#3. Toán tử logic
# phép toán and (và)
print(3>2 and 4>3) # output: True
print(2>3 and 4>3) # output: False
# phép toán or (hoặc)
# phép toán not (Phủ định)
print(not 3>4) #output: True
# Trắc nghiệm: 20 câu
# https://docs.google.com/forms/d/e/1FAIpQLSeyrSScLkJT8PnHje0BeGVDlVWRi_5pyEN-kSatTHzs4M5ZfA/viewform
# Câu 1:  Kết quả của biểu thức `-11 // 3` trong Python là gì? => -3.6666 => -4
# Câu 2: Giá trị của biểu thức `10 % -3` là bao nhiêu? => a % b = a - b * (a//b) = 10 - (-3)*(10//-3) = 10 - (-3)*(-4) = -2
# Câu 3: Kết quả của biểu thức `2 ** 3 ** 2` là gì? => 512
# Câu 4: Biểu thức `0.1 + 0.2 == 0.3` trả về giá trị gì? => False
# Câu 5: Biểu thức `5 > 4 > 3 == 3` trả về giá trị gì? <=> 5>4 and 4>3 and 3 == 3 => True 
# Câu 6: Cho x = True và y = False. Giá trị của biểu thức `x + y + 2` là bao nhiêu? => True == 1; False == 0 => 1 + 0 + 2 = 3
# Câu 7: Kết quả của so sánh `'apple' > 'Apple'` là gì? => True
# Câu 8: Toán tử `or` sẽ trả về giá trị nào trong biểu thức sau: `0 or '' or [] or 5 or {}`? => or thì trả về giá trị Truthy đầu tiên => 5
# Tìm hiểu thêm về Truthy và Falsy
# Câu 9: Toán tử `and` sẽ trả về giá trị nào trong biểu thức: `[1, 2] and 'Python' and 0 and True`? => and thì trả về giá trị falsy đầu tiên: => 0
# Câu 10: Kết quả của biểu thức `not 'False'` là gì? => 'False' là giá trị Truthy => not Truthy là False
 
# Câu 11: Biểu thức `'a' and 'b' or 'c'` sẽ trả về giá trị nào? => and chứa toàn bộ là truthy thì trả về giá trị cuối cùng 'a' and 'b' == 'b' 
#or thì trả về giá trị truthy đầu tiên => 'b' or 'c' == 'b'
# Câu 12: Biểu thức `10 - 3 ** 2 // 2` có giá trị là bao nhiêu? => 6
# Câu 13: Thứ tự ưu tiên (từ cao xuống thấp) của các toán tử logic trong Python là gì?
# not -> and -> or
# Câu 14: Kết quả của `1 == True and 0 == False` là gì? => True and True == True
# Câu 15: Cho hai danh sách a = [1, 2] và b = [1, 2]. Kết quả của `(a == b) and (a is not b)` là?
# True and True => True
# Câu 16: Kết quả của biểu thức `not 5 == 5 or 4 < 5` là gì? => False or True => True
# Câu 17: Biểu thức `"" == False` trả về giá trị gì? => "" là giá trị Falsy nhưng không không = False

# Câu 18: Điều gì xảy ra khi thực hiện phép tính `5 / 0` và `5 // 0` trong Python? => Cả hai đều sinh ra ngoại lệ ZeroDivisionError
# Câu 19: Biểu thức so sánh Tuple `(1, 2, 4) < (1, 2, 3, 5)` sẽ trả về? => 4 < 3 => False
# Câu 20: Biểu thức `10 > 5 or 5 / 0` có sinh ra lỗi `ZeroDivisionError` không? => 
