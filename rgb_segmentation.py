import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def segment_image_by_color(img, lower_bound, upper_bound):
    # Belirli bir renk aralığını içeren pikselleri seçme
    mask = np.all(np.logical_and(lower_bound <= img, img <= upper_bound), axis=-1)
    # Seçilen pikselleri içeren bir maske oluşturma
    segmented_img = np.zeros_like(img)
    segmented_img[mask] = img[mask]
    return segmented_img

# Görüntüyü yükleme
image_path = 'image.jpg'
img = mpimg.imread(image_path)

# Belirli bir renk aralığını tanımlama (örnek olarak mavi tonları)
lower_bound = np.array([10, 10, 5])  # Düşük mavi eşik değeri
upper_bound = np.array([200, 110, 150])  # Yüksek mavi eşik değeri

# Görüntüyü belirli renk aralığına göre bölütlenme
segmented_img = segment_image_by_color(img, lower_bound, upper_bound)

# Sonuçları gösterme
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_img)
plt.title('Bölütlenmiş Görüntü')
plt.axis('off')

plt.show()
