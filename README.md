# Bad Apple with Labels

A small Python demo that converts a video (`bad.mp4`) into a 30×18 black-and-white pixel grid and plays it in a simple Tkinter window using CustomTkinter. Each video frame is converted to grayscale, resized, thresholded to binary, and displayed as a grid of black/white labels.

## Requirements

- Python 3.8+
- OpenCV (cv2)
- CustomTkinter
- Tkinter (usually included with Python on Windows)

## Install

From the project root (PowerShell), install dependencies:

```powershell
pip install opencv-python customtkinter
