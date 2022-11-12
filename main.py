import youtube_dl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import music_tag


c = Options()
c.add_argument("--headless")
driver = webdriver.Chrome(options=c)


def dwl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])


def getmuscinfo(url):

    driver.get(url)
    sleep(5)
    description = driver.find_element(By.ID, 'plain-snippet-text').text
    return description[description.index("\n")+2:]


path = "Music/"
urls = []

while True:
    url = input("Enter URL to start dl press enter>")
    if url == "":
        break
    if url.__contains__("music.youtube.com"):
        url = "https://" + url[14:-1]
    urls.append(url)


for x in urls:
    description = getmuscinfo(x)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',}],
        'outtmpl': path + description +'.%(ext)s',
        }
    zxt = x.strip()
    dwl_vid()
    f = music_tag.load_file("Music/"+ description + ".mp3")

    f['title'] = description[:description.index("·")]
    f['artist'] = description[description.index("·")+1:]

    f.save()


driver.stop_client()
driver.close()
