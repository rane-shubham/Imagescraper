from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
import random

print("\n*********************WELCOME TO IMAGESCRAPER*********************\n")

search = input("Search for an image:")
params = {"q": search}
i = int(input("Enter number of images you want to save:"))
count = 0
dir_name = search.replace(" ", "_")

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

r = requests.get("https://www.bing.com/images/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})
link_len = len(links)

while not count == i:
    try:
        rand_num = random.randint(0, link_len)
        img_obj = requests.get(links[rand_num].attrs["href"])
        print("Getting:", links[rand_num].attrs["href"])
        title = links[rand_num].attrs["href"].split("/")[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + title, img.format)
            count += 1
        except:
            continue
    except:
        continue

