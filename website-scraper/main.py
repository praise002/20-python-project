import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    response = requests.get(url)
    
    
if __name__ == '__main__':
    url = 'http://udemy.com'
    scrape_data(url)