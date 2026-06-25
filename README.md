# 🐶 Dog Breed Classifier

System klasyfikacji ras psów oparty na uczeniu głębokim (Deep Learning), umożliwiający automatyczne rozpoznawanie rasy psa na podstawie przesłanego zdjęcia.

Projekt wykorzystuje **TensorFlow/Keras**, **Streamlit**, **MLflow** oraz **Docker**, zapewniając kompletny pipeline od trenowania modelu po wdrożenie aplikacji.

---

## ✨ Funkcjonalności

* Klasyfikacja ras psów na podstawie zdjęcia
* Interfejs webowy oparty na Streamlit
* Trenowanie modeli TensorFlow/Keras
* Śledzenie eksperymentów przy użyciu MLflow
* Zarządzanie danymi z wykorzystaniem DVC
* Obsługa konteneryzacji Docker

---

## 📋 Wymagania

* Python 3.9+
* Git
* pip

---

## 🚀 Instalacja

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/d-stas/ASI.git
cd ASI
```

### 2. Utworzenie środowiska wirtualnego

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

---

## 📂 Struktura projektu

```text
dog_project/
│
├── data/               # Dane treningowe
├── models/             # Wytrenowane modele
├── notebooks/          # Notebooki i eksperymenty
├── src/                # Kod źródłowy
├── tuning/             # Strojenie hiperparametrów
├── mlruns/             # Logi MLflow
│
├── app.py              # Aplikacja Streamlit
├── train_mlflow.py     # Skrypt treningowy
├── Dockerfile          # Konfiguracja Dockera
├── requirements.txt
├── README.md
│
├── .dvc/
└── .dvcignore
```

---

## 🧠 Model

Model został wytrenowany przy użyciu:

* TensorFlow
* Keras
* Transfer Learning
* Data Augmentation

Zadaniem modelu jest klasyfikacja zdjęcia psa do jednej z dostępnych ras.

### Przykładowe metryki

| Metryka   | Wynik |
| --------- | ----- |
| Accuracy  | XX %  |
| Precision | XX %  |
| Recall    | XX %  |

> Uzupełnij wartości po zakończeniu treningu.

---

## 🔄 Pipeline projektu

1. Przygotowanie danych
2. Augmentacja obrazów
3. Trening modelu
4. Logowanie eksperymentów do MLflow
5. Zapis modelu
6. Predykcja w aplikacji Streamlit

---

## 📊 MLflow

Uruchomienie panelu MLflow:

```bash
mlflow ui
```

Następnie otwórz:

```text
http://localhost:5000
```

---

## 🐳 Docker

Budowanie obrazu:

```bash
docker build -t dog-classifier .
```

Uruchomienie kontenera:

```bash
docker run -p 8501:8501 dog-classifier
```

Aplikacja będzie dostępna pod adresem:

```text
http://localhost:8501
```

---

## 🚀 Uruchomienie aplikacji

```bash
streamlit run app.py
```

---

## 🔮 Możliwe rozszerzenia

* [ ] Większa liczba ras
* [ ] API REST (FastAPI)
* [ ] Deployment na AWS
* [ ] GitHub Actions CI/CD
* [ ] Monitoring modelu po wdrożeniu

---

## 👨‍💻 Autorzy

KK
JK
DS
