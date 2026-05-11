import cv2
import numpy as np
import pyautogui
from datetime import datetime

# Screen size
screen_size = pyautogui.size()

# Video filename
filename = datetime.now().strftime(
    "recording_%Y%m%d_%H%M%S.avi"
)

# Video writer
fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter(
    filename,
    fourcc,
    20.0,
    screen_size
)

print("Recording started...")
print("Press 'q' to stop.\n")

while True:
    # Screenshot
    screenshot = pyautogui.screenshot()

    # Convert image to numpy array
    frame = np.array(screenshot)

    # Convert RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write frame
    out.write(frame)

    # Show live recording
    cv2.imshow("Screen Recorder", frame)

    # Stop on q key
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources
cv2.destroyAllWindows()
out.release()

print(f"\nRecording saved as: {filename}")