from youtubesearchpython import VideosSearch
from pytube import YouTube as PyTube
from pytube.cli import on_progress

def main():
    grappler = input("Enter grappler name: ")
    print(grappler)

    searchTerm = grappler + ' "vs"'
    folderPath = '/mnt/c/Users/Bun/Videos/' + grappler

    videoSearch = VideosSearch(searchTerm, limit = 2)
    videoResults = videoSearch.result()["result"]

    links = []

    for video in videoResults:
        links.append(video["link"])

    for url in links: 
        try:
            ytObject = PyTube(url, on_progress_callback=on_progress)
            ytObject.streams.get_highest_resolution().download(folderPath)
        except Exception as e:
            print(e)
            raise Exception('Exception occured')

    

if __name__ == "__main__":
    main()

