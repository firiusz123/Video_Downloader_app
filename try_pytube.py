from pytube import YouTube


yt = YouTube("https://youtu.be/OjNpRbNdR7E?feature=shared")
streams= yt.streams.filter(file_extension='mp4', progressive=True)
resolution=[]
for stream in streams:
    resolution.append(stream.resolution)

print(resolution)