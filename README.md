# Interactive Drawing Canvas using OpenCV

## 📌 Description
An interactive computer vision project that allows users to draw on a live camera feed using mouse movements. The application uses OpenCV to process real-time video frames and overlay drawings on top of the camera stream.

## 🚀 Features
- Real-time webcam streaming
- Interactive drawing using mouse events
- Drawing overlay on live video
- Clear canvas functionality
- Real-time image processing with OpenCV

## 🛠️ Technologies Used
- Python
- OpenCV
- NumPy

## ⚙️ How It Works
1. Capture live video from the webcam.
2. Create a transparent drawing canvas.
3. Detect mouse events:
   - Left mouse button press starts drawing.
   - Mouse movement creates lines.
   - Mouse button release stops drawing.
4. Merge the drawing layer with the camera frame.
5. Display the final output in real time.

## ▶️ Installation

Install the required libraries:

```bash
pip install opencv-python numpy
