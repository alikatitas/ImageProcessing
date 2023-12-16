import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import binary_opening, binary_closing, generate_binary_structure

def apply_opening(img, structure):
    # Açma işlemi
    return binary_opening(img, structure=structure)

def apply_closing(img, structure):
    # Kapama işlemi
    return binary_closing(img, structure=structure)

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Eğer görüntü RGB ise, gri tonlamaya çevirme ve ikili (binary) forma getirme
if img.ndim == 3:
    img = np.mean(img, axis=2)
img_binary = img > 128  # İkili eşikleme

# Yapılandırma elemanı oluşturma
structure = generate_binary_structure(2, 1)

# Açma ve Kapama uygulama
opened_img = apply_opening(img_binary, structure)
closed_img = apply_closing(img_binary, structure)

# Sonuçları gösterme
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img_binary, cmap='gray')
plt.title('Orijinal İkili Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(opened_img, cmap='gray')
plt.title('Açma Uygulanan Görüntü')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(closed_img, cmap='gray')
plt.title('Kapama Uygulanan Görüntü')
plt.axis('off')

plt.show()

