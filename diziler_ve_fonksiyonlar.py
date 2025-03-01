# Kullanıcıdan 5 adet tam sayı alarak bir listeye ekleyen
# ve ardından bu sayıların en büyüğünü ve en küçüğünü bulan 
# bir Python programı yazın. Bu işlemi gerçekleştiren bir 
# fonksiyon tanımlayın ve çağırarak sonucu ekrana yazdırın.

def en_buyuk_ve_en_kucuk():
    sayilar = []

    # Kullanıcıdan 5 sayı alarak listeye ekledim
    for i in range(5):
        sayi = int(input(f"{i+1}. sayıyı girin: "))
        sayilar.append(sayi)

    # En büyük ve en küçük sayıyı buldum
    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)

    print(f"Girilen sayıların en büyüğü: {en_buyuk}")
    print(f"Girilen sayıların en küçüğü: {en_kucuk}")

en_buyuk_ve_en_kucuk()
