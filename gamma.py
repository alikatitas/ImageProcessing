import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def apply_gamma_correction(img, gamma):
    # Gamma düzeltmesi uygulama
    corrected_img = np.power(img / 255.0, gamma) * 255.0
    # Değerlerin 0-255 aralığında olmasını sağlama
    corrected_img = np.clip(corrected_img, 0, 255).astype(np.uint8)
    return corrected_img

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Gamma düzeltmesi uygulama (örnek olarak gamma = 2.2)
gamma_corrected_img = apply_gamma_correction(img, gamma=2.2)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gamma_corrected_img, cmap='gray', vmin=0, vmax=255)
plt.title('Gamma Düzeltme Uygulanan Görüntü')
plt.axis('off')

plt.show()
