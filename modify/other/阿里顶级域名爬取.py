import requests
from bs4 import BeautifulSoup
import json
import re

# 发送 GET 请求
url = "https://wanwang.aliyun.com/domain/tld#.com"
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析 HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # 找到目标 <ul> 标签
    menu_list = soup.find('ul', {'role': 'menu', 'class': 'ace-menu ace-ver menu-list'})

    # 获取所有顶级域名并过滤
    if menu_list:
        # 域名正则表达式
        domain_pattern = re.compile(r'^\.[a-z]{2,}$')
        tlds = [{"domain": li.text.strip()} for li in menu_list.find_all('li') if domain_pattern.match(li.text.strip())]

        # 添加来源信息
        output = [{"domain": "来源-阿里爬取"}] + tlds

        # 输出到文件
        with open('src_ali_top_domain.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print("域名已成功保存到 src_ali_top_domain.json 文件中。")
    else:
        print("没有找到顶级域名列表。")
else:
    print(f"请求失败，状态码：{response.status_code}")
