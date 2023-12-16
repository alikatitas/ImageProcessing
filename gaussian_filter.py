import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter

def apply_gaussian_filter(img, sigma):
    # Gaussian filtresi uygulama
    filtered_img = gaussian_filter(img, sigma=sigma)
    return filtered_img

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Gaussian filtresi uygulama (örnek olarak sigma = 3.0)
gaussian_filtered_img = apply_gaussian_filter(img, sigma=3.0)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gaussian_filtered_img, cmap='gray', vmin=0, vmax=255)
plt.title('Gaussian Filtre Uygulanan Görüntü')
plt.axis('off')

plt.show()
