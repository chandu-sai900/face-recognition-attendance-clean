import cv2
import os
import numpy as np
from datetime import datetime

dataset_path = "dataset"

faces = []
labels = []
label_map = {}
current_label = 0

# =========================
# LOAD DATASET
# =========================
for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_folder):
        continue

    label_map[current_label] = person_name

    for image_name in os.listdir(person_folder):

        img_path = os.path.join(person_folder, image_name)

        img = cv2.imread(img_path, 0)

        if img is not None:

            # Resize all training images
            img = cv2.resize(img, (200, 200))

            faces.append(img)
            labels.append(current_label)

    current_label += 1

print("Dataset loaded!")

faces = np.array(faces)
labels = np.array(labels)

# =========================
# TRAIN MODEL
# =========================
model = cv2.face.LBPHFaceRecognizer_create()
model.train(faces, labels)

print("Model trained!")

# =========================
# ATTENDANCE FUNCTION
# =========================
def mark_attendance(name):

    file_exists = os.path.isfile("attendance.csv")

    with open("attendance.csv", "a") as f:

        if not file_exists:
            f.write("Name,Time\n")

        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")

        f.write(f"{name},{time_str}\n")


# =========================
# FACE DETECTOR
# =========================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# =========================
# START CAMERA
# =========================
cap = cv2.VideoCapture(0)

print("Camera opened:", cap.isOpened())

marked = set()

# =========================
# MAIN LOOP
# =========================
while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_detected = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces_detected:

        # Crop face
        face_img = gray[y:y+h, x:x+w]

        # Resize to match training size
        face_img = cv2.resize(face_img, (200, 200))

        # Predict
        label, confidence = model.predict(face_img)

        print("Confidence:", confidence)

        # LOWER confidence = better match
        if confidence < 120:
            name = label_map[label]
        else:
            name = "Unknown"

        # Mark attendance only once
        if name != "Unknown" and name not in marked:
            mark_attendance(name)
            marked.add(name)

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Show name
        cv2.putText(
            frame,
            f"{name}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # Show window
    cv2.imshow("Face Recognition Attendance System", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# =========================
# RELEASE
# =========================
cap.release()
cv2.destroyAllWindows()
