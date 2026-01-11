import random
hedef_sayi=[]
while len(hedef_sayi)<4:
    rakam=random.randint(0,9)
    if rakam not in hedef_sayi:
        hedef_sayi.append(rakam)
print("Sayıyı tuttum, hadi tahmin et!")
sayac=0
while True:
    tahmin=input("Tahmininiz nedir: ")
    if tahmin=="q":
        break 
    if len(tahmin) != 4:
        print("lütfen tam 4 rakam gir!")
        continue  
    sayac+=1
    sonuc=""   
    for i in range(4):
      girilen_rakam=int(tahmin[i])
      if girilen_rakam==hedef_sayi[i]:
         sonuc+="✔"
      elif girilen_rakam in hedef_sayi:
       sonuc+="0"
      else:
       sonuc+="x"
    print(sonuc)
    if sonuc=="✔✔✔✔":
       print(f"Tebrikler! {sayac}. denemede bildin")
       break
    
    
       
    
