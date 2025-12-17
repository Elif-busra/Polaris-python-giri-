import random

sayi = random.randint(1, 100)

while True:
    tahmin = int(input("Tahmininizi giriniz (1-100): "))

    if tahmin < sayi:
        print("Yukarı çık ")
    elif tahmin > sayi:
        print("Aşağı in ")
    else:
        print("Tebrikler! Doğru bildin 🎉")
        break
