import mlflow

# 1. Konfiguracja MLflow
mlflow.set_experiment("Klasyfikacja_Ras_Psow")

# Rozpoczynamy śledzenie eksperymentu
with mlflow.start_run(run_name="Baseline_MobileNetV2"):
    
    # 2. Definiujemy parametry, które chcemy śledzić
    epochs = 3
    batch_size = 32
    learning_rate = 0.001
    
    # Logujemy parametry do MLflow
    mlflow.log_param("epochs", epochs)
    mlflow.log_param("batch_size", batch_size)
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("model_architecture", "MobileNetV2")

    print("Symulacja treningu modelu (logowanie)...")
    
    # Przykładowe wyniki z naszego wcześniejszego treningu w notatniku
    accuracy = 0.88 
    loss = 0.35
    
    # Logujemy metryki do MLflow
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("loss", loss)
    
    print(f"Logowanie zakończone! Accuracy: {accuracy}, Loss: {loss}")