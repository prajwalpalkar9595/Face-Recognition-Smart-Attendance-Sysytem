import cv2
import numpy as np
import os
import face_recognition
from datetime import datetime

# Step 1: Load known face encodings and their corresponding names
def load_known_faces(known_faces_dir):
    known_encodings = []
    known_names = []

    for filename in os.listdir(known_faces_dir):
        if filename.endswith(('.jpg', '.png')):
            filepath = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(filepath)
            encoding = face_recognition.face_encodings(image)[0]
            known_encodings.append(encoding)
            known_names.append(os.path.splitext(filename)[0])

    return known_encodings, known_names

# Step 2: Mark attendance by writing the name and time to a CSV file
def mark_attendance(name):
    with open('attendance.csv', 'r+') as file:
        lines = file.readlines()
        attendance_list = [line.split(',')[0] for line in lines]

        if name not in attendance_list:
            now = datetime.now()
            timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'{name},{timestamp}\n')

# Step 3: Real-time face recognition and attendance marking
def main():
    known_faces_dir = 'known_faces'
    known_encodings, known_names = load_known_faces(known_faces_dir)

    video_capture = cv2.VideoCapture(0)  # Use 0 for webcam

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert the frame to RGB for face_recognition processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)

            if matches:
                best_match_index = np.argmin(face_distances)
                name = known_names[best_match_index]

                # Mark attendance
                mark_attendance(name)

                # Draw a box around the face
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                # Display the name below the face
                cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow('Face Recognition Attendance System', frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
