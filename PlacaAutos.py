import cv2
from cv2 import Canny
from matplotlib.pyplot import gray
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Usuario\AppData\Local\Programs\Tesseract-OCR\tesseract'

placa = []
image = cv2.imread('Cars239.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # se cambia la imagen a escala de grises
gray = cv2.blur(gray,(3,3))
canny = cv2.Canny(gray,150,200) # Para dibujar los contornos de la imagen
canny = cv2.dilate(canny,None,iterations=1) # Pare engrosar las areas blancas

cnts,_ = cv2.findContours(canny,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #Obtener los contornos de la imagen
# Dibujar los contornos del auto
#cv2.drawContours(image,cnts,-1,(0,255,0)) 

for j in cnts:
    area = cv2.contourArea(j)
    x,y,w,h = cv2.boundingRect(j)
    epsilon = 0.02*cv2.arcLength(j,True)
    approx = cv2.approxPolyDP(j, epsilon, True)
    if len(approx)==4 and area > 2000:
        print('area=', area)
        aspect_ratio = float(w)/h
        if aspect_ratio>2.4:
            placa = gray[y:y+h,x:x+w]
            text = pytesseract.image_to_string(placa, config= '--psm 11')
            print('text=', text)
            cv2.imshow('placa', placa)
            cv2.moveWindow('placa', 780,10)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0),3)
            cv2.putText(image,text,(x-20,y-5),1,2,3,(0))
       # cv2.drawContours(image,[j],0,(0,255,0),2) 
cv2.imshow('Image',image)
#cv2.imshow('Canny',canny)
cv2.moveWindow('Image', 45,10)
cv2.waitKey(0)