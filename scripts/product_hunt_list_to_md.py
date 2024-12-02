import os
# from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta, timezone
from openai import OpenAI
from bs4 import BeautifulSoup
import pytz
from collections import Counter
# 加载 .env 文件
# load_dotenv()

# 创建 OpenAI 客户端实例
api_key=os.getenv('OPENAI_API_KEY')
base_url=os.getenv('OPENAI_BASE_URL')
if base_url:
    client = OpenAI(api_key=api_key, base_url=base_url)
else:
    client = OpenAI(api_key=api_key)

producthunt_client_id = os.getenv('PRODUCTHUNT_CLIENT_ID')
producthunt_client_secret = os.getenv('PRODUCTHUNT_CLIENT_SECRET')
# 只取前 10 条数据
top_num=10
model = "gpt-4o-mini" 
#model = "Qwen/Qwen2.5-7B-Instruct" 

# Define category to keywords mapping
# Add more categories and corresponding keywords as needed
category_mapping_zh = {
    "人工智能": ["AI", "人工智能", "机器学习"],
    "工具": ["工具", "生产力工具", "效率","Notion"],
    "开发": ["API","数据库","REST API","SQL"]
}

category_mapping_en = {
    "AI": ["AI", "Artificial intelligence", "machine learning","AI agent"],
    "Tools": ["tool", "效率"],
    "Develop": ["API","Database","REST API","SQL"]
}

class Product:
    def __init__(self, id: str, name: str, tagline: str, description: str, votesCount: int, createdAt: str, featuredAt: str, website: str, url: str,en: bool, **kwargs):
        self.name = name
        self.tagline = tagline
        self.description = description
        self.votes_count = votesCount
        self.en = en
        if self.en:
            self.featured = "Yes" if featuredAt else "No"
            self.created_at = createdAt
            self.translated_tagline = self.tagline
            self.translated_description = self.description
        else:
            self.created_at = self.convert_to_beijing_time(createdAt)
            self.featured = "是" if featuredAt else "否"
            self.translated_tagline = self.translate_text(self.tagline)
            self.translated_description = self.translate_text(self.description)
        self.website = website
        self.url = url
        self.og_image_url = self.fetch_og_image_url()
        self.keyword = self.generate_keywords()

    def fetch_og_image_url(self) -> str:
        """获取产品的Open Graph图片URL"""
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            og_image = soup.find("meta", property="og:image")
            if og_image:
                return og_image["content"]
        return ""

    def generate_keywords(self) -> str:
        """生成产品的关键词，显示在一行，用逗号分隔"""
        if self.en:
            prompt = f"根据以下内容生成适合的英文关键词，用英文逗号分隔开：\n\n产品名称：{self.name}\n\n标语：{self.tagline}\n\n描述：{self.description}"
        else:
            prompt = f"根据以下内容生成适合的中文关键词，用英文逗号分隔开：\n\n产品名称：{self.name}\n\n标语：{self.tagline}\n\n描述：{self.description}"
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Generate suitable Chinese keywords based on the product information provided. The keywords should be separated by commas."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=50,
                temperature=0.7,
                timeout=600,
            )
            keywords = response.choices[0].message.content.strip()
            if ',' not in keywords:
                keywords = ', '.join(keywords.split())
            return keywords
        except Exception as e:
            print(f"Error occurred during keyword generation: {e}")
            return "无关键词"

    def translate_text(self, text: str) -> str:
        """使用OpenAI翻译文本内容"""
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是世界上最专业的翻译工具，擅长英文和中文互译。你是一位精通英文和中文的专业翻译，尤其擅长将IT公司黑话和专业词汇翻译成简洁易懂的地道表达。你的任务是将以下内容翻译成地道的中文，风格与科普杂志或日常对话相似。"},
                    {"role": "user", "content": text},
                ],
                max_tokens=500,
                temperature=0.7,
                timeout=600,
            )

            translated_text = response.choices[0].message.content.strip()
            return translated_text
        except Exception as e:
            print(f"Error occurred during translation: {e}")
            return text

    def convert_to_beijing_time(self, utc_time_str: str) -> str:
        """将UTC时间转换为北京时间"""
        utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ')
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = utc_time.replace(tzinfo=pytz.utc).astimezone(beijing_tz)
        return beijing_time.strftime('%Y年%m月%d日 %p%I:%M (北京时间)')

    def to_markdown(self, rank: int) -> str:
        """返回产品数据的Markdown格式"""
        og_image_markdown = f"![{self.name}]({self.og_image_url})"
        if self.en:
            # hugo 需要双空格+\n才是换行
            return (
                f"## {rank}. {self.name}\n"
                f"**Tagline**：{self.translated_tagline}  \n"
                f"**Description**：{self.translated_description}  \n"
                f"**Website**: [open]({self.website})  \n"
                f"**Product Hunt**: [View on Product Hunt]({self.url})  \n\n"
                f"{og_image_markdown}  \n\n"
                f"**Keyword**：{self.keyword}  \n"
                f"**VotesCount**: 🔺{self.votes_count}  \n"
                f"**Featured**：{self.featured}  \n"
                f"**CreatedAt**：{self.created_at}  \n\n"
                f"---  \n\n"
            )
        else:                
            return (
                f"## {rank}. {self.name}\n"
                f"**标语**：{self.translated_tagline}  \n"
                f"**介绍**：{self.translated_description}  \n"
                f"**产品网站**: [立即访问]({self.website})  \n"
                f"**Product Hunt**: [View on Product Hunt]({self.url})  \n\n"
                f"{og_image_markdown}  \n\n"
                f"**关键词**：{self.keyword}  \n"
                f"**票数**: 🔺{self.votes_count}  \n"
                f"**是否精选**：{self.featured}  \n"
                f"**发布时间**：{self.created_at}  \n\n"
                f"---  \n\n"
            )

