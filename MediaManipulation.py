import cv2
from collections import Counter
from module import findnameoflandmark, findpostion
import subprocess
import pyautogui  # Added library for keyboard shortcuts

cap = cv2.VideoCapture(0)
tip = [8, 12, 16, 20]
tipname = [8, 12, 16, 20]
fingers = []
finger = []

while True:
    ret, frame = cap.read()
    frame1 = cv2.resize(frame, (640, 480))

    a = findpostion(frame1)
    b = findnameoflandmark(frame1)

    if len(b and a) != 0:
        finger = []
        if a[0][1:] < a[4][1:]:
            finger.append(1)
            print(b[4])

    else:
        finger.append(0)

    fingers = []
    for id in range(0, 4):
        if a[tip[id]][2:] < a[tip[id] - 2][2:]:
            print(b[tipname[id]])
            fingers.append(1)
        else:
            fingers.append(0)

    x = fingers + finger
    c = Counter(x)
    up = c[1]
    down = c[0]
    print(up)
    print(down)

    cv2.imshow("Frame", frame1)
    key = cv2.waitKey(1) & 0xFF

    # Control YouTube video with keyboard shortcuts
    if up == 4:
        # Press right key to skip forward the video
        pyautogui.press("right")

    if up == 3:
        # Press left key to skip back the video
        pyautogui.press("left")

    if up == 2:
        # Decrease volume using down arrow key
        pyautogui.press("down")

    if up == 1:
        # Increase volume using up arrow key
        pyautogui.press("up")

    if key == ord("s"):
        break
