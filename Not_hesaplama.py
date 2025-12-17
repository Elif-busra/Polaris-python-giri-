while True:
 a= int (input("notunuzu giriniz: "))
 if a >= 50:
      print ("Geçti")
 else :
      print ("Kaldı")

 devam= int(input("devam etmek için 1'e basınız, işlemi bitirmek için 0'a basın "))
 if devam != 1 :
       print ("işleminiz bitmiştir...")
       break
