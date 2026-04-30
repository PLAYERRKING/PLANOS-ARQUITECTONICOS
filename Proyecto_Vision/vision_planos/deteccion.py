import cv2
import numpy as np

def extraer_formas(img_gris):
    # 1. Detección de bordes con Canny
    bordes = cv2.Canny(img_gris, 50, 150)
    
    # 2. Transformada de Hough para líneas de muros
    lineas = cv2.HoughLinesP(bordes, 1, np.pi/180, 50, minLineLength=30, maxLineGap=5)
    
    # 3. Detector de Harris para intersecciones
    gris_32 = np.float32(img_gris)
    esquinas = cv2.cornerHarris(gris_32, 2, 3, 0.04)
    
    return lineas, esquinas, bordes

def marcar_elementos(img_original, lineas, esquinas):
    """
    Función para dibujar los muros (líneas) y esquinas detectadas sobre la imagen.
    """
    img_marcada = img_original.copy()
    
    # Dibujar líneas de muros en verde
    if lineas is not None:
        for l in lineas:
            x1, y1, x2, y2 = l[0]
            cv2.line(img_marcada, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
    # Dibujar intersecciones en rojo
    esquinas_visibles = cv2.dilate(esquinas, None)
    img_marcada[esquinas_visibles > 0.01 * esquinas_visibles.max()] = [0, 0, 255]
    
    return img_marcada
