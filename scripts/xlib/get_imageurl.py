from bs4 import BeautifulSoup
import requests


# 获取随机图片
def imgurl_list(
    collections=None,
    username=None,
    orientation="landscape",
    query: str = "",
    topics: str = "6sMVjTLSkeQ,iUIsnVtjB0Y,Fzo3zuOHN6w,Jpg6Kidl-Hk,CDwuwXJAbEw",  # nature(6sMVjTLSkeQ),textures-patterns(iUIsnVtjB0Y),travel(Fzo3zuOHN6w),animals(Jpg6Kidl-Hk),food-drink,3d-renders(CDwuwXJAbEw)
    content_filter="low",
    count=10,
):
    """
    collections: Public collection ID(‘s) to filter selection. If multiple, comma-separated
    topics     : Public topic ID(‘s) to filter selection. If multiple, comma-separated
    username   : Limit selection to a single user.
    query      : Limit selection to photos matching a search term.
    orientation: Filter by photo orientation. (Valid values: landscape, portrait, squarish),按照片方向过滤。（有效值： 横向 、 纵向 、 方形 ）
    content_filter: Limit results by content safety. Default: low. Valid values are low and high. 通过内容安全限制结果。默认值： 低 。有效值为低和高 。
    count      : The number of photos to return. (Default: 1; max: 30)   要返回的照片数。（默认值：1;最大值：30）
    """

    url = "https://api.unsplash.com/photos/random"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Version": "v1",
        "Authorization": "Client-ID QB8WpJVbwPfveZ8q89emYtUzJh7dpDFl2DzQ0pdv4Ps",
    }

    params = {}
    if count:
        params["count"] = count
    if query:
        params["query"] = query
    if topics:
        params["topics"] = topics
    if collections:
        params["collections"] = collections
    if username:
        params["username"] = username
    if orientation:
        params["orientation"] = orientation
    if content_filter and content_filter != "low":
        params["content_filter"] = content_filter

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        resp_json = response.json()
    except (
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
    ) as e:
        print("Request failed: ", e)

    # html = response.text
    #
    # soup = BeautifulSoup(html, "html.parser")
    #
    # image_elements = soup.find_all('div', {'class': 'sc-bZQynM kfLMln wallpaper'})

    imgurl_list = []

    for image in resp_json:
        # id = image_element.a['href'].split("/")[-1].strip()
        # url = "https://wallpaperhub.app/api/v1/get/" + id + "/0/1080p"
        url = image["urls"]["raw"]
        imgurl_list.append(url)

    return imgurl_list


# 获取topics
def get_unsplash_topics():
    url = "https://api.unsplash.com/topics"
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Version": "v1",
        "Authorization": "Client-ID QB8WpJVbwPfveZ8q89emYtUzJh7dpDFl2DzQ0pdv4Ps",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching topics: {e}")
        return None


if __name__ == "__main__":
    imgurl_list()
