import time

import autopy
import cv2
import mediapipe as mp
import numpy as np
import pyautogui as pa
import win32gui

import HandTrackingModule as htm

pa.FAILSAFE = False


wcam, hcam = 640, 480
frameR = 100
smo = 9

hwnd = win32gui.FindWindow(None, "AI MOUSE")


pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0


cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

detector = htm.HandDetector(detectionCon=0.5, maxHands=1)


wScr, hScr = autopy.screen.size()
print(f"Screen size: {wScr}x{hScr}")

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)

    if len(lmList) != 0:

        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()
        print(fingers)

        cv2.rectangle(
            img,
            (frameR, frameR - 100),
            (wcam - frameR, hcam - frameR - 100),
            (255, 0, 255),
            2,
        )

        if len(fingers) >= 3 and fingers[1] == 1 and fingers[2] == 0:

            x3 = np.interp(x1, (frameR, wcam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR - 100, hcam - frameR - 100), (0, hScr))

            clocX = plocX + (x3 - plocX) / smo
            clocY = plocY + (y3 - plocY) / smo

            try:
                autopy.mouse.move(wScr - clocX, clocY)
            except ValueError:
                print("Point out of bounds")

            cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        if len(fingers) >= 3 and fingers[1] == 1 and fingers[2] == 1:
            length, img, line = detector.findDistance(8, 12, img)
            if length < 50:
                cv2.circle(img, (line[4], line[5]), 12, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
                time.sleep(0.2)

        if len(fingers) >= 3 and fingers[0] == 1 and fingers[4] == 1:
            pa.rightClick()

        if len(fingers) >= 3 and fingers[4] == 1:
            pa.scroll(-200)

        if len(fingers) >= 3 and fingers[0] == 1:
            pa.scroll(200)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (240, 0, 0), 2
    )

    cv2.imshow("AI MOUSE", img)

    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
