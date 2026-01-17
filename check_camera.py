import cv2

cap = cv2.VideoCapture(0)  # Try 1 or 2 if you have more cameras

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Get the resolution
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Camera resolution: {int(width)} x {int(height)}")

cap.release()
