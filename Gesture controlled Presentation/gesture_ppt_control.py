import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Variables
width, height = 1280, 720
folderPath = "Presentation"
# Camera setup
cap = cv2.VideoCapture(0)  # Use DirectShow backend on Windows

cap.set(3, width)
cap.set(4, height)

# Get the list of Presentation images
pathImages = sorted(os.listdir(folderPath), key=len)

# Variables
imgNumber = 0      
hs, ws = int(120 * 2.5), int(213 * 4)
gestureThreshold = 450
buttonPressed = False
buttonCounter = 0
buttonDelay = 30
annotations = [[]]
annotationNumber = -1  # Start with -1 to avoid index issues
annotationStart = False
slideTimer = 0
showWebcam = True  # Variable to track webcam visibility

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Import images
    success, img = cap.read()
    
    # Check if the frame was captured successfully
    if not success:
        print("Failed to capture image from camera. Retrying...")
        continue  # Skip the rest of the loop and try again

    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    # Resize slide images to fit the full screen size
    imgCurrent = cv2.resize(imgCurrent, (width, height))

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

    if hands and not buttonPressed:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        # Map the index finger (lmList[8]) to the full screen range
        xVal = int(np.interp(lmList[8][0], [0, width], [0, width]))  # Map x to full width range
        yVal = int(np.interp(lmList[8][1], [0, height], [0, height]))  # Map y to full height range

        indexFinger = xVal, yVal  # Pointer position

        # Ensure the pointer moves freely across the screen
        if cy <= gestureThreshold:  # If hand is at the height of the face
            # Gesture 1 - left
            if fingers == [1, 0, 0, 0, 0]:
                if imgNumber > 0:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = -1
                    imgNumber -= 1
            # Gesture 2 - Right
            elif fingers == [0, 0, 0, 0, 1]:
                if imgNumber < len(pathImages) - 1:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = -1
                    imgNumber += 1
            # Gesture 3 - Show Pointer
            elif fingers == [0, 1, 1, 0, 0]:
                annotationStart = False  # Do not start drawing
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)

            # Gesture 4 - Draw pointer
            elif fingers == [0, 1, 0, 0, 0]:
                if not annotationStart:
                    annotationStart = True
                    annotationNumber += 1
                    annotations.append([])
                cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                annotations[annotationNumber].append(indexFinger)
            else:
                annotationStart = False

            # Gesture 5 - Erase (Three fingers: [0, 1, 1, 1, 0])
            if fingers == [0, 1, 1, 1, 0]:
                if annotations:
                    if annotationNumber >= 0:
                        annotations.pop(-1)  # Remove the last annotation
                        annotationNumber -= 1
 # Gesture 6 - Auto Slide (thumb and index finger raised)
            if fingers == [1, 1, 0, 0, 0]:
                slideTimer += 1
                if slideTimer > 6:
                    slideTimer = 0
                    imgNumber = (imgNumber + 1) % len(pathImages)

            # Gesture 7 - Toggle Webcam (all fingers raised)
            if fingers == [1, 1, 1, 1, 1]:
                print("Toggle Webcam")
                showWebcam = not showWebcam  # Toggle the webcam visibility
                buttonPressed = True

    # Button pressed iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    # Draw annotations
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0, 0, 255), 10)

    # Adding webcam images on slides (only if showWebcam is True)
    if showWebcam:
        imgSmall = cv2.resize(img, (ws, hs))
        h, w, _ = imgCurrent.shape
        imgCurrent[0:hs, w - ws: w] = imgSmall

    # Show webcam feed and slides side by side
    cv2.imshow("Webcam Feed", img)
    cv2.imshow("Slides", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()