import os
import pandas as pd

# === CONFIGURACIÓN ===
carpeta_entrada = r"C:\Users\Christian\Downloads\Señales recortadas-20250706T033129Z-1-001\Señales recortadas\Extensor\Jose"  # Carpeta con los archivos CSV originales
carpeta_salida = "Jose5"  # Carpeta donde se guardarán los CSV convertidos
frecuencia_muestreo = 1000  # Hz

# Crear carpeta de salida si no existe
os.makedirs(carpeta_salida, exist_ok=True)

# Procesar todos los archivos .csv en la carpeta de entrada
for nombre_archivo in os.listdir(carpeta_entrada):
    if nombre_archivo.endswith(".csv"):
        ruta_entrada = os.path.join(carpeta_entrada, nombre_archivo)
        ruta_salida = os.path.join(carpeta_salida, f"EI_{nombre_archivo}")

        # Leer el archivo original (una sola columna)
        df = pd.read_csv(ruta_entrada)

        # Crear columna de timestamp en milisegundos
        df_tiempo = pd.DataFrame({
            "timestamp": (df.index * 1000 / frecuencia_muestreo).astype(int),  # en milisegundos
            "emg": df.iloc[:, 0]
        })

        # Guardar en formato compatible con Edge Impulse
        df_tiempo.to_csv(ruta_salida, index=False, encoding='utf-8')

        print(f"Convertido: {nombre_archivo} -> {ruta_salida}")
