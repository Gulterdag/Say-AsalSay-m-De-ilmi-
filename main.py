sayi = int(input("Bir sayı giriniz:"))
for i in range(2, sayi):
    if sayi % i == 0:
        print(sayi, "sayısı bir asal sayıdır.")
        break
else:
    print(sayi, "sayısı bir asal sayı değildir.")
