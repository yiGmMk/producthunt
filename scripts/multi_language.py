import os
from time import sleep
import requests
from datetime import datetime, timedelta, timezone
from openai import OpenAI
from bs4 import BeautifulSoup
import pytz
from collections import Counter

# Language-related configurations
LANGUAGE_SETTINGS = {
    "zh": {
        "title": "Product Hunt 今日热榜",
        "file_path": "content/zh-cn/post",
        "translate_task": "将以下内容翻译成简体中文,只返回译文:",
        "category_mapping": {
            "人工智能": ["AI", "人工智能", "机器学习"],
            "工具": ["工具", "生产力工具", "效率", "Notion"],
            "开发": ["API", "数据库", "REST API", "SQL"]
        },
        "time_format": '%Y年%m月%d日 %p%I:%M (北京时间)',
        "timezone": 'Asia/Shanghai',
        "tagline_label": "标语",
        "description_label": "介绍",
        "website_label": "网站",
        "website_label2": "立即访问",
        "product_hunt_label": "在Product Hunt查看",
        "keyword_label": "关键词",
        "votes_count_label": "票数",
        "featured_label": "是否精选",
        "featured_mapping":  {"yes": "是", "no": "否"},
        "created_at_label": "发布时间",
        "keyword_prompt": "根据以下内容生成适合的简短中文关键词，用英文逗号分隔开：\n\n产品名称：{name}\n\n标语：{tagline}\n\n描述：{description}",
        "default_keyword": "无关键词",
    },
    "en": {
        "title": "Product Hunt Daily",
        "file_path": "content/en/post",
        "translate_task": "Translate the following text to English,only return the translation:",
        "category_mapping": {
            "AI": ["AI", "Artificial intelligence", "machine learning", "AI agent"],
            "Tools": ["tool", "效率"],
            "Develop": ["API", "Database", "REST API", "SQL"]
        },
        "time_format": '%Y-%m-%d %I:%M %p (UTC)',
        "timezone": 'UTC',
        "tagline_label": "Tagline",
        "description_label": "Description",
        "website_label": "Website",
        "website_label2": "open",
        "product_hunt_label": "View on Product Hunt",
        "keyword_label": "Keyword",
        "votes_count_label": "VotesCount",
        "featured_label": "Featured",
        "featured_mapping":  {"yes": "Yes", "no": "No"},
        "created_at_label": "CreatedAt",
        "keyword_prompt": "Generate suitable short keywords based on the product information provided, separated by commas.\n\nName: {name}\nTagline: {tagline}\nDescription: {description}",
        "default_keyword": "No keywords",
    },
    "es": {
        "title": "Tendencias de Hoy",
        "file_path": "content/es/post",
        "translate_task": "Translate the following text to Spanish,only return the translation:",
        "category_mapping": {
            "Inteligencia Artificial": ["AI", "Inteligencia Artificial", "aprendizaje automático"],
            "Herramientas": ["herramienta", "productividad", "eficiencia", "Notion"],
            "Desarrollo": ["API", "base de datos", "REST API", "SQL"]
        },
        "time_format": '%Y-%m-%d %I:%M %p (UTC)',
        "timezone": 'Europe/Madrid',
        "tagline_label": "Lema",
        "description_label": "Descripción",
        "website_label": "Sitio web",
        "website_label2": "Visitar",
        "product_hunt_label": "Ver en Product Hunt",
        "keyword_label": "Palabras clave",
        "votes_count_label": "Votos",
        "featured_label": "Destacado",
        "featured_mapping": {"yes": "Sí", "no": "No"},
        "created_at_label": "Fecha de creación",
        "keyword_prompt": "Generate suitable short keywords using Spanish based on the product information provided, separated by commas.\n\nName: {name}\nTagline: {tagline}\nDescription: {description}",
        "default_keyword": "Sin palabras clave"
    },
    "ar": {
        "title": "الأكثر رواجًا اليوم",
        "file_path": "content/ar/post",
        "translate_task": "将以下内容翻译成阿拉伯语,只返回译文:",
        "category_mapping": {
            "الذكاء الاصطناعي": ["الذكاء الاصطناعي", "AI", "تعلم الآلة"],
            "الأدوات": ["أداة", "إنتاجية", "كفاءة", "Notion"],
            "التطوير": ["API", "قاعدة بيانات", "REST API", "SQL"]
        },
        "time_format": '%Y-%m-%d %I:%M %p (UTC)',
        "timezone": 'Asia/Riyadh',
        "tagline_label": "الشعار",
        "description_label": "الوصف",
        "website_label": "الموقع الإلكتروني",
        "website_label2": "زيارة",
        "product_hunt_label": "عرض على Product Hunt",
        "keyword_label": "الكلمات المفتاحية",
        "votes_count_label": "عدد الأصوات",
        "featured_label": "مميز",
        "featured_mapping": {"yes": "نعم", "no": "لا"},
        "created_at_label": "تاريخ الإنشاء",
        "keyword_prompt": "根据以下内容生成简短的适合的阿拉伯语关键词，用英文逗号分隔开：\n\n产品名称：{name}\n\n标语：{tagline}\n\n描述：{description}",
        "default_keyword": "لا توجد كلمات مفتاحية"
    }
}

