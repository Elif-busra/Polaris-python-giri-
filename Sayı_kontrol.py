while True:
    try:
        x = int(input("Sayınızı Giriniz..."))
        print(f"Sayınız {x} ")
    
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")
