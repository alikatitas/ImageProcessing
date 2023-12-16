import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import sobel

def apply_sobel_filter(img, axis):
    # Sobel filtresi uygulama
    sobel_filtered_img = sobel(img, axis=axis)
    return sobel_filtered_img

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Sobel filtresi uygulama (yatay ve dikey)
sobel_x = apply_sobel_filter(img, axis=0)
sobel_y = apply_sobel_filter(img, axis=1)

# Sonuçları gösterme
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel Filtresi - Yatay')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel Filtresi - Dikey')
plt.axis('off')

plt.show()
