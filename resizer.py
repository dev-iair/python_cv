# Complete code
import cv2
import os

folder_path = "/mnt/ssd/heidi_service/copyfile/P00000003"
new_width = 1920
new_height = 1080
cnt = 1
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        # Read the image using OpenCV
        img_path = os.path.join(folder_path, file_name)
        img = cv2.imread(img_path)

        # Resize the image
        resized_img = cv2.resize(img, (new_width, new_height))

        # Save the resized image with a new filename
        new_file_name = f"{cnt}.jpg"
        new_img_path = os.path.join(folder_path, new_file_name)
        cv2.imwrite(new_img_path, resized_img)
        cnt += 1