#Task 1: *Bài tập: Viết chương trình nhập vào danh sách số nguyên cho 
#đến khi người dùng nhập số -1 thì kết thúc danh sách. 
# Xuất ra danh sách đã nhập
# numbers = []
# number = int(input("Nhập số nguyên n (Hoặc -1 để thoát): "))
# while number != -1:
#   numbers.append(number)
#   number = int(input("Nhập số nguyên n (Hoặc -1 để thoát): "))
# print("List:", numbers)


#Task 2: Bài tập: Viết chương trình xóa tất cả các phần tử là số lẻ
#  được tìm thấy đầu tiên ra khỏi danh sách.
# numbers1 = [2, 4, 12, 29, 15, 22, 3, 29]
# for number in numbers1:
#   if number % 2 == 1:
#     odd_number_target = number
#     break
# print(odd_number_target)
# while odd_number_target in numbers1:
#   numbers1.remove(odd_number_target)
# print(numbers1)


#Task 3: Bài tập: Viết chương trình tăng tất cả 
# các phần tử của danh sách lên 1 đơn vị
# numbers2 = [2, 4, 12, 29, 15, 22, 3, 29]
# for index in range(len(numbers2)):
#   numbers2[index] += 1 #numbers2[index] = numbers2[index] + 1
# print(numbers2)

#Task 4: Bài tập: Viết chương trình sắp xếp một danh sách theo thứ tự tăng dần, 
# xóa phần tử có giá trị lớn nhất và xuất danh sách ra màn hình.
numbers3 = [2, 4, 12, 29, 15, 33, 22, 3, 29]
numbers3.sort(reverse=False)
print(numbers3)
numbers3.remove(numbers3[len(numbers3)-1])
print(numbers3)

