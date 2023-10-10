from pytube import YouTube


yt = YouTube("https://youtu.be/OjNpRbNdR7E?feature=shared")
streams= yt.streams.filter(file_extension='mp4', progressive=True , res="720p")
resolution=[]
tag = streams[0].itag
print(tag)
stream = yt.streams.get_by_itag(tag)


