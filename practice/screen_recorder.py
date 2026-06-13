import cv2
import numpy as np
import pyautogui
import time

# Screen Size
screen_size = pyautogui.size()

# Video Writer
fourcc = cv2.VideoWriter_fourcc(*"XVID")

filename = f"recording_{int(time.time())}.avi"

out = cv2.VideoWriter(
    filename,
    fourcc,
    20.0,
    screen_size
)

print("Recording Started...")
print("Press 'q' in video window to stop.")

while True:

    # Screenshot
    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    out.write(frame)

    cv2.imshow(
        "Screen Recorder",
        frame
    )

    if cv2.waitKey(1) == ord("q"):
        break

out.release()

cv2.destroyAllWindows()

print(
    f"Recording Saved: {filename}"
)