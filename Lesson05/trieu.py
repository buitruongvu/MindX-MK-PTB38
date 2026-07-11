kwh = int(input("Nhập số kWh tiêu thụ: "))
tong_tien = 0

if kwh <= 50:
    tong_tien = kwh * 1700
elif kwh <= 100:
    tong_tien = (50 * 1700) + (kwh - 50) * 1900
elif kwh <= 200:
    tong_tien = (50 * 1700) + (50 * 1900) + (kwh - 100) * 2100
else:
    tong_tien = (50 * 1700) + (50 * 1900) + (100 * 2100) + (kwh - 200) * 3000

print(f"Số tiền điện cần phải trả: {tong_tien} đồng")