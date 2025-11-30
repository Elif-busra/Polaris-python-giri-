
while True:
 a= int (input("sayınızı giriniz: "))
 if a > 0:
      print ("sayınız 0'dan büyük yani pozitif")
 elif a < 0:
      print ("sayınız 0'dan küçük yani negatif")
 else :
      print ("sayınız 0 ")
 devam= int(input("devam etmek için 1'e basınız, işlemi bitirmek için 0'a basın "))
 if devam != 1 :
       print ("işleminiz bitmiştir...")
       break
