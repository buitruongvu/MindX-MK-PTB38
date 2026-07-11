#Nhập vào số nguyên n, kiểm tra n có phải số nguyên tố hay không 
n = int(input("Enter n: "))
if n <2:
  print(f"{n} not a prime number")
else:
  is_prime = True
  for i in range(2, n):
    if n % i == 0:
      is_prime = False
      break
if is_prime:
  print(f"{n} is a prime number")
else:
  print(f"{n} not a prime number")