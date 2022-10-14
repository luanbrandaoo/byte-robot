from youtubesearchpython import VideosSearch
from pytube import YouTube

def download_music(search):
    videosSearch = VideosSearch(search+'"audio"', limit = 1)
    result = videosSearch.result()['result'][0]

    title = str(result['title']).replace('(Audio)','').replace('(audio)','').replace('(AUDIO)','').replace('(Lyric)','').replace('(Lyrics)','').replace('(Lyrics Video)','').replace('(lyric)','').replace('(lyrics)','').replace('(lyrics video)','')
    url = str(result['link'])
    thumbnail = str(result['thumbnails'][-1]['url'])

    yt=YouTube(url)
    t=yt.streams.filter(only_audio=True).all()
    t[-1].download('music.webm')

if __name__ == "__main__":
    download_music(input('digite o nome da música: '))