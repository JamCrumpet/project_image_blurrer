
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('dc_metro.png') # imread() reads image file

# slices parts of image
top =       img[ :-20,10:-10]   #[:-2] = bottom two pixels, [1:-1] = sides
left =      img[10:-10, :-20]
right =     img[10:-10,20:  ]
bottom =    img[20:  ,10:-10]   #[2:] = top two pixels, [1:-1] = sides
centre =    img[10:-10,10:-10]  #[1:-1,1:-1] = first and last column + row. edges

def blurrer(img):
    avg_img = (top + left + right + bottom + centre) / 5.00
    return avg_img


avg_img = blurrer(img)

plt.figure()
# Set colormap so that images are plotted in gray scale.
plt.gray()
# Plot the original image first
plt.subplot(1,3,1)
plt.imshow(img)
plt.title('original')

# Now the filtered image.
plt.subplot(1,3,2)
plt.imshow(avg_img)
plt.title('Blurred')

# compares difference
plt.subplot(1,3,3)
plt.imshow(img[10:-10,10:-10] - avg_img)
plt.title('difference')


plt.show()