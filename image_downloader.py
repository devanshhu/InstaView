import urllib
import os
import requests


def image_downloader_(url, name):

    with open(name, 'wb') as file:
        thisimage = requests.get(url)
        file.write(thisimage.content)
