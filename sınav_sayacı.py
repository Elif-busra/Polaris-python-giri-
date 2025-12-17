from datetime import datetime

sinav_tarihi = input("Sınav tarihini gir (YYYY-MM-DD HH:MM): ")
sinav = datetime.strptime(sinav_tarihi, "%Y-%m-%d %H:%M")

simdi = datetime.now()
fark = sinav - simdi

gun = fark.days
saat = fark.seconds // 3600

print(f"Sınava {gun} gün {saat} saat kaldı 🥲")
