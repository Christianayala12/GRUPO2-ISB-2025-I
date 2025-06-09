# **LABORATORIO 10: EKG Processing**
## **Tabla de contenidos**

1. [Actividad 1](#n1)
2. [Actividad 2](#n2)
3. [Actividad 3](#n3)
4. [Actividad 4](#n4)

## Actividad 1 <a name="n1"></a>
 #### - Generar 2 señales EKG de duración 20 s
#### - Gráfica de forma independiente estas señales
  
Primero, instalamos las librerías necesarias:
```
!pip install neurokit2
```
Segundo, importamos las librerías:
```
import numpy as np
import neurokit2 as nk
import matplotlib.pyplot as plt
```
Después, generamos la primera señal EKG
```
ti = np.array((-50, -10, 0, 15, 100))
ai = np.array((1.2, -5, 35, -7.5, 0.75))
bi = np.array((0.25, 0.1, 0.1, 0.1, 0.4))

ti = np.random.normal(ti, np.ones(5) * 3)
ai = np.random.normal(ai, np.abs(ai / 5))
bi = np.random.normal(bi, np.abs(bi / 5))

ecg1 = nk.ecg_simulate(duration=20, method="ecgsyn", ti=ti, ai=ai, bi=bi)

# 4. Crear eje de tiempo en segundos
fs = 1000
n_samples = len(ecg1)
t = np.linspace(0, n_samples / fs, n_samples)

plt.figure(figsize=(10, 3))
plt.plot(t, ecg1, color="darkgreen")
plt.title("ECG Sintético (una derivación) con ti/ai/bi personalizados")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (u.a.)")
plt.xlim(0, t[-1])
plt.grid(ls=":")
plt.tight_layout()
plt.show()
```
LA FOTO DE LA PRIMERA EKG AAAAAAAAAAA %%%%%%%%%%%%%%%%%%%%%%%%%

Y generamos la segunda señal EKG:
```
ti = np.array((-70, -8, 0, 15, 100))
ai = np.array((1.2, -5, 30, -7.5, 0.75))
bi = np.array((0.25, 0.1, 0.1, 0.1, 0.4))

ti = np.random.normal(ti, np.ones(5) * 3)
ai = np.random.normal(ai, np.abs(ai / 5))
bi = np.random.normal(bi, np.abs(bi / 5))

ecg2 = nk.ecg_simulate(duration=20, method="ecgsyn", ti=ti, ai=ai, bi=bi)

# 4. Crear eje de tiempo en segundos
fs = 1000 
n_samples = len(ecg2) 
t = np.linspace(0, n_samples / fs, n_samples)

plt.figure(figsize=(10, 3))
plt.plot(t, ecg2, color="darkgreen")
plt.title("ECG Sintético (una derivación) con ti/ai/bi personalizados")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (u.a.)")
plt.xlim(0, t[-1])
plt.grid(ls=":")
plt.tight_layout()
plt.show()
```

LA FOTO DE LA SEGUNDA EKG AAAAAAAAAAA %%%%%%%%%%%%%%%%%%%%%%%%%

## Actividad 2 <a name="n2"></a>
 #### - Para cada señal simulada, extraigan características básicas

Importamos las librerías que usaremos:
```
from scipy.stats import skew, kurtosis
```
Después, calculamos e imprimimos las características de cada uno:
Para la primera señal:
```
mean_ecg1 = np.mean(ecg1)
median_ecg1 = np.median(ecg1)
kurtosis_ecg1 = kurtosis(ecg1)
skewness_ecg1 = skew(ecg1)
energy_ecg1 = np.sum(ecg1**2)

# Imprimir las características
print(f"Mean: {mean_ecg1}")
print(f"Median: {median_ecg1}")
print(f"Kurtosis: {kurtosis_ecg1}")
print(f"Skewness: {skewness_ecg1}")
print(f"Energy: {energy_ecg1}")
```
LA FOTO DE LA IMPRESION DE EKG 1 AAAAAAAAAAA %%%%%%%%%%%%%%%%%%%%%%%%%

Para la segunda señal:
```
mean_ecg2 = np.mean(ecg2)
median_ecg2 = np.median(ecg2)
kurtosis_ecg2 = kurtosis(ecg2)
skewness_ecg2 = skew(ecg2)
energy_ecg2 = np.sum(ecg2**2)

# Imprimir las características
print(f"Mean: {mean_ecg2}")
print(f"Median: {median_ecg2}")
print(f"Kurtosis: {kurtosis_ecg2}")
print(f"Skewness: {skewness_ecg2}")
print(f"Energy: {energy_ecg2}")
```
LA FOTO DE LA IMPRESION DE EKG 2 AAAAAAAAAAA %%%%%%%%%%%%%%%%%%%%%%%%%

## Actividad 3 <a name="n3"></a>
 #### - Extraer caracteristicas de las señales EKG, reducir la dimensionalidad con PCA y graficas el scatterplot

Importamos las librerías:
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import skew, kurtosis
from sklearn.decomposition import PCA
import neurokit2 as nk
```
Ponemos las señales en una lista para iterar:
```
ecg_signals = [ecg1, ecg2]
signal_names = ['ECG_1', 'ECG_2']
```
Hacemos la tabla panda:
```
all_features = []

for i, signal in enumerate(ecg_signals):
    ecg_cleaned = nk.ecg_clean(signal, sampling_rate=fs, method="biosppy")
    peaks_dict = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)
    rpeaks = peaks_dict[0]

    if len(rpeaks) >= 2:
        t_peaks = rpeaks / fs
        rr_intervals = np.diff(t_peaks)  # array de (N_peaks - 1) valores en segundos
        rr_mean = np.mean(rr_intervals)
        rr_std  = np.std(rr_intervals)
    else:
        rr_mean = np.nan
        rr_std  = np.nan

    # 2.3) Estadísticos “básicos” + HOS
    feats = {
        'Signal_Type'       : signal_names[i],
        'Mean'              : np.mean(signal),
        'Median'            : np.median(signal),
        'STD'               : np.std(signal),
        'Skewness'          : skew(signal),
        'Kurtosis'          : kurtosis(signal, fisher=True),  # fisher=True => kurtosis “exceso” (gaussiana=0)
    #    'RR_Intervals_Mean' : rr_mean,
    #    'RR_Intervals_STD'  : rr_std
    }

    all_features.append(pd.DataFrame([feats]))

combined_features_df = pd.concat(all_features, ignore_index=True)

print("=== DataFrame con características extraídas ===")
print(combined_features_df)
```
PONER LA FOTO DE LA TABLA PANDA AAAAAAAAAAAAAAAAA %%%%%%%%%%%%%%%%%%%%%

Hacemos el PCA:
```
pca_input = combined_features_df.drop(columns=['Signal_Type']).copy()

pca_input = pca_input.fillna(pca_input.mean())

pca = PCA(n_components=2)
pca_result = pca.fit_transform(pca_input)  # devuelve matrix (n_signals × 2)

pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
pca_df['Signal_Type'] = combined_features_df['Signal_Type']

print("\n=== Resultados PCA (2 dimensiones) ===")
print(pca_df)
```
Finalmente, graficamos el PCA:
```
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x='PC1',
    y='PC2',
    hue='Signal_Type',
    data=pca_df,
    s=100,
    palette="Set2"
)
plt.title('PCA de Características de ECG (2 Dimensiones)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.grid(alpha=0.3)
plt.legend(title='Tipo de Señal')
plt.tight_layout()
plt.show()
```
PONER LA FOTO DE LA GRAFICA DE PCA AAAAAAAAAAAAAAAAA %%%%%%%%%%%%%%%%%%%%%

## Actividad 4 <a name="n4"></a>
 #### - De las 2 señales EKG creada, creado 3 mas adicionales con las mismas caracteristicas de estas 2 iniciales.
#### - Extrae sus caracteristicas y ponlos en una tabla en pandas, luego etiqueta estas señales. ejemplo: 0,1,2.
#### - Reduce las dimensionalidad a 2 y grafica si existe separabilidad.

Primero, importamos las librerías a usar:
```
import numpy as np
import neurokit2 as nk
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
```
Después, creamos las 3 señales EKG

Primer EKG (ekg 0)
```
ti = np.array((-60, -5, 0, 12, 100))
ai = np.array((1.5, -5, 15, -7.2, 0.75))
bi = np.array((0.15, 0.1, 0.1, 0.1, 0.4))

ti = np.random.normal(ti, np.ones(5) * 3)
ai = np.random.normal(ai, np.abs(ai / 5))
bi = np.random.normal(bi, np.abs(bi / 5))

ecg_0 = nk.ecg_simulate(duration=20, method="ecgsyn", ti=ti, ai=ai, bi=bi)

# 4. Crear eje de tiempo en segundos
fs = 1000 
n_samples = len(ecg_0)
t = np.linspace(0, n_samples / fs, n_samples)

plt.figure(figsize=(10, 3))
plt.plot(t, ecg_0, color="darkgreen")
plt.title("ECG Sintético (una derivación) con ti/ai/bi personalizados")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (u.a.)")
plt.xlim(0, t[-1])
plt.grid(ls=":")
plt.tight_layout()
plt.show()
```
Segundo EKG (ekg 1):












