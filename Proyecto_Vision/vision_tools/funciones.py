import cv2
import numpy as np
import matplotlib.pyplot as plt

def preparar_imagen(ruta_imagen):
    """Carga la imagen y devuelve la versión RGB y Gris."""
    img = cv2.imread(ruta_imagen)
    if img is None:
        return None, None, None
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, img_rgb, gris

def obtener_mascara_muros(gris, k_size=6, b_size=5):
    """Procesa la imagen gris para obtener la máscara de muros."""
    desenfocado = cv2.GaussianBlur(gris, (b_size, b_size), 0)
    
    binaria = cv2.adaptiveThreshold(
        desenfocado, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    )

    kernel = np.ones((k_size, k_size), np.uint8)
    muros_limpios = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)
    return muros_limpios

def detectar_detalles(img_rgb, muros_limpios, l_thresh=40):
    """Dibuja líneas y esquinas sobre la imagen y la devuelve."""
    resultado = img_rgb.copy()

    # Líneas
    lineas = cv2.HoughLinesP(muros_limpios, 1, np.pi/180, l_thresh, minLineLength=10, maxLineGap=10)
    if lineas is not None:
        for l in lineas:
            x1, y1, x2, y2 = l[0]
            cv2.line(resultado, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Esquinas
    muros_float = np.float32(muros_limpios)
    esquinas = cv2.cornerHarris(muros_float, 2, 3, 0.04)
    esquinas = cv2.dilate(esquinas, None)
    resultado[esquinas > 0.01 * esquinas.max()] = [255, 0, 0]
    
    return resultado

def mostrar(gris, mascara, final):
    """Muestra la comparativa de imágenes."""
    plt.figure(figsize=(15, 8))
    imagenes = [gris, mascara, final]
    titulos = ["Gris", "Máscara", "Resultado"]
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(imagenes[i], cmap='gray' if i < 2 else None)
        plt.title(titulos[i])
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()