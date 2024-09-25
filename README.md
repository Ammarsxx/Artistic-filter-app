# Artistic Filter App

This is a real-time webcam-based artistic filter application built with Python and OpenCV. The app allows users to apply various artistic effects, such as sketching, cartoonification, and edge detection, to a live webcam feed.

## Features
- **Sketch Filter**: Converts the live video into a pencil sketch effect.
- **Cartoon Filter**: Applies a cartoon-like filter to the video.
- **Edge Detection**: Highlights the edges in the video using the Canny edge detection algorithm.
- **Normal Feed**: Displays the original video without any filters.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/artistic-filter-app.git
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python
   ```
3. Run the script:
   ```bash
   python artistic_filter.py
   ```
4. Use the following keys to switch filters:
   - **`s`**: Apply Sketch Filter
   - **`c`**: Apply Cartoon Filter
   - **`e`**: Apply Edge Detection
   - **`n`**: Return to Normal Feed
   - **`q`**: Quit the app

## Requirements
- Python 3.7+
- OpenCV


