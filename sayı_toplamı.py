n = int(input("Bir sayı giriniz: "))

tplm = 0

for i in range(1, n + 1):
    tplm += i

print(f"1'den {n}'e kadar sayıların toplamı: {tplm}")
