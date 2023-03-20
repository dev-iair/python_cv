import cv2

# Load the JPEG image and the PNG image with transparency
jpeg_image = cv2.imread('./input.jpg')
png_image = cv2.imread('/logo.png', cv2.IMREAD_UNCHANGED)

# RESIZE OR CROP
# png_image_resized = cv2.resize(png_image, (jpeg_image.shape[1], jpeg_image.shape[0]))
png_image_crop = png_image[0:jpeg_image.shape[0],0:jpeg_image.shape[1]]

b, g, r, a = cv2.split(png_image_crop)
rgba = cv2.merge((b, g, r))
alpha = cv2.merge((a, a, a))

blended_image = cv2.addWeighted(jpeg_image, 1, alpha, 0.3, 0)

cv2.imwrite('./output.png', blended_image)