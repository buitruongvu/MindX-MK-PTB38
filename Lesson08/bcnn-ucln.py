#cách 1:
a = int(input("Enter a: "))
b = int(input("Enter b: "))

max = a
min = b
if b>a:
  max = b
  min = a
bcnn = max

for i in range(1, min+1):
  if i * max % min == 0:
    bcnn = i*max
    break
print(f"bcnn cua {a} va {b} la {bcnn}")

ucln = min
for i in range(min, 0, -1):
  if max % i == 0 and min % i == 0:
    ucln = i
    break
print(f"ucln cua {a} va {b} la {ucln}")


#Cách 2

# Lưu lại giá trị gốc để in kết quả
temp_a, temp_b = a, b

# Tính UCLN bằng thuật toán Euclid (Rất nhanh)
while temp_b != 0:
    temp_a, temp_b = temp_b, temp_a % temp_b
ucln = temp_a

# Suy ra BCNN từ UCLN
bcnn = (a * b) // ucln

print(f"BCNN của {a} và {b} là {bcnn}")
print(f"UCLN của {a} và {b} là {ucln}")