from sys import argv
from os import system
from datetime import datetime, timedelta
from re import search

def help():
    print "Cut video using ffmpeg"
    print "Author: SakaDream"
    print "Command: python cut-video.py <FileName> <Start> <End>"
    print "Duration format: hh:mm:ss"
    print "Example: 00:10:20\n"

def videoDurationCheck(start, end):
    matchstart = search("(?:(\d{1,2}):)?(\d{1,2}):(\d{2})", start)
    matchduration = search("(?:(\d{1,2}):)?(\d{1,2}):(\d{2})", end)
    if(matchstart and matchduration):
        return True
    else:
        return False

def process(filename, start, end):
    if search("^[][!\"#$%&\'()*+,./:;<=>?@\\^_`{|}~-]", filename):
        filename = filename[2:]
        print filename
    name, extension = filename.split(".")
    output = name + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "." + extension
    print "Processing your video...\n"
    system("ffmpeg.exe -ss " + start + " -i " + filename + " -to " + end + " -c copy -copyts " + output)

if __name__ == '__main__':
    if len(argv) == 4:
        script, filename, start, end = argv 
        if videoDurationCheck(start, end):
            process(filename, start, end)
        else:
            print("Invaild duration time, please try agian")
    else:
        print "Invaild command, read help() and try again\n"
        help()