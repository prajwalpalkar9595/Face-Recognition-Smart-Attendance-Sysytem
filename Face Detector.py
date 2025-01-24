import cv2

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture object (0 is the default camera)
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
