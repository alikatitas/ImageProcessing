import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter

def apply_gaussian_blur(img, sigma):
    # Gaussian blurring uygulama
    blurred_img = gaussian_filter(img, sigma=sigma)
    return blurred_img

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Gaussian blurring uygulama (örnek olarak sigma = 1.5)
gaussian_blurred_img = apply_gaussian_blur(img, sigma=1.5)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gaussian_blurred_img, cmap='gray', vmin=0, vmax=255)
plt.title('Gaussian Blurring Uygulanan Görüntü')
plt.axis('off')

plt.show()
