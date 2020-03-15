import eel
from pytube import YouTube

eel.init("web")


def YtVideoDownload(data):
    yt = YouTube(data)
    videos = yt.streams.filter(progressive=True).all()
    i = 1
    for stream in videos:
        print(str(i) + " " + str(stream))
        i += 1
    
    # for x in videos:
    #     if "720p" in x:
    #         #video =
    #         print(x)
    
    stream_number = int(input("enter number :"))
    video = videos[stream_number-1]
    video.download()
    
    print("downloaded")
    
eel.start('main.html')
