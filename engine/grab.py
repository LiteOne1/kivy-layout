#scater site and get info
from bs4 import BeautifulSoup
import requests



html_rotten = requests.get('https://www.rottentomatoes.com/m/deadpool_2')
html_insider = requests.get('https://www.movieinsider.com/m14108/deadpool-2')
#html_get.encoding = 'UTF-8'

soup = BeautifulSoup(html_rotten.text, 'html.parser')
soup1 = BeautifulSoup(html_insider.text, 'html.parser')

def get_synopsis(html_soup): 
    synopsis = soup.find('div', id ='movieSynopsis')
    return synopsis.text

def get_rating(html_soup):
    rating = soup.find('span', {'class': 'meter-value superPageFontColor'})
    return rating.text

def get_cast(html_soup1):
        actors = ''
        cast = soup1.find_all('b', itemprop = 'actor')
        for actor in cast:
            actors += actor.text+', '
        return actors


print(get_synopsis(soup))
print(get_rating(soup))
print(get_cast(soup1))
