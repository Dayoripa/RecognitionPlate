from ast import Break
from audioop import reverse
import cv2
from cv2 import FILLED
import numpy as np
from cv2 import Canny
import pytesseract
from PIL import Image

# se importa el video
cap = cv2.VideoCapture("video.mp4")

Ctexto = ''                 
while True:
    #Realiza la lectura de la videoCaptura
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    # Dibujamos un rectangulo
    cv2.rectangle(frame, (750, 190), (550, 240), (255, 0, 0), cv2.FILLED)
    cv2.putText(frame, Ctexto[0:7], (590, 225), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    bandera = True
    placas = Ctexto[0:7]
    
    if(placas == 'IPY 428'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Pepito perez', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)   
    elif(placas == 'HZS 810'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Teofila Mina', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)
    elif(placas == 'KVN 289'):
         cv2.rectangle(frame, (695, 480), (425, 520), (0, 0, 255), cv2.FILLED)
         cv2.putText(frame, 'Vehiculo no registrado', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
    elif(placas == 'CUN 160'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Fulanito Diaz', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)
    elif(placas == 'CUR 984'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Elenena', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)
    elif(placas == 'CUN-160'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'paquito Moreno', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)
    elif(placas == 'HDY 778'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Teresa Caicedo ', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Saliendo / pagar: $10.000', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 0, 255), 2)
    elif(placas == 'EHY 392'):
        cv2.rectangle(frame, (695, 480), (425, 520), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, 'Vehiculo no registrado', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)
    elif(placas == 'ENV 570'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Liliana Cabezas', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Saliendo / pagar: $10.000', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0, 0, 255), 2)
    elif(placas == 'HPT 699'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Martin Sanchez', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)
    elif(placas == 'JZR 933'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Diego Flores', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)
    elif(placas == 'DIV 402'):
        cv2.rectangle(frame, (640, 480), (425, 520), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, 'Gina Arce', (427, 507), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255), 2)
        cv2.putText(frame, 'Ingresando...', (430, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255, 255, 255), 2)

    # Extraemos el ancho y alto de los fotogramas
    al, an, c = frame.shape
    
    # Tomar el centro de la imagen
    #En x
    x1 = int(an / 3) # Tomamos 1/3 de la imagen
    x2 = int(x1 * 2) #Hasta el inicio del 3/3 de la imagen"
    
    # En y
    y1 = int (al / 3) # Tomamos 1/3 de la imagen
    y2 = int (y1 * 2) #Hasta el inicio del 3/3 de la imagen"
    
    # ubicamos el rectangulo en las zonas extraidas
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    # Realizamos un recorte a nuestra zonas de inters
    recorte = frame[y1:y2, x1:x2]

    # Preprocesamiento de la zona de interes
    mB = np.matrix(recorte[:, :, 0])
    mG = np.matrix(recorte[:, :, 1])
    mR = np.matrix(recorte[:, :, 2])
    
    
    # color
    Color = cv2.absdiff(mG, mB)
    
    # Binarizamos la imagen
    _, umbral = cv2.threshold(Color, 40, 255, cv2.THRESH_BINARY)
    
    # eXTRAEMOS LOS CONTORNOS
    contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Primero los ordenamos de la zona seleccionada
    contornos = sorted(contornos, key=lambda x: cv2.contourArea(x), reverse = True)
    
    # Dibujamos los contornos extraidos
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 500 and area < 5000:
            #Detectamos la placa
            x, y, ancho, alto = cv2.boundingRect(contorno)
            
            # Extraemos las coordenadas
            xpi = x + x1 # Coordenadas de la placa en X inicial
            ypi = y + y1 # Coordenadas de la  placa en Y inicial
            
            xpf = x + ancho + x1  # Coordenadas de la placa en X final
            ypf = y + alto + y1 # Coordenadas de la placa en y final
            
            # Dibujamos el rectangulo
            cv2.rectangle(frame, (xpi, ypi), (xpf, ypf), (0, 255, 0), 2)
            
            #Extraemos los pixeles
            placa = frame[ypi:ypf, xpi:xpf]
            
            # Extraemos el ancho y el alto de los fotogramas
            alp, anp, cp = placa.shape
            #print(alp, anp)
            
            # Procesamos los pixles para extraer los valores de las placas
            Mva = np.zeros((alp, anp))
            
            # Normalizamos las matrices
            mBp = np.matrix(placa[:, :, 0])
            mGp = np.matrix(placa[:, :, 1])
            mRp = np.matrix(placa[:, :, 2])
            
            # creamos una mascara
            for col in range(0, alp):
                for fil in range(0, anp):
                    Max = max(mRp[col, fil], mGp[col, fil] ,mBp[col, fil])
                    Mva[col, fil] = 255 - Max
            
            
            # Binarizamos la imagen
            _, bin = cv2.threshold(Mva, 150, 255, cv2.THRESH_BINARY)
            
            #cONVERTIMOS LA MATRIZ EN IMAGEN
            bin = bin.reshape(alp, anp)
            bin = Image.fromarray(bin)
            bin = bin.convert("L")
            
            # Nos aseguramos de tener un buen tamaño de la placa
            if alp >= 36 and anp >=82:
                
                # Declaramos la direccion de Pytesseract
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                
                # Extraemos el texto
                config = "--psm 1"
                texto = pytesseract.image_to_string(bin, config=config)
                # If para no mostrar basura
                if len(texto) >= 7:
                    #print(texto[0:7])
                    
                    Ctexto = texto
                    
                    ## Mostramos los valores que nos interesa
                    # cv2.putText(frame, Ctexto[0:7], (910, 810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            break
                
            # Mostramos el reporte
            #cv2.imshow("Recorte", bin)
                
    #Mostramos el recorte en gris
    cv2.imshow("Vehiculos", frame)
     
    # Leemos una tecla
    t = cv2.waitKey(1)
    
    if t == 27:
        break
cap.release()
cv2.destroyAllWindows()
            
                
            
            
            