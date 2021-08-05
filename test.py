import requests
from bs4 import BeautifulSoup

URL = 'https://www.airbnb.fr/rooms/16765199?adults=1&source_impression_id=p3_1628135606_5GJdbRjg9rqp9UCx&guests=1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="_le6wlg")

for result in results:
    print(result.text)
