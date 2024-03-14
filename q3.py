import cv2
from matplotlib import pyplot as plt

# a) Read image and convert to grayscale
image_path = "C:\\Users\\User\\Pictures\\Saved Pictures\\stowe_dest_34.jpeg"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)

# b) Histogram before equalization
plt.figure(figsize=(6, 4))  # Adjusted figure size for a more balanced aspect ratio
plt.hist(gray_image.ravel(), bins=256, range=(0.0, 256.0))
plt.title('Histogram for Grayscale Image')
plt.show()

# c) Grayscale equalized
equalized_image = cv2.equalizeHist(gray_image)
cv2.imshow('Equalized Grayscale Image', equalized_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

# d) Generating the histogram for the equalized image (after equalization)
plt.figure(figsize=(6, 4))
plt.hist(equalized_image.ravel(), bins=256, range=(0.0, 256.0))
plt.title('Histogram for Equalized Image')
plt.show()
