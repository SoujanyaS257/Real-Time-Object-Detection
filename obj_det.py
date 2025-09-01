import cv2
from cvlib.object_detection import draw_bbox
import cvlib as cv
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
spoken = set()  # To avoid repeating the same object

# Start webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    
while webcam.isOpened():
    status, frame = webcam.read()
    if not status:
        break

    # Detect common objects in the frame
    bbox, label, conf = cv.detect_common_objects(frame)

    # Draw bounding box
    output_image = draw_bbox(frame, bbox, label, conf)

    # Show detected labels
    for obj in label:
        if obj not in spoken:
            print(f"Detected object: {obj}")
            engine.say(obj)
            engine.runAndWait()
            spoken.add(obj)

    cv2.imshow("Real-time object detection", output_image)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
