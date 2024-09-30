import requests
from bs4 import BeautifulSoup
import json

# 获取网页内容
url = "https://zh.wikipedia.org/wiki/%E4%BA%92%E8%81%94%E7%BD%91%E9%A1%B6%E7%BA%A7%E5%9F%9F%E5%88%97%E8%A1%A8"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的 wikitable
tables = soup.find_all('table', class_='wikitable')

# 存储顶级域名信息
tlds = []

# 处理每个表格
for table in tables:
    rows = table.find_all('tr')[1:]  # 跳过表头
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2:  # 确保有名称和实体
            tld_name = cols[0].get_text(strip=True)
            entity = cols[1].get_text(strip=True)
            tlds.append({
                "domain": tld_name,
                "entity": entity
            })

# 输出为 JSON 格式并保存到文件
with open('src_wiki_domain.json', 'w', encoding='utf-8') as f:
    json.dump(tlds, f, ensure_ascii=False, indent=4)

print("数据已保存到 top_level_domains.json")
