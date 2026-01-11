import pandas as pd
import numpy as np

veriler = {
    "Ogrenci": ["Ali", "Ayşe", "Fatma", "Hayri", "Veli"],
    "Not": [45, None, 80, None, 60]
}
df = pd.DataFrame(veriler)

temiz_df = df.dropna()

notlar = np.array(temiz_df["Not"])

# Hoca bonkör davrandı, herkese 10 puan ekle (Vektörel İşlem)
yeni_notlar = notlar + 10

print("Temizlenmiş ve Puan Eklenmiş Notlar:")
print(yeni_notlar)



