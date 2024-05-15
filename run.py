#pip install pytube
from pytube import Playlist, YouTube
import re
# --------------------------------------------------------------------------------------------------------------------------
def downloadOne(_url):
    # res= 360p / 720p / 144 
    res = "720p"
    prefix= "_"
    extension= "mp4"
    try:
        yt = YouTube(_url)
        # video = yt.streams.get_highest_resolution()
        video = yt.streams.filter(progressive=True, file_extension=extension,res=res).order_by('resolution').desc() .first()
        title = video.title
        title = re.sub('[\/:?*"<>|]', '_', title)
        video.download(output_path="./download/" ,filename=title+"."+extension ,filename_prefix=prefix )
    except Exception as e:
        print("error : ",_url)        
# --------------------------------------------------------------------------------------------------------------------------
url_playlist = 'https://www.youtube.com/watch?v=TyKwwVemYhw&list=PLKhm8Z5pXdOUWVTnTojfHw_Cr7Ac-HLyR'
playlist = Playlist(url_playlist)
listUrl = playlist.video_urls
# --------------------------------------------------------------------------------------------------------------------------
# var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);
# window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title-link"){console.log('\t'+v.title+'\t'+v.href+'\t')}});
# window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title-link"){console.log(v.href)}});
# file = open("list.txt", "r")
# listUrl = file.readlines()
# --------------------------------------------------------------------------------------------------------------------------
for i in range(0,len(listUrl)):
    print("------------------ > : ",str(i))
    downloadOne(listUrl[i])
