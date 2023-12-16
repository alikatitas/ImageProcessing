import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import median_filter

def add_salt_and_pepper_noise(img, amount=0.05):
    # Salt and pepper gürültüsü ekleyen fonksiyon
    noisy_img = np.copy(img)
    # Tuz (beyaz) gürültüsü
    num_salt = np.ceil(amount * img.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
    noisy_img[coords[0], coords[1]] = 1

    # Karabiber (siyah) gürültüsü
    num_pepper = np.ceil(amount * img.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
    noisy_img[coords[0], coords[1]] = 0

    return noisy_img

def apply_median_filter(img, size=3):
    # Medyan filtresi uygulama
    return median_filter(img, size=size)

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme
if img.ndim == 3:
    img = np.mean(img, axis=2)

# Salt and pepper gürültüsü ekleme
noisy_img = add_salt_and_pepper_noise(img, amount=0.05)

# Medyan filtresi uygulama
median_filtered_img = apply_median_filter(noisy_img, size=3)

# Sonuçları gösterme
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_img, cmap='gray', vmin=0, vmax=150)
plt.title('Salt and Pepper Gürültüsü Eklenmiş Görüntü')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(median_filtered_img, cmap='gray', vmin=0, vmax=150)
plt.title('Medyan Filtre Uygulanan Görüntü')
plt.axis('off')

plt.show()
