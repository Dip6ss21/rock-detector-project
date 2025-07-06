import cv2

# Load the image
image = cv2.imread('rock.jpg.png')  # Image file should be in the same folder
if image is None:
    print("Image not found. Check the filename.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Show images
cv2.imshow("Original", image)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
