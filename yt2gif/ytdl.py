import youtube_dl

url = 'https://www.youtube.com/watch?v=hqf3u18kQaA?start=5'

#ydl_opts = {'merge_output_format':'webm', 'recodevideo':'webm', 'extractaudio':False}
ydl_opts = {'format':'243', 'extractaudio':False, 'outtmpl':'down/tiger.webm', 'postprocessor_args': '-ss 00:00:10 -t 00:00:15'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  vid = ydl.download([url])

