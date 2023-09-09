import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(rgb, scaleFactor=1.8, minNeighbors=3)

    for (x, y, w, h) in faces:
        color = (123, 2, 252) # in BGR
        stroke = 2
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, stroke)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

#Press ESC to exit
cap.release()
cv2.destroyAllWindows()
