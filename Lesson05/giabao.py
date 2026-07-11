kwh = int(input("Số kWh tiêu thụ là 145"))

if kwh <= 50:
    tien = kwh * 1700
else:
    tien = 50 * 1700 + kwh - 50 * 1900

print("Số tiền phải trả : ")
