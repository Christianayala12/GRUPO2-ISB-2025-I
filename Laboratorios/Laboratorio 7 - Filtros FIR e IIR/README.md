# **LABORATORIO 07: Filtros FIR  e IIR**
## **Tabla de contenidos**

1. [Filtrado de señal ECG](#n1)
2. [Filtrado de señal EMG](#n2)  
3. [Filtrado de señal EEG](#n3)  

 ## 1. ECG <a name="n1"></a>



 ## 2. EMG <a name="n2"></a>

### **Objetivo:**
Procesar las señales EMG para reducir el ruido y los artefactos, enfocándose en resaltar la actividad muscular relevante.

### **Procesamiento:**

1. **Filtro FIR**
   - Objetivo: Aislar la banda de frecuencia de interés que corresponde a la actividad muscular.
   - Métodos de ventana: **Hamming y Blackman**.
   - Especificaciones sugeridas:
     - **Frecuencia de corte (Fc): 40 Hz**. Solo las frecuencias asociadas a la actividad muscular (por debajo de 40 Hz) se mantienen.
     - **Pasabanda bajo**

     
2. **Filtro IIR**
   - Objetivo: Eliminar las frecuencias altas asociadas a ruido eléctrico y artefactos de movimiento que interfieren con la señal EMG.
   - Filtros usados: **Butterworth y Chebyshev tipo I**
   - Especificaciones sugeridas:
     - **Frecuencia de corte (Fc): 60 Hz**, corresponde al ruido eléctrico y los artefactos de movimiento.
     - **Frecuencia de paso (Wp): 188 rad/s (30 Hz)**. Permite el paso de las frecuencias de interés, que son las frecuencias más bajas de la señal EMG.
     - **Frecuencia de atenuación (Ws): 300 rad/s (47.75 Hz)**. Define la frecuencia a partir de la cual las señales no deseadas se atenúan de forma significativa.
   


| Campo de Actividad| Señal Cruda     | Filtros FIR         | Filtros IIR     |
|-------------------|------------------|------------------|------------------|
| Descanso           | ![](imagenes_filtros/EMG/FIR/reposo.png) | ![](imagenes_filtros/EMG/FIR/reposo_blackman.png) ![](imagenes_filtros/EMG/FIR/reposo_hamming.png)| ![](imagenes_filtros/EMG/IIR/REPOSO_BUTTER.png) ![](imagenes_filtros/EMG/IIR/REPOSO_CHEBY.png)|
| Contracción leve   | ![](imagenes_filtros/EMG/FIR/movimiento.png) | ![](imagenes_filtros/EMG/FIR/movimiento_blackman.png) ![](imagenes_filtros/EMG/FIR/movimiento_hamming.png)| ![](imagenes_filtros/EMG/IIR/MOVIMIENTO_BUTTER.png) ![](imagenes_filtros/EMG/IIR/MOVIMIENTO_CHEBY.png)|
| Contracción fuerte | ![](imagenes_filtros/EMG/FIR/fuerza.png)  | ![](imagenes_filtros/EMG/FIR/fuerza_blackman.png) ![](imagenes_filtros/EMG/FIR/fuerza_hamming.png) | ![](imagenes_filtros/EMG/IIR/FUERZA_BUTTER.png) ![](imagenes_filtros/EMG/IIR/FUERZA_CHEBY.png)|

 ### Comparación de filtros FIR
 ![](imagenes_filtros/EMG/FIR/dif_magnitudes.png)

Se puede observar que aunque los filtros comparten las mismas especificaciones, también presentan diferencias sutiles en su comportamiento espectral.
Primero, en la **ventana Blackman** se muestra una atenuación más pronunciada en las frecuencias fuera de la banda de interés, lo cual se puede traducir en una reducción más agresiva del contenido de alta frecuencia. Por otro lado, la **ventana Hamming** presenta un espectro más elevado en la zona de atenuación, lo que indica que es un poco más permisiva en cuanto al contenido fuera de la banda.
Sin embargo, en general, ambos filtros cumplen con el objetivo planteado, el cual es aislar la banda de actividad muscular, pero el filtro con ventana Blackman resulta más eficiente en la supresión de ruido de alta frecuencia.

 ### Comparación con filtros IIR
![](imagenes_filtros/EMG/IIR/BUTTER_VS_CHEBY2.png)

A pesar de que los filtros comparten las mismas especificaciones de diseño, se observan variaciones en sus respuestas espectrales. La señal filtrada con el **filtro Butterworth** presenta una transición suave entre la banda pasante y la banda de rechazo, con una atenuación gradual de las frecuencias más altas, sin generar rizado ni distorsión aparente. En contraste, el **filtro Chebyshev tipo I** ofrece una caída más abrupta en la banda de rechazo; sin embargo, este rendimiento viene acompañado de ondulaciones o rizado en la banda pasante, visibles especialmente en las frecuencias iniciales, lo que puede introducir cierta distorsión en la señal dentro del rango útil. En conclusión, el **filtro Butterworth** ofrece una respuesta más suave, ideal para aplicaciones donde la calidad de la señal es crítica ya que no atenúa de manera agresiva. En contraste, el **filtro Chebyshev tipo I** elimina mejor el ruido porque atenúa más rápido las frecuencias no deseadas, pero puede alterar un poco la señal útil debido al rizado en la banda pasante.

 ## 3. EEG <a name="n3"></a>

### **Objetivo:**
Preprocesar las señales EEG para reducir el ruido y extraer caracteristicas de interes como ondas cerebrales especificas.

### **Procesamiento:**

1. **Filtro IIR**
   - Filtro: Butterworth
   - Especificaciones sugeridas:
     - **Frecuencia de corte (Fc): 30 Hz**. Solo las frecuencias asociadas a la actividad cerebral (por debajo de 30 Hz) se mantienen.
     - **Pasabajos**
     - **Frecuencia de paso (Wp): 188 rad/s (30 Hz)**. Permite el paso de las frecuencias de interés, que son las frecuencias más bajas de la señal EMG.
     - **Frecuencia de atenuación (Ws): 300 rad/s (47.75 Hz)**. Define la frecuencia a partir de la cual las señales no deseadas se atenúan de forma significativa.

2. **Filtro FIR**
   - Objetivo: Extraer bandas de frecuencia especificas (alfa, beta, etc.).
   - Filtros usados: **Hamming**
   - Especificaciones sugeridas:
     - **Frecuencias de corte (Fc): 8-12 Hz**, pasa banda para ondas alfa.

| Campo de Actividad| Señal Cruda     | Filtros FIR         | Filtros IIR     |
|-------------------|------------------|------------------|------------------|
| Basal           |<img width="832" alt="Captura de pantalla 2025-05-14 a la(s) 08 09 38" src="https://github.com/user-attachments/assets/6a0b619e-8008-4ece-80aa-f6df93b9da32" />|<img width="827" alt="Captura de pantalla 2025-05-14 a la(s) 08 12 57" src="https://github.com/user-attachments/assets/7ec9270d-6a3c-49a3-ba57-a2139a74e0ff" />|<img width="653" alt="Captura de pantalla 2025-05-14 a la(s) 08 11 34" src="https://github.com/user-attachments/assets/8c003433-5b20-4c9e-90af-8dc9c1dd2e60" />|
| Ojos Cerrados   |<img width="828" alt="Captura de pantalla 2025-05-14 a la(s) 08 15 01" src="https://github.com/user-attachments/assets/d4f20308-cd17-44a8-be70-8273c4a5a98d" />|<img width="824" alt="Captura de pantalla 2025-05-14 a la(s) 08 16 23" src="https://github.com/user-attachments/assets/424ee51e-8982-47f2-8afa-bf6a6bcfda3a" />| <img width="643" alt="Captura de pantalla 2025-05-14 a la(s) 08 15 38" src="https://github.com/user-attachments/assets/c6a1fe3e-774e-4152-aa92-984899d1cec5" />|
| Preguntas |<img width="837" alt="Captura de pantalla 2025-05-14 a la(s) 08 18 20" src="https://github.com/user-attachments/assets/e06bfa5e-bb0c-470e-8cee-79e7def091a3" />|<img width="833" alt="Captura de pantalla 2025-05-14 a la(s) 08 19 05" src="https://github.com/user-attachments/assets/f232c013-35d6-4fcc-909c-a24a78014302" />|<img width="661" alt="Captura de pantalla 2025-05-14 a la(s) 08 18 39" src="https://github.com/user-attachments/assets/91dcda1a-7deb-4fb4-ab56-76091eb97950" />
|

