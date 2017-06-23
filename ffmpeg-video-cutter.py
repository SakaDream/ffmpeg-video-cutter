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

def durationCalculator(start_str, end_str):
    start_t = datetime.strptime(start_str,"%H:%M:%S")
    end_t = datetime.strptime(end_str,"%H:%M:%S")
    start_s = timedelta(hours=start_t.hour, minutes=start_t.minute, seconds=start_t.second).total_seconds()
    end_s = timedelta(hours=end_t.hour, minutes=end_t.minute, seconds=end_t.second).total_seconds()
    duration_s = end_s - start_s
    return duration_s

def process(filename, start, end):
    duration = str(durationCalculator(start, end))
    if search("^[][!\"#$%&\'()*+,./:;<=>?@\\^_`{|}~-]", filename):
        filename = filename[2:]
        print filename
    name, extension = filename.split(".")
    output = name + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "." + extension
    print "Processing your video...\n"
    system("ffmpeg.exe -i " + filename + " -ss " + start + " -c copy -t " + duration + " " + output)

if __name__ == '__main__':
    if len(argv) != 4:
        print "Invaild command, read help() and try again\n"
        help()
    else:
        matchstart = search("(?:(\d{1,2}):)?(\d{1,2}):(\d{2})", argv[2])
        matchduration = search("(?:(\d{1,2}):)?(\d{1,2}):(\d{2})", argv[3])
        if not matchstart and not matchduration:
            print("Invaild duration time, please try agian")
        else:
            process(argv[1], argv[2], argv[3])