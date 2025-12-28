# 1. Baz İmaj: Python 3.9'un hafif bir sürümünü kullan (Linux tabanlı)
FROM python:3.9-slim

# 2. Çalışma Dizini: Konteyner içinde /app klasörünü oluştur ve oraya geç
WORKDIR /app

# 3. Bağımlılıkları Kopyala: Önce requirements.txt'yi at (Cache avantajı için)
COPY requirements.txt .

# 4. Yükle: Kütüphaneleri kur
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kodları Kopyala: Kalan tüm dosyaları (main.py, model.joblib vs.) içeri at
COPY . .

# 6. Portu Aç: Konteynerin 8000 portunu dışarı duyur
EXPOSE 8000

# 7. Başlatma Komutu: Konteyner ayağa kalkınca API'yi başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]