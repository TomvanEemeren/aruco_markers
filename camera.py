import cv2
import numpy as np
from openni import openni2

def start_uvc():
    cap = cv2.VideoCapture(0)

    return cap

def get_frame_uvc(cap):
    ret, frame = cap.read()

    return frame

def stop_uvc(cap):
    cap.release()

def init_capture_device(libpath):
    openni2.initialize(libpath)
    dev = openni2.Device.open_any()
    return dev

def close_capture_device(color_stream):
    color_stream.stop()
    openni2.unload()

def start_astra(dev):
    # Create a color stream
    color_stream = dev.create_color_stream()

    # Start the color stream
    color_stream.start()

    return color_stream

def get_frame_astra(color_stream):
    # Read a frame from the color stream
    frame = color_stream.read_frame()

    # Convert the frame to a numpy array
    frame_data = frame.get_buffer_as_uint8()
    frame_np = np.frombuffer(frame_data, dtype=np.uint8)
    frame_np = frame_np.reshape((frame.height, frame.width, 3))

    # Convert the frame to grayscale
    bgr_frame = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
    bgr_frame = cv2.flip(bgr_frame, 1)

    return bgr_frame