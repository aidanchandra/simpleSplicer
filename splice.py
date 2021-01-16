import cv2
import os
import argparse

def generateFrames(video, path, prepend, append, leading, start, end):
    '''
    Generates and saves each frame from start to end in the specified video

    Per each frame, one can optionally specify a string to prepend and append to the number of the
        frame itself, allowing for easy matching of rigid inputs elsewhere

    Leading specifies how many leading zeroes will be in the number of the name of the file that is saved

    See the readme for more information
    '''
    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    count = 0
    while success and (end == -1 or count < end):
      if count >= start:
        cv2.imwrite(os.path.join(path,(prepend + str(count).zfill(leading) + append + ".jpg")), image)     # save frame as JPEG file
      success,image = vidcap.read()
      count += 1


if __name__ == "__main__":
    '''
    Output directory    Working
    Start frame         Working
    End frame           Working
    prepend             Working
    append              Working
    n of leading 0's    Working
    video               Working
    '''

    ##Defualt path to save videos to
    defaultPath = os.path.dirname(os.path.abspath(__file__)) + "/output/"

    ##Argument parsing
    parser = argparse.ArgumentParser(description="Simple Video to frames program")
    parser.add_argument(
        "--video",
        type=str,
        help="The name of the video to start generating from (including extension)",
        required=True
    )
    parser.add_argument(
        "--start_frame",
        type = int,
        help = "The number of the frame to start splicing from (0 indexed :) )",
        required= False,
        default=0
    )
    parser.add_argument(
        "--end_frame",
        type=int,
        help="The number of the frame to end splicing",
        required=False,
        default=-1
    )
    parser.add_argument(
        "--path",
        type=str,
        help="The location of the absolute path to export files",
        required=False,
        default=defaultPath
    )
    parser.add_argument(
        "--prepend",
        type=str,
        help="The string to add to the end of the frame number",
        required=False,
        default="frame"
    )
    parser.add_argument(
        "--append",
        type=str,
        help="The string to add to the beginning of the frame number",
        required=False,
        default=""
    )
    parser.add_argument(
        "--leading",
        type=int,
        help="The number of leading zeroes to add to the beginning of the frame number",
        required=False,
        default=0
    )
    args = parser.parse_args()

    ##Now, actually do the thing!
    generateFrames(args.video, args.path, args.prepend, args.append, args.leading, args.start_frame, args.end_frame)