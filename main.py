import requests
from bs4 import BeautifulSoup

print("Hello Python + Docker with its containers")

def scrape(url):
    a = []
    img = []
    data = requests.get(url)
    img_url = url
    s = BeautifulSoup(data.text , "html.parser")
    for i in s.find_all('a'):
        href = i.attrs['href']
        if href.startswith("/"):
            url += href
            if url not in a :
                a.append(url)
    print(a)
    for i in s.find_all('img'):
        src = i.attrs['src']
        img.append(src)
    print(img)
    return {"Number of images" : len(img),
    "Number of links" : len(a)}

if __name__ == "__main__":
    print(scrape(input("Enter url : \n")))


