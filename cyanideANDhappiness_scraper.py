import sys
from pushbullet import Pushbullet
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

pushbullet_auth_filepath = "C:\Temp\Python_auth\pusbullet_authkey.txt"

with open(pushbullet_auth_filepath) as f:
    authkey = f.readline()
    pb = Pushbullet(authkey.strip())


# sys.stdout=open('C:\Temp\Scrapes\Scraper_Logs\cyanideAndHappiness_scraper_log.txt','a')

minIndex = 1
maxIndex = 4215

for i in range(minIndex, maxIndex):
    print("Checking :" + str(i))
    page = requests.get("http://explosm.net/comics/" + str(i)).content
    soup = BeautifulSoup(page)
    comicImage = soup.find("img", {"id": "main-comic"})
    if comicImage is not None:
        comicURL = "http:" + comicImage['src'].strip()

        for char in comicURL:
            if char in " ":
                print("Replacing")
                comicURL = comicURL.replace(char, "%20")

        print("URL : " + comicURL)
        try:
            urlretrieve(comicURL, "C:\Temp\Scrapes\CH\\CH" + str(i) + ".png")
        except Exception as e:
            print("ERROR!!!" + str(e))
            continue

push = pb.push_note("Cyanide And Happiness", "Downloaded from " +
                    str(minIndex) + " to " + str(maxIndex) + ".")
