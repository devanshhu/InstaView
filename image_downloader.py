import urllib
import os


def image_downloader_(url, name):
    try:
        urllib.request.urlretrieve(url, name + '.jpg')
        print('Download Successful.. Downloaded to ' + os.getcwd())
    except:
        print('sorry download failed ')
