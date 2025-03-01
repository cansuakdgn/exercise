# Kullanıcıdan bir sayı alarak, bu sayının çift mi tek mi 
# olduğunu ekrana yazdıran bir Python programı yazın. 
# Eğer sayı negatifse, ekrana "Negatif sayı girdiniz!" 
# mesajı versin.

sayi = int(input("Bir sayı girin: "))

if sayi < 0:
    print("Negatif sayı girdiniz!")
elif sayi % 2 == 0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")

