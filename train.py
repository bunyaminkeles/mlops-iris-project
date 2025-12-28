from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Veriyi Yükle
iris = load_iris()
X, y = iris.data, iris.target

# 2. Veriyi Böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Modeli Eğit
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 4. Modeli Kaydet (Modeli bir dosya olarak dışarı aktarıyoruz)
joblib.dump(model, 'model.joblib')

print("Model başarıyla eğitildi ve 'model.joblib' olarak kaydedildi.")