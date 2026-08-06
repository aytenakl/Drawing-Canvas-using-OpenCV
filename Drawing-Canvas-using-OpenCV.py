import cv2 as cv
import numpy as np

# Canvas size
WIDTH = 640
HEIGHT = 360

# Drawing state
drawing = False
prev_x, prev_y = -1, -1


# Create camera
cam = cv.VideoCapture(0)

cam.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)


# Create transparent drawing canvas
canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)


# Mouse callback function
def mouse_event(event, x, y, flags, params):
    global drawing, prev_x, prev_y, canvas

    # Start drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        prev_x, prev_y = x, y


    # Draw while moving
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



# Create window
cv.namedWindow("Drawing Canvas using OpenCV")

cv.setMouseCallback(
    "Drawing Canvas using OpenCV",
    mouse_event
)



while True:

    success, frame = cam.read()

    if not success:
        print("Error: Camera not detected")
        break


    # Combine camera frame and drawing layer
    output = cv.add(
        frame,
        canvas
    )


    # Display result
    cv.imshow(
        "Drawing Canvas using OpenCV",
        output
    )


    key = cv.waitKey(1) & 0xFF


    # Clear canvas
    if key == ord('c'):
        canvas = np.zeros(
            (HEIGHT, WIDTH, 3),
            dtype=np.uint8
        )


    # Exit
    elif key == ord('q'):
        break



cam.release()
cv.destroyAllWindows()
