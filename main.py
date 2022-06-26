from pytube import YouTube
import os
from platform import system
import argparse

def cls():
    user_os = system().lower()
    if(user_os == "windows"):
        os.system('cls')
    else:
        os.system('clear')

def __main__():
    cls()
    parser = argparse.ArgumentParser(description='Youtube video downloader.')
    parser.add_argument('--url',type=str,help='Url of the video (put the url in between of "" please)')

    args = parser.parse_args()
    print("Downloading file...")

    try:
        yt = YouTube(args.url)#get vid data
        streams = yt.streams.filter(progressive=True,file_extension="mp4")#filter files by mp4

        if(os.path.exists("OUTPUT") is False):
            print('Creating "OUTPUT" folder...')
            os.mkdir("OUTPUT")
            cls()
            print("FOLDER SUCCESSFULLY CREATED!!!")

        yt.streams.get_by_itag(streams[0].itag).download(output_path="OUTPUT/")#download video
    except:
        cls()
        assert False, "ERROR WHILE DOWNLOADING VIDEO!!!"

    cls()
    print('Download ended!!!')
