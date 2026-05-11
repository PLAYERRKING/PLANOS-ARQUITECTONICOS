# Proyecto: Visión de Planos Arquitectónicos

Este proyecto consiste en una librería de Python diseñada para procesar imágenes de planos arquitectónicos, permitiendo la detección de muros e intersecciones mediante algoritmos de visión robótica.

---

## Contenido de la Carpeta del Proyecto

La organización del proyecto sigue el estándar de empaquetado de Python, lo cual garantiza la modularidad y la facilidad de distribución.

---

## 1. Directorio Raíz (Proyecto_Vision)

Es el contenedor principal de todo el desarrollo. En este nivel se encuentran los archivos de configuración global y las carpetas de módulos.

### Archivos principales

- **setup.py**  
  Archivo de configuración de setuptools. Contiene los metadatos del paquete, como:
  - Nombre: `vision_tools`
  - Versión
  - Dependencias: `numpy`, `opencv-python`, `matplotlib`

- **README.md**  
  Documento técnico que explica el propósito de la librería, los algoritmos utilizados y las instrucciones de uso.

- **main.py**  
  Script principal para probar la librería con imágenes reales, cargando los módulos de preprocesamiento y detección.

---

## 2. Paquete de Librería (`vision_planos/`)

Contiene el código fuente del proyecto. El archivo `__init__.py` indica que esta carpeta es un paquete de Python.

### Módulos

- **preprocesamiento.py**  
  Funciones para limpieza de imagen:
  - Conversión a escala de grises  
  - Aplicación de filtros Gaussianos para reducción de ruido  

- **deteccion.py**  
  Módulo principal de análisis:
  - Detección de bordes (Canny)  
  - Detección de muros (Hough)  
  - Detección de intersecciones (Harris)  

---

## 3. Carpeta de Recursos (`ejemplos/`)

Contiene imágenes de prueba utilizadas para validar los algoritmos de visión.

---

## Procedimiento de Instalación (Anaconda)

### 1. Localización del Proyecto

Ubícate en la carpeta donde se encuentra el archivo `setup.py`:
```bash
cd "C:\ruta\de\tu\proyecto"
```
### 2. Instalación del Paquete

Ejecuta:

```bash
pip install .
```
### 3. Verificación de la Instalación

Comprueba que se instaló correctamente:

```bash
pip show vision_tools
```