def get_producthunt_token(): 
    """通过 client_id 和 client_secret 获取 Product Hunt 的 access_token"""
    url = "https://api.producthunt.com/v2/oauth/token"
    payload = {
        "client_id": producthunt_client_id,
        "client_secret": producthunt_client_secret,
        "grant_type": "client_credentials",
    }

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to obtain access token: {response.status_code}, {response.text}")

    token = response.json().get("access_token")
    return token

def fetch_product_hunt_data():
    """从Product Hunt获取前一天的Top 30数据"""
    token = get_producthunt_token()
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    date_str = yesterday.strftime('%Y-%m-%d')
    url = "https://api.producthunt.com/v2/api/graphql"
    headers = {"Authorization": f"Bearer {token}"}

    base_query = """
    {
      posts(order: VOTES, postedAfter: "%sT00:00:00Z", postedBefore: "%sT23:59:59Z", after: "%s") {
        nodes {
          id
          name
          tagline
          description
          votesCount
          createdAt
          featuredAt
          website
          url
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
    """

    all_posts = []
    has_next_page = True
    cursor = ""

    while has_next_page and len(all_posts) < top_num:
        query = base_query % (date_str, date_str, cursor)
        response = requests.post(url, headers=headers, json={"query": query})

        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from Product Hunt: {response.status_code}, {response.text}")

        data = response.json()['data']['posts']
        posts = data['nodes']
        all_posts.extend(posts)

        has_next_page = data['pageInfo']['hasNextPage']
        cursor = data['pageInfo']['endCursor']

    # 只保留前top_num个产品
    return [Product(**{**post, 'en': False}) for post in sorted(all_posts, key=lambda x: x['votesCount'], reverse=True)[:top_num]],[Product(**{**post, 'en': True}) for post in sorted(all_posts, key=lambda x: x['votesCount'], reverse=True)[:top_num]]


# 提取关键字
def extract_keywords(products,en:bool):
    keywords=[]
    max_len =10
    if en:
        max_len=30
    for product in products:
        if product.keyword:
            
            val=[keyword.strip() for keyword in product.keyword.split(',') if keyword.strip() and len(keyword)<max_len]
            keywords.extend(val)    
    return keywords

def count_and_sort_keywords(keywords):
    # 计算每个关键词的出现次数
    keyword_counts = Counter(keywords)
    # 按出现次数排序
    sorted_keywords = keyword_counts.most_common()
    return sorted_keywords

def generate_markdown(products, date_str:str,en:bool):
    """生成Markdown内容并保存到data目录"""
    # 获取今天的日期并格式化
    today = datetime.now(timezone.utc)
    date_today = today.strftime('%Y-%m-%d')
    date = today.strftime('%Y-%m-%d %H:%M:%S%z')
    
    # 提取关键词
    keywords = extract_keywords(products,en=en)
    top_keywords=count_and_sort_keywords(keywords)

    ## 文章标题
    markdown_content="---\n"
    if en:
        markdown_content += f"title: Producthunt Daily | {date_today}\n"
        markdown_content += f"date: {date}\n"
        markdown_content += f"image: {products[0].og_image_url}\n"  
        category_mapping=category_mapping_en
    else:
        markdown_content += f"title: 今日热榜 | {date_today}\n"
        markdown_content += f"date: {date}\n"
        markdown_content += f"image: {products[0].og_image_url}\n"        
        category_mapping=category_mapping_zh
    
    if len(top_keywords)>0:
        hugo_keywords = ', '.join([f'"{keyword}"' for keyword, _ in top_keywords[:3]])
        markdown_content += f'tags: [{hugo_keywords}]\n'

        categories = set()
        keyword_set = set(keyword for keyword, _ in top_keywords)
        for category, keywords in category_mapping.items():
            if any(keyword in keyword_set for keyword in keywords):
                categories.add(category)    
        if categories:
            vals = list(categories)
            vals.sort()
            formatted_categories = ', '.join(f'"{category}"' for category in vals)
            markdown_content += f'categories: [{formatted_categories}]\n'      
    markdown_content+="---\n\n"
    
    ## 内容
    for rank, product in enumerate(products, 1):
        markdown_content += product.to_markdown(rank)

    # 确保 data 目录存在
    os.makedirs('content/en/post', exist_ok=True)
    os.makedirs('content/zh-cn/post', exist_ok=True)

    # 修改文件保存路径到 data 目录
    if en:
        file_name = f"content/en/post/producthunt-daily-{date_str}.md"
    else:
        file_name = f"content/zh-cn/post/producthunt-daily-{date_str}.md"
    
    # 如果文件存在，直接覆盖
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"文件 {file_name} 生成成功并已覆盖。")


def main():
    # 获取昨天的日期并格式化
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    date_str = yesterday.strftime('%Y-%m-%d')

    # 获取Product Hunt数据
    products,productsEn = fetch_product_hunt_data()

    # 生成Markdown文件
    generate_markdown(products, date_str,en=False)
    generate_markdown(productsEn, date_str,en=True)

if __name__ == "__main__":
    main()