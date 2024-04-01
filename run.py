#pip install pytube
from pytube import Playlist, YouTube
import re
import os
# --------------------------------------------------------------------------------------------------------------------------
def downloadOne(_url):
    # res= 360p / 720p / 144 
    res = "720p"
    try:
        yt = YouTube(_url)
        video = yt.streams.get_highest_resolution()
        # video =   yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc() .first()
        video =   yt.streams.filter(progressive=True, file_extension='mp4',res=res).first()    
        # title = str(i) + '-' + video.title
        title = video.title
        title = re.sub('[\/:?*"<>|]', '_', title)

        print("------------------ > : ",str(i))
        if not os.path.isdir(title) :
            print("----- > : ",title)
            # os.makedirs(title)
            video.download(title)
        else:
            print("----- > : exist : ",title)
            # break
    except:
        print("error : ",i)        
# --------------------------------------------------------------------------------------------------------------------------
# url_playlist = 'https://www.youtube.com/watch?v=Q0mWz1BYH-k&list=PLUitXL66pnO_K_Q_mqnB7MzoHjLnkU_jo&index=110'
# playlist = Playlist(url_playlist)
# listUrl = playlist.video_urls
# --------------------------------------------------------------------------------------------------------------------------
# var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);
# window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title-link"){console.log('\t'+v.title+'\t'+v.href+'\t')}});
# window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title-link"){console.log(v.href)}});
file = open("list.txt", "r")
listUrl = file.readlines()
# --------------------------------------------------------------------------------------------------------------------------
for i in range(0,len(listUrl)):
    downloadOne(listUrl[i])
