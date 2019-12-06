import cv2
import numpy as np

def nothing(x): #nothing isminde x parametreli bir fonksiyon
    pass



cv2.namedWindow("Uygulama") #windows penceresinin ismi
cv2.createTrackbar("LH", "Uygulama", 0, 255, nothing) #kırmızı-yeşil-mavi
cv2.createTrackbar("LS", "Uygulama", 0, 255, nothing)# beyaz alanlar
cv2.createTrackbar("LV", "Uygulama", 0, 255, nothing)#Siyah alanlar
cv2.createTrackbar("UH", "Uygulama", 255, 255, nothing)#mabi-yeşil-kırmızı
cv2.createTrackbar("US", "Uygulama", 255, 255, nothing)#rgb siler
cv2.createTrackbar("UV", "Uygulama", 255, 255, nothing)#siyah renkler hariç siler

while True:
    frame = cv2.imread('test2.jpg')

    #HSV (Hue, Saturation, Value) (Ton, Doygunluk, Değer)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#Secilen görüntüyü griye cevir

    l_h = cv2.getTrackbarPos("LH", "Uygulama")
    l_s = cv2.getTrackbarPos("LS", "Uygulama")
    l_v = cv2.getTrackbarPos("LV", "Uygulama")

    u_h = cv2.getTrackbarPos("UH", "Uygulama")
    u_s = cv2.getTrackbarPos("US", "Uygulama")
    u_v = cv2.getTrackbarPos("UV", "Uygulama")

    dusuk = np.array([l_h, l_s, l_v])
    yuksek = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, dusuk, yuksek)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("orjinal", frame)
    cv2.imshow("ters cevrim(maske)", mask)
    cv2.imshow("renkli alanlar", res)

    key = cv2.waitKey(1)# işlemlerin ekranda sürekli yapılması için
    #if key == 2:
     #   break

#cv2.destroyAllWindows()