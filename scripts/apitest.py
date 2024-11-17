from product_hunt_list_to_md import Product


a=Product(id='11',
          name='Softr for Notion',
          tagline='Discover hidden niches before they go mainstream',
          description='A new trends intelligence tool that helps you discover under-the-radar trending products, companies and ideas. Spot new niche markets and uncover hidden business opportunities before they go mainstream',
          votesCount=1,
          createdAt='2023-10-05T14:48:00Z',
          featuredAt='2023-10-05T14:48:00Z',
          website='https://www.producthunt.com/r/OBFDFWJ666PSXQ?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+decohack+%28ID%3A+131684%29',
          url='https://www.producthunt.com/posts/softr-for-notion?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+decohack+%28ID%3A+131684%29')
print(a.to_markdown(1))