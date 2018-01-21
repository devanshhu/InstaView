
from soup_maker import make_soup
from get_details import get_detail

rawurl = ''
if __name__ == '__main__':
    rawurl = input('Enter the Username:  ')
    url = "https://www.instagram.com/" + str(rawurl)
    # print(url)
    soup = make_soup(url)
    get_detail(soup)

    # print('project Successful')
    # print(soup.prettify())
