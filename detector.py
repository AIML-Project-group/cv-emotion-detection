from keras.models import load_model
from pathlib import Path
import numpy as np
import cv2

model_file = Path(__file__).parent / 'model/emotion-detector.h5'

model = load_model(model_file)

emotion_dict = { 0: 'angry', 1: 'disgusted', 2: 'fearful', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprised' }

def predict(file_path):
    image = cv2.imread(file_path)
    img = image.copy()
    facehaar = cv2.CascadeClassifier('face.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facehaar.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        print('No faces detected')
        return img

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]

        cropped_image = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = model.predict(cropped_image)

        max_index = int(np.argmax(prediction))
        cv2.putText(img, emotion_dict[max_index], (x + 50, y + h - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    return img
