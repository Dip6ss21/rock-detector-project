from ultralytics import YOLO
import cv2

# Load a pre-trained YOLOv8 model (you can fine-tune this later)
model = YOLO("yolov8n.pt")  # "n" = nano version (fast & small)

# Load your image
img = cv2.imread("boulder.jpg.")

# Run YOLO detection
results = model(img)

# Draw results on the image
annotated_frame = results[0].plot()

# Show the result
cv2.imshow("Detected Rocks", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
