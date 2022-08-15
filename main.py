import os
import argparse

from unicodedata import name
from pytube import YouTube
from os.path import exists
from platform import system

def cls():
    try:
        user_os = system().lower()
        if(user_os == "windows"):
            os.system('cls')
        else:
            os.system('clear')
    except OSError:
        assert False, "UNKNOW OS ERROR!!!"

def __main__():
    cls()
    parser = argparse.ArgumentParser(description='Youtube video downloader. (remember to put values in-between of "")')
    parser.add_argument('--url',type=str,help='Video URL')
    parser.add_argument('--res',type=str, default=None,help='Video resolution, i.e: 144p, 240p, 360p, 480p, 720p')

    args = parser.parse_args()
    print("Downloading file...")

    try:
        yt = YouTube(args.url)#get vid data
        streams = yt.streams.filter(progressive=True,file_extension="mp4",resolution=args.res)#filter files by mp4

        if(exists("OUTPUT") is False):
            os.mkdir("OUTPUT")
        if(exists("OUTPUT/"+yt.title.upper()+"_"+args.res+".mp4") is True):
            assert False,"VIDEO ALREADY DOWNLOADED"

        yt.streams.get_by_itag(streams[0].itag).download(output_path="OUTPUT/", filename=yt.title.upper()+"_"+args.res+".mp4")#download video
    except RuntimeError:
        cls()
        assert False, "ERROR WHILE DOWNLOADING VIDEO!!!"

    cls()
    print('Download ended!!!')
    
if(__name__ == "__main__"):
    __main__()