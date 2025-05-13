# **LABORATORIO 07: Filtros FIR  e IIR**
## **Tabla de contenidos**

1. [Filtrado de señal ECG](#n1)
2. [Filtrado de señal EMG](#n2)  
3. [Filtrado de señal EEG](#n3)  

 ## 1. ECG <a name="n1"></a>



 ## 2. EMG <a name="n2"></a>

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
![](imagenes_filtros/EMG/IIR/BUTTER_VS_CHEBY2.png)|

A pesar de que los filtros comparten las mismas especificaciones de diseño, se observan variaciones en sus respuestas espectrales. La señal filtrada con el **filtro Butterworth** presenta una transición suave entre la banda pasante y la banda de rechazo, con una atenuación gradual de las frecuencias más altas, sin generar rizado ni distorsión aparente. En contraste, el **filtro Chebyshev tipo I** ofrece una caída más abrupta en la banda de rechazo; sin embargo, este rendimiento viene acompañado de ondulaciones o rizado en la banda pasante, visibles especialmente en las frecuencias iniciales, lo que puede introducir cierta distorsión en la señal dentro del rango útil.

 ## 3. EEG <a name="n3"></a>




