# for i in range(0, 10):
#   print("Hello world")
# print("-----------------------")
# for i in range(5):
#   print(i)
# print("-----------------------")
# for i in range(3, 7):
#   print(i)
# print("-----------------------")
# for i in range(3, 8, 2):
#   print(i)
# Way 1:
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# sum = 0
# for i in range(a, b+1):
#   if i % 2 == 0:
#     sum += i # sum = sum + i
# print(f"Sum of range {a} and {b}: {sum}")
#Way 2
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# sum = sum(i for i in range(a, b+1) if i % 2 == 0) # List Comprehension
# print(f"Sum of range {a} and {b}: {sum}")


# Bài 1: Khởi động đếm ngược thời gian
# Yêu cầu: Viết chương trình thực hiện đếm ngược từ số 10 về số 1. Mỗi số được in ra trên một dòng
# riêng biệt. Sau khi kết thúc chu trình đếm, màn hình hiển thị dòng chữ thông báo "Phát nổ!".
# Mục tiêu: Hiểu cách sử dụng bước nhảy âm (negative step) trong hàm range().
# Gợi ý thuật toán: Sử dụng hàm range(start, stop, step) trị bắt đầu là 10,
# giá trị kết thúc bao gồm cả 1 và giảm dần.
# for i in range(10, 0, -1):
#   print(i)
# print("Phát nổ")

# Bài 2: Tính tổng chuỗi số chẵn giới hạn

# Yêu cầu: Nhập vào từ bàn phím một số nguyên dương N. Hãy viết chương trình sử dụng vòng lặp
# để tính tổng của tất cả các số chẵn nằm trong khoảng từ 0 đến N (bao gồm cả N nếu N là số
# số chẵn).
# Mục tiêu: Ứng dụng tham số bước nhảy của hàm range() để tối ưu hóa vòng lặp mà không cần sử
# dụng thêm câu lệnh điều kiện if kiểm tra tính chẵn lẻ bên trong thân vòng lặp.
N = int(input("Nhập N: "))
sum = 0
for i in range(0, N + 1, 2):
  sum += i # sum = sum + i
print(sum)
