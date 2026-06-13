# n = int(input("Nhập số n: "))
# if n % 2 == 0:
#   print(f"{n} is even") 
# else:
#   print(f"{n} is odd")

# Bài 1 (Mức độ: Dễ) - Phân loại kết quả học tập
# Yêu cầu thuật toán: Viết chương trình nhận vào điểm trung bình của một học viên (thang điểm 10) và in ra xếp loại học lực tương ứng. Thuật toán cần có bước kiểm tra tính hợp lệ của dữ liệu đầu vào (điểm không được nhỏ hơn 0 hoặc lớn hơn 10).
# • Từ 8.0 trở lên: 'Giỏi'
# • Từ 6.5 đến dưới 8.0: 'Khá'
# • Từ 5.0 đến dưới 6.5: 'Trung bình'
# • Dưới 5.0: 'Yếu'
# • Ngoài khoảng 0-10: 'Điểm không hợp lệ'
# while True:
#   score = float(input("Enter your score: "))
#   if score > 10 or score < 0:
#     print('Điểm không hợp lệ')
#   elif score >= 8.0:
#     print('Giỏi')
#   elif score >= 6.5:
#     print('Khá')
#   elif score >= 5.0:
#     print('Trung bình')
#   else:
#     print('Yếu')

# Bài 2 (Mức độ: Trung bình) - Thuật toán tính học phí với điều kiện lồng nhau
# Yêu cầu thuật toán: Một khóa học lập trình có mức học phí gốc là 5,000,000 VNĐ. Viết thuật toán tính số tiền học viên cần đóng dựa trên các chính sách ưu đãi sau:
# 1. Nếu là học viên cũ, được giảm 20% học phí gốc.
# 2. Nếu đăng ký sớm (trước 10 ngày trở lên), được giảm 10% học phí gốc.
# 3. Nếu thỏa mãn cả hai điều kiện trên, học viên được áp dụng mức giảm 20% trước, sau đó tiếp tục giảm thêm 10% trên mức giá đã giảm.
# 4. Nếu không thỏa mãn điều kiện nào, đóng 100% học phí.
# Input: is_alumni (True/False), days_in_advance (Số ngày đăng ký trước).
# Output: Số tiền cuối cùng cần thanh toán (Kiểu số nguyên).
# while True:
#   is_alumni = input("is alumni (True/False): ") == "True"
#   days_in_advance = int(input("Số ngày đăng ký trước: ")) >= 10
#   hoc_phi = 5000000
#   if is_alumni and days_in_advance:
#     print(hoc_phi * 0.8 * 0.9)
#   elif is_alumni:
#     print(hoc_phi * 0.8)
#   elif days_in_advance:
#     print(hoc_phi * 0.9)
#   else:
#     print(hoc_phi)

# Bài 3 (Mức độ: Khó) - Thuật toán tìm số lớn thứ hai (Không dùng hàm có sẵn)
# Yêu cầu thuật toán: Cho 3 số nguyên a, b, c bất kỳ. 
# Chỉ sử dụng các câu lệnh if - elif - else và toán tử logic,
# hãy viết thuật toán tìm và in ra số có giá trị lớn thứ hai. 
# Không được dùng các hàm built-in như sort(), max(), min(). 
# Nếu có ít nhất 2 số bằng nhau và là số lớn nhất, in ra chính giá trị đó.
while True:
  a, b, c = map(int, input("Nhập 3 số a, b, c cách nhau bởi dấu ',': ").split(","))
  if (a <= b and a >= c) or (a >= b and a <= c):
    print(a)
  elif (b <= a and b >= c) or (b >= a and b <= c):
    print(b)
  else:
    print(c)






