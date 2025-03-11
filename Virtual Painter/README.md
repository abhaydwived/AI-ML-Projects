# Hand Tracking Virtual Painter

## Overview
This project is a **Hand Tracking Virtual Painter** using OpenCV and MediaPipe. It allows users to draw on a virtual canvas using their fingers. The program utilizes a webcam to detect hand gestures and provides an interactive drawing experience.

## Features
- **Hand Tracking:** Uses MediaPipe's Hand Tracking module to detect hands in real-time.
- **Drawing Mode:** Users can draw on the screen using their index finger.
- **Selection Mode:** Different colors can be selected by raising both the index and middle fingers.
- **Eraser Mode:** Users can erase drawings by selecting the eraser option.
- **Overlay Menu:** A menu at the top of the screen for selecting different brush colors.

## Installation & Setup
### Prerequisites
Make sure you have Python installed. Then, install the required dependencies using:
```sh
pip install opencv-python numpy mediapipe
```

### Running the Project
1. Clone the repository or download the script.
2. Ensure you have a folder named `Header` with color selection images.
3. Run the script using:
```sh
python virtual_painter.py
```
4. The webcam will open, and you can start drawing with your fingers.

## How to Use
### Hand Gestures
- **Selection Mode:** Raise both the index and middle fingers to select a color from the menu.
- **Drawing Mode:** Raise only the index finger and start drawing.
- **Eraser Mode:** Select the eraser color to remove drawings.

## Project Structure
```plaintext
|-- Header/                   # Folder containing color selection images
|-- handtracking.py           # Hand tracking module (if separate)
|-- hand_tracking_painter.py  # Main script
```

## Dependencies
- OpenCV
- NumPy
- MediaPipe

## Future Improvements
- Adding more brush styles and sizes.
- Implementing shape drawing (circles, rectangles, etc.).
- Saving the drawings as images.

## License
This project is open-source and free to use for educational purposes.

