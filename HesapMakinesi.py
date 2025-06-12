ilksayi = int(input(" Lütfen ilk sayıyı giriniz "))
sonuc = 0
kare = input("Bu sayının karesini almak ister misin?").lower()
if kare == "evet":
    sonuc = ilksayi * ilksayi
    print(sonuc)
elif kare == "hayır":
    ikincisayi = int(input(" Lütfen ikinci sayıyı giriniz "))
    print("yapmak istediğiniz işlemi giriniz")
    islem = input("+, -, *, /")
    if islem == "+":
        sonuc = ilksayi + ikincisayi
        print(sonuc)
    elif islem == "-":
        sonuc = ilksayi - ikincisayi
        print(sonuc)
    elif islem == "*":
        sonuc = ilksayi * ikincisayi
        print(sonuc)
    elif islem == "/":
        sonuc = ilksayi / ikincisayi
        print(sonuc)
