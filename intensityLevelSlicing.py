import cv2
import numpy as np

#? Dosyadan resmi okuyup resim değişkenine atıyoruz ve boyutu 0 olarak belirterek gri tonlama yapıyoruz
resim = cv2.imread("image.jpg",0)

#? Resmin en ve boyunu buluyoruz
row, column = resim.shape

#? Dilimlenmiş görüntüyü depolamak için numpy kütüphanesini kullanarak sıfır dizisi oluşturuyoruz
resimYeni = np.zeros((row,column), dtype='uint8')

#? Max ve min aralığı belirliyoruz
minRange=5
maxRange=25

#! Giriş görüntüsü üzerinde döngü yapılarak piksel değeri istenen aralıktaysa 255'e ayarlandı, DEĞİLSE 0'a ayarlandı

for i in range(row):
    for j in range(column):
        if resim[i,j]>minRange and resim[i,j]<maxRange:
            resimYeni[i,j] = 255
        else:
            resimYeni[i,j] = 0
            
# Resmin son hali gösteriliyor
cv2.imshow('Dilimlenen Resim', resimYeni)

cv2.waitKey(0)
cv2.destroyAllWindows()


