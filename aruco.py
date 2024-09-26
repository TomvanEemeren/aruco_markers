import cv2

ARUCO_DICT = {
  "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
  "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
  "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
  "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
  "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
  "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
  "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
  "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
  "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
  "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
  "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
  "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
  "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
  "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
  "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
  "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
  "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL
}

def acuro_display(corners, ids, rejected, frame):
    """
    Draws a bounding box around the detected ArUco markers, calculates and 
    draws the center of the markers, and displays the marker IDs on the frame.

    Args:
        corners (list): List of detected ArUco marker corners.
        ids (ndarray): Array of detected ArUco marker IDs.
        rejected (list): Returned list of ArUco marker candidates.
        frame (ndarray): Input frame to display the markers on.

    Returns:
        frame (ndarray): Frame with ArUco markers displayed.
    """

    # Check that at least one ArUco marker was detected
    if len(corners) > 0:

        ids = ids.flatten()

        # Loop over the detected ArUco corners
        for (marker_corner, marker_id) in zip(corners, ids):
        
            # Extract the marker corners
            corners = marker_corner.reshape((4, 2))
            (top_left, top_right, bottom_right, bottom_left) = corners

            # Convert the (x,y) coordinate pairs to integers
            top_right = (int(top_right[0]), int(top_right[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
            bottom_left = (int(bottom_left[0]), int(bottom_left[1]))
            top_left = (int(top_left[0]), int(top_left[1]))

            # Draw the bounding box of the ArUco detection
            cv2.line(frame, top_left, top_right, (0, 255, 0), 2)
            cv2.line(frame, top_right, bottom_right, (0, 255, 0), 2)
            cv2.line(frame, bottom_right, bottom_left, (0, 255, 0), 2)
            cv2.line(frame, bottom_left, top_left, (0, 255, 0), 2)

            # Calculate and draw the center of the ArUco marker
            center_x = int((top_left[0] + bottom_right[0]) / 2.0)
            center_y = int((top_left[1] + bottom_right[1]) / 2.0)
            cv2.circle(frame, (center_x, center_y), 4, (0, 0, 255), -1)

            # Draw the ArUco marker ID on the video frame
            # The ID is always located at the top_left of the ArUco marker
            cv2.putText(frame, str(marker_id), 
                (top_left[0], top_left[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)

    return frame

def detect_markers(frame, aruco_dictionary, aruco_parameters):
    """
    Detects ArUco markers of a specific type in a video frame 
    and displays the markers on the frame.

    Args:
        frame (ndarray): Input frame to detect ArUco markers.
        aruco_dictionary (cv2.aruco.Dictionary): ArUco marker dictionary.
        aruco_parameters (cv2.aruco.DetectorParameters): ArUco detector parameters.

    Returns:
        detected_markers (ndarray): Frame with ArUco markers displayed.
    """

    # Detect ArUco markers in the video frame
    (corners, ids, rejected) = cv2.aruco.detectMarkers(
        frame, aruco_dictionary, parameters=aruco_parameters)

    # Display the resulting frame
    # For raspberry pi camera, this drastically reduces performance
    detected_markers = acuro_display(corners, ids, rejected, frame)

    return detected_markers