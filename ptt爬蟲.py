import requests
from bs4 import BeautifulSoup
import re
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'cookie': 'over18=1'}

# Regular expression pattern to match an IP address
ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
def get_titles_and_urls(soup):
    title_url = []
    count = 0
    r_ent = soup.select("div.r-ent")
    for title in r_ent:
        try:
            print(count, title.select_one("div.title a").text.strip())
            title_url.append(f'https://www.ptt.cc{title.select_one("div.title a")["href"]}')
            count += 1
        except:
            print('遭到刪除')
    return title_url


def vpn_status(ip):
    response = requests.get(f"https://ipinfo.io/{ip}", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    vpn_status_element = soup.select_one("#block-privacy > div > div:nth-child(2) > div:nth-child(1) img")
    if vpn_status_element:
        src_attribute = vpn_status_element['src']
        position_info = src_attribute.split('/')[-1]
        # Extract the portion before ".svg"
        vpn_tag = position_info.split('.')[0]
    else:
        return None
    if vpn_tag == 'right-big':
        vpn_stu = 'use VPN'
    else:
        vpn_stu = 'not use VPN'
    return vpn_stu


def get_ip_status(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    country = data.get("country")
    city = data.get('city')
    return country, city


def ptt():
    url = "https://www.ptt.cc/bbs/Gossiping/index.html"
    page = 0
    name_tag = 3
    while True:
        result_text = ""
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        url_page = get_titles_and_urls(soup)
        if page == 0:
            options = "[a] up"
        else:
            options = "[a] up [d] down"
        user_input = input(options + "\n").lower()
        if user_input == 'a':
            page += 1
            name_tag = 1
        elif user_input == 'd' and page > 0:
            page -= 1
            name_tag = 2
        else:
            print('------------------------------------')
            try:
                user_input_int = int(user_input)
                if 0 <= user_input_int <= len(url_page):
                    r = requests.get(url_page[user_input_int], headers=headers)
                    soup = BeautifulSoup(r.text, "html.parser")
                    sel = soup.select("#main-content")  # 前面有id 所以需要使用#字號
                    # 检查是否找到對應了的元素
                    if sel:
                        all_text = sel[0].text  # sel本身是一個列表  但我們要取得的是元素 所以第一個就是[0]
                        all_text = all_text.replace('()', '()\n')  # 在左括號前插入换行符
                        all_text = all_text.replace('標題', '\n標題')  # 在"標題"前插入换行符
                        all_text = all_text.replace('時間', '\n時間')  # 在"時間"前插入换行符
                        lines = all_text.split('\n')
                        for line in lines:
                            if line.startswith('推') or line.startswith('噓') or line.startswith('→'):
                                line = re.sub(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', r' \1', line)
                                match = re.search(ip_pattern, line)
                                if match:
                                    ip_address = match.group()  # ex: 114.47.66.79 12/22 16:50
                                    vpn = vpn_status(ip_address)
                                    line = f"{line} [{vpn}]"
                                    # country,city = get_ip_status(ip_address)
                                    # line = f"{line} [{country}] [{city}]"
                            result_text += line + "\n"
                        print(result_text)
                    else:
                        print("not found element")
                    input("anykey to return")
                    continue
                else:
                    print("Invalid input. Please enter 'a', 'd', or a valid number.")
            except ValueError:
                print("Invalid input. Please enter 'a', 'd', or a valid number.")
                continue
        # a標籤 最舊 上頁 下頁 最新 name_tag=0 最舊 =1 上頁  取得下一個頁面url
        url = "https://www.ptt.cc" + (
            soup.select(f"div.btn-group.btn-group-paging a")[3 if page == 0 else name_tag]["href"])


ptt()

