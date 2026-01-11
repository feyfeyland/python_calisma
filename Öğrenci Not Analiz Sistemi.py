import pandas as pd
import numpy as np

# Verileri tutacağımız boş listeler
isimler = []
notlar = []

print("--- NOT GİRİŞ SİSTEMİ (Çıkış için isim yerine 'bitti' yaz) ---")

# --- BÖLÜM 1: VERİ GİRİŞİ (Algoritma) ---
while True:
    isim = input("Öğrenci Adı: ")
    
    # 1. Çıkış Kapısı: İsim 'bitti' ise döngüyü kır
    if isim == "bitti":
        break
        
    giris_notu = input(f"{isim} için not girin (Yoksa boş geçin): ")
    
    # 2. Kontrol: Eğer not boşsa (giris_notu == "") veya sayı değilse
    if giris_notu == "" or not giris_notu.isdigit():
        kaydedilecek_not = None  # Bozuk veri olarak işaretle
    else:
        kaydedilecek_not = int(giris_notu) # Sayıya çevir
        
    # Listelere ekle
    isimler.append(isim)
    notlar.append(kaydedilecek_not)

# --- BÖLÜM 2: TEMİZLİK (Pandas) ---
# Sözlük oluşturup DataFrame'e çeviriyoruz
veri_sozlugu = {"Ogrenci": isimler, "Puan": notlar}
df = pd.DataFrame(veri_sozlugu)

print("\n--- HAM LİSTE ---")
print(df)

# 3. Temizlik: Puanı 'None' olanları sil (.dropna)
temiz_df = df.dropna()

# --- BÖLÜM 3: ANALİZ (Numpy) ---
# 4. 'Puan' sütununu Numpy dizisine çevir
puanlar = np.array(temiz_df["Puan"])

# 5. Ortalamayı bul (np.mean)
ortalama = np.mean(puanlar)
print(f"\nSınıf Ortalaması: {ortalama:.2f}")

# --- BÖLÜM 4: BONUS (Filtreleme ve İşlem) ---
# Ortalamadan düşük alanları bulup 5 puan ekle
# Mantık: puanlar < ortalama olanlara +5 ekle
# İpucu: Bu zor olabilir. Numpy'da şöyle yapılır:
# puanlar[puanlar < ortalama] += 5

# Kodu buraya sen yazmaya çalış (Yapamazsan sor):
puanlar[puanlar<ortalama]+=5
print("\n--- PUAN EKLENMİŞ SON DURUM ---")
print(puanlar)