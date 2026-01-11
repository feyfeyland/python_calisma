import pandas as pd
import numpy as np

# Veriyi hazırladık
veriler = {
    "Gun": ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"],
    "Derece": [25, 30, None, 22, 40, None, 18]
}
df = pd.DataFrame(veriler)

# 1. TEMİZLİK: Tablonun (df) içindeki boşlukları at
# DİKKAT: 'derece' değil 'df' kullandık.
temiz_df = df.dropna()

# 2. DÖNÜŞÜM: Temiz tablonun "Derece" sütununu alıp Array yap
# DİKKAT: np.array(...) parantezinin içine veriyi koyduk.
dereceler = np.array(temiz_df["Derece"])

# 3. MATEMATİK: Burayı zaten doğru yapmıştın, tebrikler.
fahrenheit = (dereceler * 1.8) + 32

print("Temizlenmiş Veriler:")
print(temiz_df)
print("\nFahrenheit Sonuçları:")
print(fahrenheit)


# EKSTRA: Ortalamayı bul (np.mean)
print(f"\nOrtalama Sıcaklık (F): {np.mean(fahrenheit)}")
