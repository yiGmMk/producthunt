import requests
from bs4 import BeautifulSoup


def fetch_og_image_url(url) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        og_image = soup.find("meta", property="og:image")
        if og_image:
            return og_image["content"]
    return ""

url="https://www.producthunt.com/posts/lanceboard-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+weekly+%28ID%3A+148189%29"

print(fetch_og_image_url(url=url))