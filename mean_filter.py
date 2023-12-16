import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import uniform_filter

def apply_mean_filter(img, filter_size):
    # Ortalama filtresi uygulama
    filtered_img = uniform_filter(img, size=filter_size)
    return filtered_img

# Görüntüyü yükleme (örnek olarak bir dosya yolu)
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Ortalama filtresi uygulama (örnek olarak filter_size = 10)
mean_filtered_img = apply_mean_filter(img, filter_size=10)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(mean_filtered_img, cmap='gray', vmin=0, vmax=255)
plt.title('Ortalama Filtre Uygulanan Görüntü')
plt.axis('off')

plt.show()
