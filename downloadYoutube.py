from pytube import Playlist ,YouTube
import re

url_playlist =\
'https://www.youtube.com/watch?v=DRd918aoZaw&list=PLqfwbUVlG7UewbjmxHDRvzr2bQVz_S1x5'

playlist = Playlist(url_playlist)
listUrl = playlist.video_urls


for i in range(0,len(listUrl)):
    yt = YouTube(listUrl[i])
    video = yt.streams.filter(progressive=True,
                                file_extension='mp4', resolution="360p"#720p 144
                                ).first()
    print(video)
    title = str(i) +" - "+ video.title
    title = re.sub(r"[\/:*?""<>|]", "", title)
    # video = yt.streams.get_highest_resolution()

    print(title)
    # with open('url.txt', 'a') as the_file:
    #     the_file.write(url_download+'\n')
    
    video.download("v\\"+title)



