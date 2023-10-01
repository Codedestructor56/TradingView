import cv2
import pytesseract
import time
# Load the image
image_path = "new_option.png"
image = cv2.imread(image_path)

# Resize the image to a reasonable size (e.g., 800x600)
height, width = image.shape[:2]
new_height = 400
new_width = int((new_height / height) * width)
resized_image = cv2.resize(image, (400, new_height))

# Convert the resized image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to create a binary image
# You can adjust blockSize and C values as needed
binary_image = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)
cv2.imshow("adaptive",binary_image)
time.sleep(5)
# Perform OCR on the binary image
text = pytesseract.image_to_string(gray_image)

# Print the extracted text
print("Extracted Text:")
print(text)
