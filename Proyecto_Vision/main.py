import vision_tools as vt

# 1. Cargar
ruta = r"C:\Users\leona\OneDrive\Documentos\vision proyecto 2\imagenes\prueba 9.jpg"
original, rgb, gris = vt.preparar_imagen(ruta)

if original is not None:
    # 2. Procesar (Pasamos 'gris', obtenemos 'mascara')
    mascara = vt.obtener_mascara_muros(gris)

    # 3. Detectar (Pasamos 'rgb' y 'mascara', obtenemos 'final')
    final = vt.detectar_detalles(rgb, mascara)

    # 4. Visualizar
    vt.mostrar(gris, mascara, final)
else:
    print("Error: No se encontró la imagen.")