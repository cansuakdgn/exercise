# Kullanıcıdan bir sayı alarak 1’den bu sayıya kadar olan 
# tüm sayıların toplamını hesaplayan bir Python programı yazın.
# Programda hem for hem de while döngüsü kullanarak
# iki farklı yöntemle sonucu ekrana yazdırın.

# Kullanıcıdan sayı alma
sayi = int(input("Bir sayı girin: "))

# For döngüsü ile toplama işlemi
toplam_for = 0
for i in range(1, sayi + 1):
    toplam_for += i
print(f"For döngüsü ile toplam: {toplam_for}")

# While döngüsü ile toplama işlemi
toplam_while = 0
i = 1
while i <= sayi:
    toplam_while += i
    i += 1
print(f"While döngüsü ile toplam: {toplam_while}")
