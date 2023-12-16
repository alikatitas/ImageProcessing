import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def normalize(image):
    return (image - np.min(image)) / (np.max(image) - np.min(image))

def standardize(image):
    return (image - np.mean(image)) / np.std(image)

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Görüntüyü normalizasyon ve standardizasyon
normalized_img = normalize(img)
standardized_img = standardize(img)

# Sonuçları gösterme
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(normalized_img)
plt.title('Normalize Edilmiş Görüntü')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(standardized_img)
plt.title('Standardize Edilmiş Görüntü')
plt.axis('off')

plt.show()
