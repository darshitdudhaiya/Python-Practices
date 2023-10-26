import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=iphone&ref=nb_sb_noss"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}

data = {'title': [], 'price': []}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")

prices = soup.select("span.a-price")

for span in spans:
    print(span.string)
    data["title"].append(span.string)

for price in prices:
    if not ("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        data["price"].append(price.find("span").get_text())
        if len(data["price"]) == len(data["title"]):
            break

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)
