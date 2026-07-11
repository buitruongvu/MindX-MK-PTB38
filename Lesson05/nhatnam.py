kwh = int(input("Nhập số kWh tiêu thụ: "))

if kwh <= 50:
    tien = kwh * 1700
elif kwh <= 100:
    tien = 50 * 1700 + (kwh - 50) * 1900
else:
    tien = 50 * 1700 + 50 * 1900 + (kwh - 100) * 2100

print("Số tiền điện cần phải trả:", tien, "đồng")