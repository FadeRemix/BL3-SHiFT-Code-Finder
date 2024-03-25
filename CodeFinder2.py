import requests
from bs4 import BeautifulSoup

URL = "https://mentalmars.com/game-news/borderlands-3-golden-keys/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

name_results = soup.find("tbody")
for child in name_results.children:
    print(child.get_text(" | ",strip = True))
    
input("\nPress Enter to exit...")
