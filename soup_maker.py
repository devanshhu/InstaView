from bs4 import BeautifulSoup
from requests import get

def make_soup(url):
	agent = {'User-Agent':'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}	
	htmltxt = get(url, headers=agent ).text
	soup= BeautifulSoup(htmltxt,'lxml')
	return soup
