# The-Artificial-Mouse

This code implements a hand gesture-based mouse control system using a webcam, OpenCV, MediaPipe, and autopy for controlling the mouse cursor. Here’s a brief overview of how the system works:

Key Features:
Hand Tracking with MediaPipe:
The code utilizes the HandTrackingModule (likely a custom module based on MediaPipe) to detect and track the position of the hand and fingers. MediaPipe is used for detecting and identifying hand landmarks (e.g., finger positions), which are then used for interacting with the computer interface (mouse control).

Mouse Control:

Move Cursor: The position of the index finger (landmark 8) is used to control the mouse cursor. The x and y coordinates of the finger are mapped to the screen resolution to move the cursor in real-time.
Clicking: If the index and middle fingers are both up and close to each other (distance < 50 pixels), a click is simulated using autopy.mouse.click().
Right-click: If the thumb and pinky fingers are both up, the code simulates a right-click using the pyautogui.rightClick() function.
Scrolling: Scrolling is triggered by the presence of the index finger or pinky finger in a specific gesture:
Scroll up with the index finger up (pa.scroll(200)).
Scroll down with the pinky finger up (pa.scroll(-200)).
Dynamic Gesture Handling:

The code continuously checks which fingers are raised (using the fingersUp() method) and performs specific actions based on this.
A rectangle is drawn on the screen to represent the area where hand gestures will be tracked.
A smoothing factor (smo) is applied to prevent the cursor from jumping too erratically by smoothing out the movement between frames.
FPS Display:
It calculates and displays the Frames Per Second (FPS) to provide feedback on the performance of the hand tracking and mouse control.

Window Handling:

The script tries to find the window titled "AI MOUSE" using win32gui and attempts to interact with that specific window. This may allow it to focus on controlling the mouse only within this window.
Exit Condition:

The system will continue running until the user presses the "q" key to quit the program.
Libraries Used:
OpenCV (cv2): Used for image capture, processing, and displaying the webcam feed.
MediaPipe (mediapipe): Used for detecting hand landmarks (fingers, palms).
Autopy (autopy): Used for controlling the mouse cursor and simulating mouse actions like clicks and movement.
PyAutoGUI (pyautogui): Used for right-click and scroll actions.
Win32gui (win32gui): Used for interacting with specific application windows by finding them with their title.
Time (time): Used for timing operations like calculating FPS and controlling the delay between actions.
Workflow:
Capture webcam feed.
Process the feed to detect hand landmarks.
Based on the detected finger gestures, control mouse actions:
Move cursor based on finger position.
Simulate mouse clicks, right-clicks, or scrolling based on finger gestures.
Display FPS and continuously update the webcam feed.
Exit when the "q" key is pressed.
Summary:
