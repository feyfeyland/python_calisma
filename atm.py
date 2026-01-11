bakiye=1000
while True:
    kullanici_secimi=input("\nİşlem seç(1: yatır, 2:çek, q: çık): ")
    if kullanici_secimi=="q":
        print("Güle Güle")
        break
    elif kullanici_secimi=="1":
        tutar=int(input("Lütfen yatırmak istediğiniz tutarı girin: "))
        bakiye+=tutar
        print(f"Yeni bakiyeniz: {bakiye}")
    elif kullanici_secimi=="2":
        tutar=int(input("Lütfen çekmek istediğiniz tutarı girin: "))
        if tutar>bakiye :
            print("Yetersiz bakiye")
        else:
             bakiye-=tutar
        print(f"Kalan bakiyeniz: {bakiye}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          










   

    
        
