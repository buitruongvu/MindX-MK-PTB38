product_list = ["Quần", "Áo", "Rau, củ", "Thịt", "Cá", "Gạo"]
shopping_cart = []
while True:
  print("--------------SHOPPING CART---------------")
  print("1. Xem danh sách sản phẩm")
  print("2. Xem giỏ hàng")
  print("3. Thêm sản phẩm vào giỏ hàng")
  print("4. Xóa sản phẩm khỏi giỏ hàng")
  print("5. Thoát")
  choice = input("Nhập lựa chọn của bạn (1-5): ")
  if choice == "1":
    print("---------MENU---------")
    for index, item in enumerate(product_list):
      print(f"{index + 1}. {item}")
  elif choice == "2":
    if not shopping_cart:
      print("Giỏ hàng của bạn đang trống!!")
    else: 
      print("Các mặt hàng trong giỏ hàng của bạn là: ")
      for index, item in enumerate(shopping_cart):
            print(f"{index + 1}. {item}")
  elif choice == "3":
    print("Danh sách sản phẩm: ")
    for index, item in enumerate(product_list):
      print(f"{index + 1}. {item}")
