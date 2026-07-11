# App đoán số từ 1 đến 100
import random
number_random = random.randint(1, 100)
number_player = int(input("Nhập số bạn đoán (số từ 1 - 100): "))
while number_player != number_random:
  if number_player > number_random:
    print("Số cần tìm nhỏ hơn")
  if number_player < number_random:
    print("Số cần tìm lớn hơn")
  number_player = int(input("Nhập lại số bạn đoán (số từ 1 - 100): "))
print("Chính xác rồi")
  