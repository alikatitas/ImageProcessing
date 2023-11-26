import numpy as np
import cv2
#? Resmi gri şekilde okuyoruz
resim = cv2.imread('image.jpg',0)

#? Her piksel üzerinde yineleme yaparak np.binary_repr() işlevini kullanarak piksel değerini ikili olarak değiştirip bir listedede tutuyoruz
lst = []
for i in range(resim.shape[0]):
    for j in range(resim.shape[1]):
         lst.append(np.binary_repr(resim[i][j] ,width=8))

#? Her dizenin ikili piksel değerini temsil ettiği bir dize listemiz var. Bit düzlemlerini çıkarmak için dizeler üzerinde yinelememiz ve bit düzlemlerine karşılık gelen karakterleri listelerde saklamamız gerekir.
#! 2^(n-1) ile çarparak bit görüntüsünü yeniden oluşturmak için yeniden şekillendiriyoruz : 
eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(resim.shape[0],resim.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(resim.shape[0],resim.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(resim.shape[0],resim.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(resim.shape[0],resim.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(resim.shape[0],resim.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(resim.shape[0],resim.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(resim.shape[0],resim.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(resim.shape[0],resim.shape[1])

#? Görüntüleme kolaylığı için cv2.hconcat() kullanarak bu görüntüleri birleştiriyoruz
finalr = cv2.hconcat([eight_bit_img,seven_bit_img,six_bit_img,five_bit_img])
finalv =cv2.hconcat([four_bit_img,three_bit_img,two_bit_img,one_bit_img])

#? Dikey olarak birleştiriyoruz
final = cv2.vconcat([finalr,finalv])

#? Resmi gösteriyoruz
cv2.imshow('Resim',final)
cv2.waitKey(0) 