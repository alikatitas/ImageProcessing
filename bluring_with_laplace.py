import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter, laplace

def apply_blur_and_laplace(img, sigma):
    # Gaussian blurring uygulama
    blurred_img = gaussian_filter(img, sigma=sigma)
    # Laplace filtresi uygulama
    laplace_img = laplace(blurred_img)
    return laplace_img

# Görüntüyü yükleme (örnek olarak bir dosya yolu)
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Blurring ve Laplace filtresi uygulama (örnek olarak sigma = 1.5)
laplace_img = apply_blur_and_laplace(img, sigma=1.5)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(laplace_img, cmap='gray')
plt.title('Blurring ve Laplace Filtresi Uygulanan Görüntü')
plt.axis('off')

plt.show()
