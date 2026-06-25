# Używamy lekkiego obrazu Pythona
FROM python:3.9-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy wymagania i instalujemy je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy całą resztę naszych plików
COPY . .

# Wystawiamy port, na którym działa Streamlit
EXPOSE 8501

# Komenda uruchamiająca naszą apkę
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]