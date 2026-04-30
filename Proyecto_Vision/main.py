import cv2
import matplotlib.pyplot as plt
from vision_planos import preprocesamiento as prep
from vision_planos import deteccion as det
# Cargar tu imagen de prueba (reemplaza la ruta si es necesario)
ruta = r"C:\Users\leona\OneDrive\Desktop\Proyecto_Vision\ejemplos\prueba 1.jpg"
img = cv2.imread(ruta)
if img is not None:
    # 1. Procesamiento
    gris = prep.limpiar_imagen(img)
    lineas, esquinas, bordes = det.extraer_formas(gris)
    # 2. Generar imagen con los muros y esquinas marcados
    # Esta es la función que añadimos a tu librería
    resultado_final = det.marcar_elementos(img, lineas, esquinas)
    # 3. Mostrar las imágenes en una comparativa
    plt.figure(figsize=(18, 6))
    # Mostrar Original
    plt.subplot(1, 3, 1),plt.title("Imagen Original"),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)),plt.axis('off')
    # Mostrar Bordes (Canny)
    plt.subplot(1, 3, 2),plt.title("Bordes (Canny)"),plt.imshow(bordes, cmap='gray'),plt.axis('off')
    # Mostrar Resultado Final
    plt.subplot(1, 3, 3),plt.title("Detección Final (Hough + Harris)"),plt.imshow(cv2.cvtColor(resultado_final, cv2.COLOR_BGR2RGB)),plt.axis('off')
    plt.tight_layout()
    plt.show()
    print("¡Librería instalada y funcionando correctamente!")
    print(f"Líneas detectadas: {len(lineas) if lineas is not None else 0}")
else:
    print(f"No se encontró la imagen en la ruta: {ruta}")
