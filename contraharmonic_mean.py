import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import generic_filter

def contraharmonic_mean_filter(img, size, Q):
    # Kontraharmonik ortalama filtre fonksiyonu
    def filter_func(values):
        return np.sum(np.power(values, Q + 1)) / np.sum(np.power(values, Q))
    
    return generic_filter(img, filter_func, size=size)

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Kontraharmonik ortalama filtresi uygulama (örnek olarak size=3, Q=1.5)
filtered_img = contraharmonic_mean_filter(img, size=3, Q=1.5)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_img, cmap='gray', vmin=0, vmax=255)
plt.title('Kontraharmonik Ortalama Filtre Uygulanan Görüntü')
plt.axis('off')

plt.show()
