## **Proyecto: Visión de Planos Arquitectónicos**



Este proyecto consiste en una librería de Python diseñada para procesar imágenes de planos arquitectónicos, permitiendo la detección de muros e intersecciones mediante algoritmos de visión robótica.



*Contenido de la Carpeta del Proyecto*



La organización del proyecto sigue el estándar de empaquetado de Python, lo cual garantiza la modularidad y la facilidad de distribución.



##### **1. Directorio Raíz** (Proyecto\_Vision)

Es el contenedor principal de todo el desarrollo. En este nivel se encuentran los archivos de configuración global y las carpetas de módulos.



**setup.py**: Es el archivo de configuración de setuptools. Contiene los metadatos del paquete, como el nombre (vision\_planos), la versión y las dependencias necesarias (numpy, opencv-python, matplotlib). Es el archivo que permite que la librería sea reconocida por el sistema.

**README.md**: Documento técnico que explica el propósito de la librería, los algoritmos utilizados y las instrucciones de uso.

**main.py**: Script de ejecución principal destinado a probar la librería con imágenes reales, cargando los módulos de preprocesamiento y detección.

##### 

##### **2. Paquete de Librería (vision\_planos/)**

Esta carpeta contiene el código fuente lógico del proyecto. La presencia del archivo \_\_init\_\_.py le indica a Python que esta carpeta debe ser tratada como un paquete distribuible.



**preprocesamiento.py**: Incluye las funciones destinadas a la limpieza de la imagen, como la conversión a escala de grises y la aplicación de filtros Gaussianos para eliminar el ruido.

**deteccion.py:** Es el módulo central de análisis. Contiene algoritmos para la detección de bordes (Canny), la identificación de muros (Hough) e intersecciones (Harris).

##### 

##### **3. Carpeta de Recursos (ejemplos/)**

Contiene las imágenes de prueba utilizadas para validar que los algoritmos de visión funcionen correctamente sobre casos de estudio reales.



**Procedimiento de Instalación en Anaconda**



Para asegurar que la librería esté disponible en todo el entorno de trabajo, siga estos pasos desde el Anaconda PowerShell Prompt:



&#x20;***1. Localización del Proyecto***

Debe posicionar la terminal en el directorio donde reside el archivo setup.py ejecutando el siguiente comando:





cd "C:**<i>~~Colocar aquí la dirección de la carpeta~~</i>**"



&#x20;***2. Instalación del Paquete***

Ejecute el gestor de paquetes pip apuntando al directorio actual (representado por el punto .). Esto lee el archivo setup.py e instala la librería en el entorno activo.



&#x20;  **pip install .**



***3. Verificación de la Instalación***

Puede confirmar que el proceso fue exitoso consultando la información del paquete:



&#x20;**pip show vision\_planos**





