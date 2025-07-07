# **Project: Analysis of Forearm Muscle Activation During Typing and Clicking Tasks in University Students**
# **Proyecto:Análisis de la activación muscular en músculos del antebrazo durante tareas de mecanografía y uso del mouse en estudiantes universitarios**

## Motivación
El uso intensivo de computadoras en estudiantes universitarios ha generado un aumento en la incidencia de fatiga muscular y trastornos musculoesqueléticos, especialmente en los músculos del antebrazo involucrados en tareas repetitivas como la mecanografía y el clickeo. Aunque se sugiere que la actividad física regular podría tener un efecto protector, existen pocos estudios que evalúen su impacto directo sobre la activación muscular durante estas actividades cotidianas.


## Resumen  
Este estudio analiza la activación muscular del antebrazo durante tareas de mecanografía y clickeo en estudiantes universitarios físicamente activos y sedentarios. Se utilizaron señales de electromiografía de superficie (sEMG) registradas con sensores BITalino en los músculos flexor digitorum superficialis y extensor digitorum. Los datos fueron procesados y clasificados mediante un modelo de redes neuronales convolucionales desarrollado en Edge Impulse, con el objetivo de identificar signos de fatiga muscular.

Los resultados mostraron un rendimiento limitado del modelo (precisión de entrenamiento: 55,6 %; prueba: 45 %), sin lograr diferenciar adecuadamente los estados de fatiga. No se observaron diferencias significativas en la activación muscular entre estudiantes activos y sedentarios, lo que sugiere que, en tareas digitales de corta duración, el nivel de actividad física no tendría un impacto determinante en la fatiga muscular.

## Principales hallazgos
- El modelo de red neuronal alcanzó una **precisión de 55,6 % en entrenamiento y 45 % en prueba**, sin lograr detectar correctamente los casos de fatiga.

- **Las bandas espectrales entre 93,75 y 218,75 Hz** fueron las más relevantes para la clasificación de fatiga muscular.

- Las clases fatiga y no fatiga mostraron **alto solapamiento** en el espacio de características, lo que dificultó la diferenciación.

- **No se encontraron diferencias significativas en la activación muscular entre estudiantes físicamente activos y sedentarios.**

- Factores como el tamaño reducido de muestra, la variabilidad en técnicas de mecanografía y el agarre del mouse podrían haber influido en los resultados.
