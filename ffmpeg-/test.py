from ffmpeg import stream



s = stream.Stream()
s.input_file = 'xxx.mp4'
print(s.video_info())

