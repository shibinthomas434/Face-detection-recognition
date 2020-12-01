import face_recognition
import numpy as np
import cv2

video_capture=cv2.VideoCapture(0)

admin_image= face_recognition.load_image_file("me.jpg")
admin_face_encoding = face_recognition.face_encodings(admin_image) [0]

known_face_encodings = [
    admin_face_encoding
]
known_face_names = [
    "ADMIN"
]

while True:
    ret, frame = video_capture.read()
    rgb_frame  = frame[:, :, ::-1]

    face_locations= face_recognition.face_locations(rgb_frame)
    face_encodings= face_recognition.face_encodings(rgb_frame, face_locations)

    #loop through each faces in this video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        cv2.rectangle(frame, (left, top), (right,bottom), (0,0,255), 2)
        name = "Unknown"
        
        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        
        cv2.rectangle(frame, (left, bottom -35),(right, bottom),(0,225,0),cv2.FILLED)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame,name, (left+6, bottom -6), font, 1.0, (255,255,255),1)

    cv2.imshow('Video', frame)

    #making the key 'q' for exit
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

