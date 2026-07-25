# len() (length)
numbers = [1, 8, 4, 2, 10, 15, 12, 18]
length = len(numbers)
print(f"Length of {numbers} is", length)

print(numbers[5])

for index in range(length):
  print(numbers[index], end = " ")
print("")

for number in numbers:
  print(number, end = " ")
print("")

for index, number in enumerate(numbers): #Lặp lấy cả chỉ số index và value
  print(f"{index}: {number}")
#add
numbers.append(21) # Thêm phần tử vào cuối danh sách 
numbers.append(4)
print(numbers)
numbers.insert(1, 23) #Thêm phần tử vào vị trí chỉ định (index)
print(numbers)
#Delete
numbers.remove(4) #Xoá theo giá trị, xoá phần tử đầu tiên từ trái qua phải
numbers.remove(4)
# numbers.remove(4)
print(numbers)
numbers.pop(5) #xoá theo chỉ số index
print(numbers)
# numbers.clear() #xoá toàn bộ phần tử
# print(numbers)
numbers[3] = 1 #Thay đổi giá trị thông qua chỉ số index
print(numbers)
numbers.sort(reverse = True) #Sắp xếp phần tử
print(numbers)




