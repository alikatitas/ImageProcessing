import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def contrast_stretching(img, a, b):
    # Görüntünün min ve max değerlerini hesaplama
    min_val = np.min(img)
    max_val = np.max(img)

    # Contrast stretching uygulama
    stretched_img = (img - min_val) / (max_val - min_val) * (b - a) + a

    return stretched_img

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Contrast stretching uygulama
stretched_img = contrast_stretching(img, a=0, b=255)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(stretched_img, cmap='gray', vmin=0, vmax=255)
plt.title('Contrast Stretched Görüntü')
plt.axis('off')

plt.show()
