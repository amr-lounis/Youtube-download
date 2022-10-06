from pytube import Playlist ,YouTube
import re

url_playlist = 'https://www.youtube.com/watch?v=9-3NXuezvTg&list=PLTXGTJFiOSPE0NUN31_c7-FMWnBjOtlKv'

playlist = Playlist(url_playlist)
listUrl = playlist.video_urls

for i in range(0,len(listUrl)):
    try:
        yt = YouTube(listUrl[i])
        video = yt.streams.get_highest_resolution()
        # video =   yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc() .first()
        video =   yt.streams.filter(progressive=True, file_extension='mp4',res="360p").first()
        # res= 360p / 720p / 144 
        title = str(i) + '-' + video.title
        title = re.sub('[\/:?*"<>|]', '_', title)
        print("------------------ > : ",title)
        video.download(title)
        # break
    except:
        print("error : ",i)
