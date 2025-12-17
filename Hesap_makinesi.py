while True:
 a = float(input("ilk sayıyınızı giriniz: "))
 b = float(input("ikinci sayınızı giriniz: "))
 print ("toplama için 1 e basınız \nçıkarma için 2 ye basınız \nbölme için 3 e basınız \nçarpma için 4 e basınız")
 topla= a + b
 cikar= a - b
 bol = a/b
 carp = a*b
 islem= int(input("hangi işlemi seçiyorsunuz: "))
 if islem == 1:
    print ("sonucunuz:", topla)
 elif islem == 2:
     print ("sonucunuz:", cikar)
 elif islem == 3:
      print ("sonucunuz:", bol) 
 elif islem == 4:
      print ("sonucunuz:", carp)
 else :
      print ( "islemi hatalı seçtiniz" )
 devam= input (" isleminize devam etmek istiyor musunuz (evet/hayır): ").lower()
 
 if devam != "evet" :
    print("programdan çıkılıyor..")
    break
      
 
   
