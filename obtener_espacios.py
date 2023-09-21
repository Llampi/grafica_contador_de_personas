
import cv2
import pickle

# Lee la imagen original
img = cv2.imread('img.png')

# Define las dimensiones deseadas
#840 x 480
nuevo_ancho = 1285
nuevo_alto = 740

# Cambia el tamaño de la imagen a las dimensiones deseadas
img_redimensionada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

alto, ancho, _ = img_redimensionada.shape
#numero total de rectangulos: 40 x 40
num_rectangulos = 40

# Calcula el ancho y alto de cada rectángulo
ancho_rectangulo = ancho // num_rectangulos
alto_rectangulo = alto // num_rectangulos

# Inicializa una lista para almacenar los rectángulos
rectangulos = []

# Itera para crear y dibujar los rectángulos
for i in range(num_rectangulos):
    x1 = i * ancho_rectangulo 
    x2 = x1 + ancho_rectangulo 
    for j in range(num_rectangulos):    
        y1 = j * alto_rectangulo -1
        y2 = y1 + alto_rectangulo -1
    
    # Agrega las coordenadas del rectángulo a la lista
        rectangulos.append((x1, y1, x2, y2))
    
    # Dibuja el rectángulo en la imagen
        cv2.rectangle(img_redimensionada, (x1, y1), (x2, y2), (255, 0, 0), 2)
        coordenadas_texto = f'({x1}, {y1}) - ({x2}, {y2})'
        cv2.putText(img_redimensionada, coordenadas_texto, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

#espacio = cv2.selectROI('espacio', img_redimensionada, False)
# Guarda los espacios en un archivo pickle
with open('espacios.pkl', 'wb') as file:
    pickle.dump(rectangulos, file)
'''

import cv2
import pickle

# Lee la imagen original
img = cv2.imread('img.png')

# Define las dimensiones deseadas
#840 x 480
nuevo_ancho = 1285
nuevo_alto = 740

# Cambia el tamaño de la imagen a las dimensiones deseadas
img_redimensionada = cv2.resize(img, (nuevo_ancho, nuevo_alto))

# Crea una nueva lista para almacenar los espacios
espacios = []

for x in range(10):
    espacio = cv2.selectROI('espacio', img_redimensionada, False)
    cv2.destroyWindow('espacio')
    
    espacios.append(espacio)

    for x, y, w, h in espacios:
        cv2.rectangle(img_redimensionada, (int(x), int(y)), (int(x+w), int(y+h)), (255, 0, 0), 2)

# Guarda los espacios en un archivo pickle
with open('espacios.pkl', 'wb') as file:
    pickle.dump(espacios, file)
    '''