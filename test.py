from pytube import YouTube

url='http://youtube.com/watch?v=2lAe1cqCOXo'
yt = YouTube(url)

for stream in yt.streams:
     print(stream)