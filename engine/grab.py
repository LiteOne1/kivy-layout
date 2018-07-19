#scater site and get info
from bs4 import BeautifulSoup
import requests



html_get = requests.get('https://www.rottentomatoes.com/m/deadpool_2')
html_get.encoding = 'UTF-8'

soup = BeautifulSoup(html_get.text, 'html.parser')

def get_synopsis(html_soup): 
    synopsis = soup.find('div', id='movieSynopsis')
    return synopsis.text

