from moviepy.editor import VideoFileClip
import sys, getopt, math, os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def split_movie(inputfile, number):
    clip = VideoFileClip(inputfile)
    start = 0.0

    total = math.floor(clip.duration)
    segment = total // number

    filename, extension = os.path.splitext(inputfile)

    print(filename)
    endpoints = []
    for i in range(number):
        if i == number - 1:
            endpoints.append(clip.duration)
        else:
            endpoints.append(segment * (i + 1))

    pieces = []
    for point in endpoints:
        pieces.append((start, point))
        start = point

    for i, piece in enumerate(pieces):
        name = filename + "_" + str(i + 1) + extension
        ffmpeg_extract_subclip(inputfile, piece[0], piece[1], name)
        print("Splitting %s into file %s..." % (inputfile, name))

def main(argv):
    inputfile = ''
    number = 2
    try:
        opts, args = getopt.getopt(argv, "i:n:")
    except getopt.GetoptError:
        print("Error")
    print(opts)
    for opt, arg in opts:
        if opt == "-i":
            inputfile = arg
        elif opt == "-n":
            number = int(arg)
    print("Input File is:", inputfile)
    print("Number of splits:", number)
    split_movie(inputfile, number)

if __name__ == "__main__":
    main(sys.argv[1:])
