from pytubefix import Playlist
from pytubefix.cli import on_progress
from pytubefix import YouTube

info = {
    'wiseman': {
        'url': 'https://www.youtube.com/watch?v=juLa4hNoKoU&list=PL65yxaK_x91IhJjobxjugYGzKEZ87wgfU',
        'output_path': 'wiseman',
    },
    'spirit' : {
        'url': 'https://www.youtube.com/watch?v=bbsqp7hn4_M&list=PLZ6oZ9aUOsaPFIq9QaOUXawQMZm6Fi8qN',
        'output_path': 'spirit',
    },
}

channel = 'wiseman' # 'wiseman', 'spirit'
url = info[channel]['url']
output_path = info[channel]['output_path']

pl = Playlist(url)
# yt = YouTube(url, on_progress_callback=on_progress)

for video in pl.videos:
    yt = video.streams.get_audio_only()
    # print(yt.title)
    yt.download(output_path)