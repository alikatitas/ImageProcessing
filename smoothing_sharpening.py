import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter, convolve

def apply_smoothing(img, sigma):
    # Gaussian blurring (smoothing) uygulama
    return gaussian_filter(img, sigma=sigma)

def apply_sharpening(img, alpha=1.5):
    # Keskinleştirme için bir kernel tanımlama
    sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # Convolve işlemi uygulayarak keskinleştirme
    return convolve(img, sharpening_kernel) * alpha

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Smoothing ve sharpening uygulama
smoothed_img = apply_smoothing(img, sigma=1.5)
sharpened_img = apply_sharpening(smoothed_img, alpha=1.5)

# Sonuçları gösterme
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(smoothed_img, cmap='gray', vmin=0, vmax=255)
plt.title('Smoothing Uygulanan Görüntü')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sharpened_img, cmap='gray', vmin=0, vmax=255)
plt.title('Sharpening Uygulanan Görüntü')
plt.axis('off')

plt.show()
