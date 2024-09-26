# Detecting Aruco markers with Alphabot 2

## Description
This repository provides a basic example of detecting Aruco markers with the Alphabot 2. Although developed for the Alphabot 2, the code can also be run on any personal computer. In this case, a Python environment should be configured to match the Python version and dependencies used by the Alphabot 2. The following sections explain how to install the code and configure the Python environment. Additionally, a basic example demonstrates how to detect Aruco markers using the device's camera.

## Requirements

- Python >= 3.6

## Installation
1. Clone this repository to the desried folder:

        git clone https://github.com/TomvanEemeren/aruco_markers.git

2. Create a virtual environment in the repository folder:

        python3 -m venv .venv

3. Activate the virtual environment:

        source .venv/bin/activate

4. Install the dependencies using pip:

        pip install -r requirements.txt

## Demo
This demo provides a basic example of using the device's camera to detect Aruco markers. To start the demo, run the Python script from the terminal, using the `--type` or `-t` flags to pass the desired Aruco dictionary as an argument:

    python3 detection.py -t "DICT_4X4_50"

This will open an OpenCV window that displays the video stream from the camera. If any Aruco markers from the selected dictionary are detected, they will be highlighted with a bounding box and their corresponding IDs will be displayed. Press 'q' to close the window. 

