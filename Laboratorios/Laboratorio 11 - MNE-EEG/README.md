# **Actividad de Procesamiento y Análisis de Señales EEG**

## **Tabla de contenidos**
1. Preprocesamiento de señales EEG
2. Optimización de características para ML
3. Análisis integrado con MNE-Python

En el siguiente enlace se presenta el código utilizado en este laboratorio, que abarca todos los pasos, desde la carga de los datos y el preprocesamiento, hasta la extracción de características y la implementación de técnicas de optimización y selección.  
- [Código desarrollado](https://github.com/Christianayala12/GRUPO2-ISB-2025-I/blob/master/Laboratorios/Laboratorio%2011%20-%20MNE-EEG/ML_EEG_LAB_ISB.ipynb)

## 1. Origen de los datos [1]
Para el registro y análisis de las señales EEG, se utilizó un equipo no invasivo Ultra Cortex Mark IV, que opera con una frecuencia de muestreo de 125 Hz. Este dispositivo cuenta con 16 electrodos secos de base de plata clorada. El conjunto de datos utilizado proviene del paquete MNE, específicamente de la función `mne.datasets.eegbci.load_data`, que permite cargar fácilmente señales EEG de la competencia BCI. Esta herramienta es ampliamente utilizada para el análisis de datos EEG en investigaciones sobre interfaces cerebro-computadora (BCI) y otras áreas neurocientíficas. Más detalles sobre esta función y cómo utilizarla están disponibles en la [documentación oficial de MNE](https://mne.tools/stable/generated/mne.datasets.eegbci.load_data.html).

![](imagenes/figura_1.png)  
Figura 1: Las áreas de Brodmann y el sistema de colocación de electrodos 10-10. [1]

## 2. Procedimiento de preprocesamiento [2]
Especificar filtros aplicados (rangos frecuenciales, notch), método de alineación y eliminación de artefactos (ICA).
Para el preprocesamiento de las señales EEG, se utilizó un filtro pasa banda activo en un rango frecuencial de 5 a 50 Hz, Las formas de onda más comúnmente estudiadas incluyen delta (0,5 a 4 Hz); theta (4 a 7 Hz); alfa (8 a 12 Hz); sigma (12 a 16 Hz) y beta (13 a 30 Hz)[2]. Así mismo el equipo de lectura de señales EEG presenta un filtro notch a 60 Hz (para atenuar la interferencia de la línea eléctrica)[3]. Ultracortex no elimina los artefactos por parpadeos o movimientos musculares, por lo que utiliza un análisis de componentes independientes para realizar una limpieza para el análisis y clasificación de las señales EEG, se utilizan librerías MNE en python para implementar ICA para EEG, logrando así separar la actividad cerebral de artefactos oculares, musculares, 60hz del VAC[4].

![](imagenes/figura_2.png)  
Figura 2: Datos de EEG antes y después de la eliminación de artefactos con ICA: se han eliminado los artefactos que potencialmente provenían del parpadeo de los ojos.[5]

## 3. Extracción de características
Para la extracción de características, se utilizó el análisis **Wavelet Morlet** para obtener la representación tiempo-frecuencia (TFR) de las señales EEG. Este análisis se realizó en un rango de frecuencias de **4 a 40 Hz**. Las características extraídas fueron la **potencia espectral en diferentes bandas de frecuencia, como theta (4-8 Hz), alpha (8-12 Hz), beta (13-30 Hz) y gamma (30-40 Hz)**. Estas características representan la actividad eléctrica del cerebro en distintas frecuencias y son útiles para evaluar diferentes estados cognitivos o emocionales del sujeto. Posteriormente, **las potencias promedio por banda de frecuencia** fueron calculadas para cada época (segmento de tiempo) y canal. Estas características fueron usadas para analizar la actividad cerebral en relación con los eventos experimentales y para la clasificación de patrones de actividad cerebral.

## 4. Optimización y selección
Para optimizar y seleccionar las características, se utilizó **normalización con StandardScaler** para estandarizar las características y ponerlas en la misma escala. Luego, se aplicó **PCA** para reducir la dimensionalidad, manteniendo el 95% de la varianza explicada. Además, se calcularon **estadísticas temporales y frecuenciales (media, desviación estándar, máximo y mínimo)** de las características extraídas de las bandas de frecuencia, las cuales fueron usadas como entradas para el análisis y clasificación de las señales EEG.



## Referencias
[1]Víctor Asanza, et al. “MILimbEEG: A Dataset of EEG Signals Related to Upper and Lower Limb Execution of Motor and Motor Imagery Tasks.” Data in Brief, vol. 50, 7 Sept. 2023, pp. 109540–109540, pmc.ncbi.nlm.nih.gov/articles/PMC10505670/, https://doi.org/10.1016/j.dib.2023.109540.  
[2]C. S. Nayak and A. C. Anilkumar, “EEG Normal Waveforms,” Nih.gov, Jul. 24, 2023. https://www.ncbi.nlm.nih.gov/books/NBK539805/  
[3]X. Li, W. Z. Rymer, G. Li, and P. Zhou, “The effects of notch filtering on electrically evoked myoelectric signals and associated motor unit index estimates,” Journal of NeuroEngineering and Rehabilitation, vol. 8, no. 1, Nov. 2011, doi: https://doi.org/10.1186/1743-0003-8-64.  
[4]“(PDF) IAC: On the Feasibility of Utilizing Neural Signals for Access Control,” ResearchGate, 2018, doi: https://doi.org/10.1145//3274694.3274713.  
[5]“(PDF) SmartHelm: User Studies from Lab to Field for Attention Modeling,” ResearchGate, 2022. https://www.researchgate.net/publication/364936500_SmartHelm_User_Studies_from_Lab_to_Field_for_Attention_Modeling/figures?lo=1