# Configure OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv('OPENAI_BASE_URL')
client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)

producthunt_client_id = os.getenv('PRODUCTHUNT_CLIENT_ID')
producthunt_client_secret = os.getenv('PRODUCTHUNT_CLIENT_SECRET')
top_num = 10
model = "gemini-1.5-flash" 
#model = "gpt-4o-mini" 
#model = "deepseek-ai/DeepSeek-V2.5" 
lang = os.getenv('LANGUAGE')

class Product:
    def __init__(self, language: str, **kwargs):
        self.language = language
        self.settings = LANGUAGE_SETTINGS[language]
        self.name = kwargs.get('name')
        self.tagline = kwargs.get('tagline')
        self.description = kwargs.get('description')
        self.votes_count = kwargs.get('votesCount')
        self.featuredAt = kwargs.get('featuredAt')
        self.createdAt = kwargs.get('createdAt')
        self.website = kwargs.get('website')
        self.url = kwargs.get('url')
        
        self.is_en = (language == 'en')
        self.featured = self.settings["featured_mapping"]["yes"] if self.featuredAt else self.settings["featured_mapping"]["no"]
        self.created_at = self.convert_to_local_time(self.createdAt)
        self.translated_tagline = self.tagline if self.is_en else self.translate_text(self.tagline)
        self.translated_description = self.description if self.is_en else self.translate_text(self.description)
        self.og_image_url = self.fetch_og_image_url()
        self.keyword = self.generate_keywords()

    def fetch_og_image_url(self) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            og_image = soup.find("meta", property="og:image")
            if og_image:
                return og_image["content"]
        return ""

    def generate_keywords(self) -> str:
        lang_settings = self.settings

        # Use language-specific prompt for keyword generation
        prompt = lang_settings['keyword_prompt'].format(
            name=self.name, tagline=self.tagline, description=self.description
        )

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": prompt}],
                max_tokens=100,
                temperature=0.7,
                timeout=600,
            )
            keywords = response.choices[0].message.content.strip()
            return ', '.join(keywords.split()) if ',' not in keywords else keywords
        except Exception as e:
            print(f"Error occurred during keyword generation: {e}")
            return lang_settings['default_keyword']

    def translate_text(self, text: str) -> str:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": self.settings['translate_task']}, {"role": "user", "content": text}],
                max_tokens=500,
                temperature=0.7,
                timeout=600,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error occurred during translation: {e}")
            return text

    def convert_to_local_time(self, utc_time_str: str) -> str:
        utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ')
        local_tz = pytz.timezone(self.settings['timezone'])
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_tz)
        return local_time.strftime(self.settings['time_format'])

    def to_markdown(self, rank: int) -> str:
        lang_settings = self.settings

        # Use language-specific keywords for markdown content
        markdown_labels = {
            "rank": f"{rank}. {self.name}",
            "tagline":  lang_settings["tagline_label"],
            "description": lang_settings["description_label"],
            "website": lang_settings["website_label"],
            "website2": lang_settings["website_label2"],
            "product_hunt": lang_settings["product_hunt_label"],
            "keyword":  lang_settings["keyword_label"],
            "votes_count": lang_settings["votes_count_label"],
            "featured": lang_settings["featured_label"],
            "created_at": lang_settings["created_at_label"],
        }
        og_image_markdown = f"![{self.name}]({self.og_image_url})"
        fields = [
            f"## {markdown_labels['rank']}",
            f"**{markdown_labels['tagline']}**: {self.translated_tagline}",
            f"**{markdown_labels['description']}**: {self.translated_description}",
            f"**{markdown_labels['website']}**: [{markdown_labels['website2']}]({self.website})",
            f"**Product Hunt**: [{markdown_labels['product_hunt']}]({self.url})",
            og_image_markdown,
            f"**{markdown_labels['keyword']}**: {self.keyword}",
            f"**{markdown_labels['votes_count']}**: 🔺{self.votes_count}",
            f"**{markdown_labels['featured']}**: {self.featured}",
            f"**{markdown_labels['created_at']}**: {self.created_at}",
            "\n"
            "---"
        ]
        return "  \n".join(fields) + "  \n\n"

