import cv2
import numpy as np
def limpiar_imagen(img):
    # Conversión a gris y suavizado Gaussiano[cite: 2]
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gris, (5, 5), 0) # El kernel de 5x5 que usas en clase[cite: 2]
    return blur
