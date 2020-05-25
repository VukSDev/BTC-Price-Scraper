# scrapes a site for current price of btc

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://coinmarketcap.com/'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs the a tag on the page that holds the bitcoin price
containers = page_soup.findAll("a",{"class":"cmc-link"})
container = containers[17]

# prints the price of btc to the terminal
print("")
print("Current price of Bitcoin is: " + str(container.text))
print("")