def get_producthunt_token():
    url = "https://api.producthunt.com/v2/oauth/token"
    payload = {
        "client_id": producthunt_client_id,
        "client_secret": producthunt_client_secret,
        "grant_type": "client_credentials",
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    response.raise_for_status()
    return response.json().get("access_token")

def fetch_product_hunt_data():
    token = get_producthunt_token()
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    date_str = yesterday.strftime('%Y-%m-%d')
    url = "https://api.producthunt.com/v2/api/graphql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
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
        response.raise_for_status()
        data = response.json()['data']['posts']
        posts = data['nodes']
        all_posts.extend(posts)
        has_next_page = data['pageInfo']['hasNextPage']
        cursor = data['pageInfo']['endCursor']
    # 只进行一次排序
    sorted_posts = sorted(all_posts, key=lambda x: x['votesCount'], reverse=True)[:top_num]
    return sorted_posts

def extract_keywords(products):
    keywords = [keyword.strip() for product in products for keyword in product.keyword.split(',') if keyword.strip()]
    return keywords

def count_and_sort_keywords(keywords):
    keyword_counts = Counter(keywords)
    return keyword_counts.most_common()

def generate_markdown(products, date_str: str, language: str):
    today = datetime.now(timezone.utc)
    date_today = today.strftime('%Y-%m-%d')
    date = today.strftime('%Y-%m-%d %H:%M:%S%z')
    keywords = extract_keywords(products)
    top_keywords = count_and_sort_keywords(keywords)
    
    settings = LANGUAGE_SETTINGS[language]
    path = settings['file_path']
    category_mapping = settings['category_mapping']

    os.makedirs(path, exist_ok=True)
    markdown_content = f"---\ntitle: {settings['title']} | {date_today}\ndate: {date}\nimage: {products[0].og_image_url}\n"

    if top_keywords:
        hugo_keywords = ', '.join([f'"{keyword}"' for keyword, _ in top_keywords[:3]])
        markdown_content += f"tags: [{hugo_keywords}]\n"
        categories = set()
        keyword_set = set(keyword for keyword, _ in top_keywords)
        for category, keywords in category_mapping.items():
            if any(keyword in keyword_set for keyword in keywords):
                categories.add(category)
        if categories:
            formatted_categories = ', '.join(f'"{category}"' for category in sorted(categories))
            markdown_content += f'categories: [{formatted_categories}]\n'
    markdown_content += "---\n\n" + ''.join(product.to_markdown(rank) for rank, product in enumerate(products, 1))

    file_name = f"{path}/producthunt-daily-{date_str}.md"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"文件 {file_name} 生成成功并已覆盖。")

def main():
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    date_str = yesterday.strftime('%Y-%m-%d')
    posts = fetch_product_hunt_data()
    products = []
    # https://ai.google.dev/pricing?hl=zh-cn#1_5flash , gemini-1.5-flash 限制了15RPM(每分钟15个请求)
    # 每个post需要3次
    for post in posts:
        products.append(Product(language=lang, **post))
        sleep(15)  # 每5秒钟生成一个Product对象
    generate_markdown(products, date_str, language=lang)

def save_csv():
    return 

if __name__ == "__main__":
    main()
