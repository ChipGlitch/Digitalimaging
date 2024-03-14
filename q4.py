import cv2

image = cv2.imread("C:\\Users\\User\\Pictures\\Saved Pictures\\stowe_dest_34.jpeg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(image)

# Blue channel
b_img = image.copy()
b_img[:, :, 1] = 0  # Set green channel to 0
b_img[:, :, 2] = 0  # Set red channel to 0
cv2.imshow('B-RGB', b_img)
cv2.waitKey(0)

# Green channel
g_img = image.copy()
g_img[:, :, 0] = 0  # Set blue channel to 0
g_img[:, :, 2] = 0  # Set red channel to 0
cv2.imshow('G-RGB', g_img)
cv2.waitKey(0)

# Red channel
r_img = image.copy()
r_img[:, :, 0] = 0  # Set blue channel to 0
r_img[:, :, 1] = 0  # Set green channel to 0
cv2.imshow('R-RGB', r_img)
cv2.waitKey(0)

# Merge comparison
merged_img = cv2.merge((b, g, r))
cv2.imshow("RGB_Image", merged_img)
cv2.waitKey(0)

# Red and blue channel
rb_img = image.copy()
rb_img[:, :, 1] = 0  # Set green channel to 0
cv2.imshow('RB_Image', rb_img)
cv2.waitKey(0)

# Merge (r,r,r)
rrr_img = cv2.merge((r, r, r))
cv2.imshow('Red_Merge_Image', rrr_img)
cv2.waitKey(0)
