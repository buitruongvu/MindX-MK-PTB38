# Bài 1: Khởi tạo và Duyệt xâu
# Yêu cầu người dùng nhập vào một chuỗi văn bản bất kỳ từ bàn phím. Hãy viết
# chương trình thực hiện các công việc sau:
# Duyệt qua chuỗi và in ra màn hình từng ký tự, mỗi ký tự trên một dòng.
# Đếm và thông báo ra màn hình:
# Số lượng ký tự là chữ cái (không phân biệt hoa, thường).
# Số lượng ký tự là chữ số.
# Số lượng nguyên âm (a, e, i, o, u) có trong chuỗi.
chuoi_van_ban = input("Nhập chuỗi văn bản bất kỳ: ")
letter_count = 0
digit_count = 0
vowel_count = 0
#Duyệt qua chuỗi và in ra màn hình từng ký tự, mỗi ký tự trên một dòng.
for letter in chuoi_van_ban:
  print(letter)
  #Số lượng ký tự là chữ cái (không phân biệt hoa, thường).
  if letter.isalpha():
    letter_count += 1
  #Số lượng ký tự là chữ số.
  if letter.isdigit():
    digit_count += 1
  #Số lượng nguyên âm (a, e, i, o, u) có trong chuỗi.
  if letter in ["a", "e", "i", "o", "u"]:
    vowel_count += 1
print("Số lượng ký tự là chữ cái (không phân biệt hoa, thường) is:", letter_count)
print("Số lượng ký tự là chữ số:", digit_count)
print("Số lượng nguyên âm (a, e, i, o, u) có trong chuỗi:", vowel_count)


  

