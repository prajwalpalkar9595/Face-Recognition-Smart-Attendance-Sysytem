import cv2
import mediapipe as mp

# Initialize video capture (0 is the default camera)
cap = cv2.VideoCapture(0)

# Initialize Mediapipe for pose detection (can be used for recognizing actions)
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize Mediapipe drawing utility to draw pose landmarks
mp_drawing = mp.solutions.drawing_utils

def recognize_moment(pose_landmarks):
    """
    Recognize the action/moment based on pose landmarks.
    This is a placeholder function. Add custom logic here for moment recognition.
    """
    if pose_landmarks:
        # Example: Check if both hands are raised
        left_hand = pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        right_hand = pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

        if left_hand.y < pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y and \
           right_hand.y < pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y:
            return "Hands Raised"
    return "Unknown Action"

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the frame to RGB as Mediapipe requires RGB input
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and detect poses
    results = pose.process(image_rgb)

    # Draw the pose landmarks on the frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Recognize the action or moment
        action = recognize_moment(results.pose_landmarks)
        # Display the recognized moment
        cv2.putText(frame, action, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame with landmarks and recognized moment
    cv2.imshow('Live Moment Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
