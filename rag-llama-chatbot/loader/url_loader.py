import requests
from bs4 import BeautifulSoup
import html2text

def load_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return html2text.html2text(str(soup))
