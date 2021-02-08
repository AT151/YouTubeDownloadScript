from youtubesearchpython import VideosSearch
from pytube import YouTube as PyTube

grappler = input("Enter grappler name: ")
print(grappler)

searchTerm = grappler + ' "vs"'

videoSearch = VideosSearch(searchTerm, limit = 3)
videoResults = videoSearch.result()["result"]

links = []

for video in videoResults:
    youtubeStream = PyTube(video["link"])
    print(youtubeStream.streams.filter(only_video=True).first())



