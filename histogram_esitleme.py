import cv2
from matplotlib import pyplot as plt

image_path = 'image.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme
equ = cv2.equalizeHist(img)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equ, cmap='gray', vmin=0, vmax=255)
plt.title('Histogram Eşitleme Uygulanan Görüntü')
plt.axis('off')

plt.show()
