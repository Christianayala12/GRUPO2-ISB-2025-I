# **LABORATORIO 03: – Adquisición de señal EMG con BITalino**
## **Tabla de contenidos**

1. [Introducción](#n1)
2. [Propósito de la práctica](#n2)  
3. [Materiales y metodología](#n3)  
4. [Resultados y limitaciones](#n4)  
5. [Referencias bibliográficas](#n5)
   
 ## 1. Introducción: <a name="n1"></a>
El análisis de señales biomédicas como la electromiografía (EMG) y el electrocardiograma (ECG) es esencial para evaluar el funcionamiento del sistema neuromuscular y del sistema cardiovascular, respectivamente. La EMG permite registrar la actividad eléctrica generada por los músculos, facilitando el estudio de desórdenes neuromusculares, la caracterización de la fatiga muscular y el desarrollo de interfaces de control en rehabilitación. Por su parte, el ECG proporciona información clave sobre la actividad eléctrica del corazón, siendo indispensable para la detección de arritmias, cardiopatías isquémicas y otras alteraciones cardíacas (1).  
El uso de tecnologías accesibles y didácticas como BITalino ha revolucionado la enseñanza y la investigación en bioinstrumentación. BITalino es una plataforma modular, de bajo costo y fácil integración, diseñada para la adquisición en tiempo real de señales fisiológicas. Este sistema incluye sensores para EMG, ECG, EDA, acelerometría, entre otros, y es ampliamente utilizado en entornos educativos y de investigación aplicada (2). Su compatibilidad con el software OpenSignals (r)evolution permite visualizar, procesar y exportar señales de manera sencilla, lo cual lo convierte en una herramienta ideal para prácticas académicas y prototipado de dispositivos biomédicos (3).

 ## 2. Propósito de la práctica: <a name="n2"></a>
Durante la presente práctica, se empleará BITalino en conjunto con el software OpenSignals (r)evolution para la captura y visualización de señales EMG y ECG. Se abordará desde la configuración inicial del sistema hasta la exportación de datos adquiridos, permitiendo a los estudiantes familiarizarse con el flujo completo de trabajo en bioinstrumentación. Esta experiencia permitirá comprender mejor las características eléctricas de las señales musculares y cardíacas, así como adquirir habilidades prácticas en el manejo de herramientas tecnológicas en el campo de la ingeniería biomédica.

 ## 3. Materiales y metodología: <a name="n3"></a>

 ### Materiales
 | Descripción                                   | Cantidad | Imagen                          |
|----------------------------------------------|----------|---------------------------------|
| Batería 3.7V                                  | 2        | ![Batería](Imagenes-L3/IM0.png) |
| OpenSignals - PLUX Wireless Biosignals SA    | 2        | ![OpenSignals](Imagenes-L3/IM2.png) |
| Electrodos descartables tipo disco           | 6        | ![Electrodos](Imagenes-L3/IM3.png) |
| Cable de 3 electrodos sensor Ag/AgCl         | 2        | ![Cable](Imagenes-L3/IM4.png) |
| BITalino                                     | 2        | ![BITalino](Imagenes-L3/IM5.png) |
| Laptop                                       | 2        | ![Laptop](Imagenes-L3/IM6.png) |

 ### Métodos

 #### **Conexiones al Bitalino**

![Conexiones](Imagenes-L3/IM7.png)
 
 1. Se conecta la batería de 3.7V al puerto de energía y se enciende el bluetooth de la laptop/celular.
 2. Se conecta al bitalino de código 78-31 y se desactivan todos los canales del vitalino menos el canal 1.
 3. Se conecta el sensor AG/AgCl de 3 electrodos al puerto indicado para EMG (Electromiograma)


 #### **Colocación de elctrodos**
 Se evaluaron 4 músculos en el estudio de señales. 

 **Sujeto 1**
  1. Músculo fusiforme del antebrazo  
     ![Antebrazo](Imagenes-L3/IM8.png)   
     Se colocan los electrodos positivo y negativo a lo largo del centro de la fibra muscular y el electrodo de referencia en el hueso del codo. Se tomaron medidas en reposo, durante ejercicios de extensión y flexión de la muñeca (4).

 **Sujeto 2**
  1. Trapecio Superior  
     ![Trapecio](Imagenes-L3/IM9.png)  

     Se colocan los electrodos positivo y negativo a lo largo del centro superior de la fibra muscular y el electrodo de referencia en la apófisis mastoides (detrás de la oreja) (5).
     
  2.  Bíceps brachii
    
       ![Biceps](Imagenes-L3/IM10.png)  

      Se colocan los electrodos positivo y negativo a lo largo del centro del músculo y el electrodo de referencia en el hueso del codo (6). 
   

   

 


 

 ## 4. Resultados y limitaciones: <a name="n4"></a>

 ### Sujeto 1

 ### Sujeto 2

 ## 5. Referencias bibliográficas: <a name="n5"></a>
 [1] Gisbert JA. Electromiografía clínica. 2ª ed. Madrid: Editorial Médica Panamericana; 2006.  
 [2] Tercedor Sánchez LG. Electrocardiografía clínica: fundamentos y aplicaciones. Madrid: Díaz de Santos; 2018  
 [3] Silva H, Lourenço P, Fred A. OpenSignals: A Modular Software Tool for Biomedical Signal Acquisition and Processing. In: 2014 IEEE International Symposium on Medical Measurements and Applications (MeMeA); 2014 May 30-31; Lisbon, Portugal.  
 [4] Rojas-Martínez M, García M, Alonso JF, Marín J, Mañanas MÁ. Evaluación de la función neuromuscular del antebrazo durante contracciones isométricas mediante electromiografía de superficie multicanal. Rev Iberoam Autom Inform Ind. 2011;8(2):35-44. https://doi.org/10.1016/s1697-7912(11)70024-3  
 [5] Instituto Nacional de Ciencias Neurológicas. Guía técnica de procedimientos médicos: electromiografía (EMG). Pruebas electrodiagnósticas: neuroconducción motora y sensitiva, electromiografía de aguja, latencias tardías, reflejo de parpadeo y estimulación repetitiva. Lima: Ministerio de Salud del Perú; 2016. p. 26–7.  
 [6] Burhan N, Kasno M, Ghazali R, Said MR, Abdullah SS, Jali MH. Analysis of the biceps brachii muscle by varying the arm movement level and load resistance band. J Healthc Eng. 2017;2017:1–8. https://doi.org/10.1155/2017/1631384

