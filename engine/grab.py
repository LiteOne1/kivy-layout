#scater site and get info
from bs4 import BeautifulSoup
import requests



html_get = requests.get('https://www.rottentomatoes.com/m/deadpool_2')
html_get.encoding = 'UTF-8'

soup = BeautifulSoup(html_get.text, 'html.parser')

def get_movie_details(html_soup): 
    synopsis = soup.find('div', id='movieSynopsis')
    title = soup.find('h1', class_='title')
    rating= soup.find('span', class_='meter-value')
    cast = soup.find_all('div', {'class': 'media-body'})
    
    print(synopsis.text)
    print(title.text)
    print(rating.text)
    for name in cast:
        print name.span


get_movie_details(soup)