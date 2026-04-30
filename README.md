# PLANOS-ARQUITECTONICOS
DESARROLLO DE UNA LIBRERÍA EN PYTHON PARA LA DETECCIÓN DE LÍNEAS, ESQUINAS  E INTERSECCIONES EN PLANOS ARQUITECTÓNICOS 
# Detección de Características en Planos Arquitectónicos
Librería desarrollada para la materia de Visión Robótica.

## Descripción
Esta librería automatiza la extracción de muros e intersecciones en planos digitalizados mediante procesamiento digital de imágenes[cite: 1, 2].

## Pipeline de Procesamiento
1. **Gris y Suavizado**: Se usa un Filtro Gaussiano para eliminar el ruido del escaneo.
2. **Detección de Bordes**: Algoritmo de Canny.
3. **Muros**: Transformada de Hough Probabilística para detectar líneas rectas[cite: 2].
4. **Esquinas**: Algoritmo de Harris para encontrar intersecciones[cite: 2].

## Instalación
```bash
pip install .
