import cv2 as cv
import numpy as np

# Drawing state
drawing = False
prev_x, prev_y = -1, -1

WIDTH = 640
HEIGHT = 360

# Create camera
cam = cv.VideoCapture(0)
cam.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# Transparent drawing canvas
canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)


# Mouse event function
def mouse_event(event, x, y, flags, params):
    global drawing, prev_x, prev_y, canvas

    # Start drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        prev_x, prev_y = x, y

    # Draw while moving mouse
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.line(
                canvas,
                (prev_x, prev_y),
                (x, y),
                (255, 0, 0),
                3
            )
            prev_x, prev_y = x, y

    # Stop drawing
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


cv.namedWindow("OpenCV Drawing Canvas")
cv.setMouseCallback("OpenCV Drawing Canvas", mouse_event)


while True:
    success, frame = cam.read()

    if not success:
        print("Camera error")
        break

    # Combine camera frame with drawing layer
    output = cv.add(frame, canvas)

    cv.imshow("OpenCV Drawing Canvas", output)

    key = cv.waitKey(1) & 0xFF

    # Clear canvas
    if key == ord('c'):
        canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Exit
    elif key == ord('q'):
        break


cam.release()
cv.destroyAllWindows()