import cv2
from aruco import ARUCO_DICT, detect_markers
from args import parse_args, load_aruco
from camera import get_frame_uvc, start_uvc, stop_uvc

def main():
    # Parse the command line arguments
    args = parse_args()
    aruco_dictionary, aruco_parameters = load_aruco(args)

    cap = start_uvc()

    while True:
        frame = get_frame_uvc(cap)  

        detected_markers = detect_markers(frame, aruco_dictionary, aruco_parameters)

        cv2.imshow('frame', detected_markers)

        # If "q" is pressed on the keyboard, exit this loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break

    # Close down the video stream
    stop_uvc(cap)
    cv2.destroyAllWindows()
   
if __name__ == '__main__':
  main()