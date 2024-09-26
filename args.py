import sys
import cv2
import argparse
from aruco import ARUCO_DICT

def parse_args():
    # Allow parsing arguments via the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", type=str, metavar='', default="DICT_6X6_250",
                        help="ArUco dictionary to use (default: DICT_6X6_250)")
    
    return vars(parser.parse_args())

def load_aruco(args):
    aruco_type = args["type"]

    # Check that we have a valid ArUco marker
    if ARUCO_DICT.get(aruco_type) is None:
        print("[INFO] ArUCo tag of '{}' is not supported".format(args["type"]))
        sys.exit(0)

    # Load the ArUco dictionary
    print("[INFO] detecting '{}' markers...".format(aruco_type))
    aruco_dictionary = cv2.aruco.Dictionary_get(ARUCO_DICT[aruco_type])
    aruco_parameters = cv2.aruco.DetectorParameters_create()

    return aruco_dictionary, aruco_parameters
