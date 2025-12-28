from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Kaydedilen Modeli Geri Yükle
model = joblib.load('model.joblib')

# 2. API Uygulamasını Başlat
app = FastAPI()

# 3. Gelen Verinin Formatını Belirle (Validasyon için)
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 4. Ana Sayfa Endpoint'i
@app.get("/")
def home():
    return {"message": "MLOps Level 1: Iris Model API Hazır!"}

# 5. Tahmin Endpoint'i
@app.post("/predict")
def predict(data: IrisInput):
    # Gelen veriyi modelin anlayacağı formata (array) çevir
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    
    # Tahmin yap
    prediction = model.predict(features)
    
    # Sonucu döndür (0: Setosa, 1: Versicolor, 2: Virginica)
    return {"prediction": int(prediction[0])}