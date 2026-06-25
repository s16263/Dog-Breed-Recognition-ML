import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import os

# Konfiguracja strony
st.set_page_config(page_title="Dog Breed Classifier", page_icon="🐶", layout="wide")

# Funkcja ladujaca model
@st.cache_resource
def load_model_and_classes():
    model_path = 'models/best_model.keras'
    json_path = 'models/class_names.json'
    
    if not os.path.exists(model_path) or not os.path.exists(json_path):
        return None, None
        
    model = tf.keras.models.load_model(model_path)
    
    with open(json_path, 'r', encoding='utf-8') as f:
        class_names = json.load(f)
        
    return model, class_names

# Sidebar - Informacje
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=100)
    st.header("O projekcie")
    st.write("Klasyfikator ras psow oparty na sieci MobileNetV2.")
    st.divider()
    st.write("Wgraj zdjecie, a model w ulamku sekundy sprawdzi, jaka to rasa.")

# Glowny interfejs
st.title("🐶 Klasyfikator Ras Psow")
st.markdown("Witaj! Sprawdzmy, jakiej rasy jest Twoj pies.")

# Ladowanie modelu
model, class_names = load_model_and_classes()
if model is None:
    st.error("Blad: Nie znaleziono plikow modelu w folderze /models!")
    st.stop()

# Uploader
uploaded_file = st.file_uploader("Wybierz zdjecie psa...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption='Analizowane zdjecie', use_container_width=True)
    
    with col2:
        if st.button("🚀 Rozpoznaj rase"):
            with st.spinner("Analizowanie..."):
                img = image.resize((224, 224))
                img_array = tf.keras.utils.img_to_array(img)
                img_array = np.expand_dims(img_array, 0)
                
                predictions = model.predict(img_array)
                predicted_class_index = np.argmax(predictions[0])
                confidence = np.max(predictions[0]) * 100
                
                predicted_breed = class_names[predicted_class_index].split('-')[-1].replace('_', ' ').title()
                
                st.subheader("Wynik analizy:")
                st.success(f"To jest: **{predicted_breed}**!")
                st.metric(label="Pewnosc modelu", value=f"{confidence:.2f}%")
                
                if confidence > 80:
                    st.balloons()