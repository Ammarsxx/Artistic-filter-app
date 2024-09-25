import cv2
import numpy as np

#initialize webcam
cap = cv2.VideoCapture(0)

def sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def cartoonify(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def edge_detection(image):
    edges = cv2.Canny(image, 100, 200)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

#Set the default filter
filter_type = 'normal'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Apply filter based on user input
    if filter_type == 'sketch':
        frame = sketch(frame)
    elif filter_type == 'cartoon':
        frame = cartoonify(frame)
    elif filter_type == 'edge':
        frame = edge_detection(frame)

    #Show the live feed
    cv2.imshow('Artistic Filter App', frame)

    #Press keys to change filters or quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        filter_type = 'sketch'
    elif key == ord('c'):
        filter_type = 'cartoon'
    elif key == ord('e'):
        filter_type = 'edge'
    elif key == ord('n'):
        filter_type = 'normal'

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows() 