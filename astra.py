import cv2
from aruco import ARUCO_DICT
from camera import init_capture_device, close_capture_device, start_astra, get_frame_astra
from aruco import detect_markers

def main():
    libpath = "/home/tom/Resources/OpenNI/sdk/libs"

    aruco_dictionary = cv2.aruco.Dictionary_get(ARUCO_DICT["DICT_4X4_50"])
    aruco_parameters = cv2.aruco.DetectorParameters_create()
    
    dev = init_capture_device(libpath)

    color_stream = start_astra(dev)

    while True:
        frame = get_frame_astra(color_stream)

        detected_markers = detect_markers(frame, aruco_dictionary, aruco_parameters)

        # Display the frame with ArUco markers
        cv2.imshow("ArUco Markers", detected_markers)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    close_capture_device(color_stream)
    cv2.destroyAllWindows()

if __name__ == '__main__':
  main()