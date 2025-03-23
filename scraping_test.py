import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://hosh-it.github.io/scraping-practice/"
response = requests.get(url)
url_article_coffee = "https://hosh-it.github.io/scraping-practice/coffee.html"
response_coffee = requests.get(url_article_coffee)
url_article_sakura = "https://hosh-it.github.io/scraping-practice/sakura.html"
response_sakura = requests.get(url_article_sakura)
url_article_mtg = "https://hosh-it.github.io/scraping-practice/onlinemtg.html"
response_mtg = requests.get(url_article_mtg)
url_article_camp = "https://hosh-it.github.io/scraping-practice/camp.html"
response_camp = requests.get(url_article_camp)

soup = BeautifulSoup(response.text, 'html.parser')
coffee = BeautifulSoup(response_coffee.text, 'html.parser')
sakura = BeautifulSoup(response_sakura.text, 'html.parser')
mtg = BeautifulSoup(response_mtg.text, 'html.parser')
camp = BeautifulSoup(response_camp.text, 'html.parser')

# tag取得
# a_tag
a_tags_find_all = soup.find_all('a')
# img_tag
img_tags_find_all = soup.find_all('img')
# p_tag
coffee_p_tags_find_all = coffee.find_all('p')
sakura_p_tags_find_all = sakura.find_all('p')
mtg_p_tags_find_all = mtg.find_all('p')
camp_p_tags_find_all = camp.find_all('p')

# それぞれのソースを格納する配列を作成
title_list = []
for a_tag_list in a_tags_find_all:
  title_list.append(a_tag_list.get_text())
print(title_list)
img_url_list=[]
for img_src_list in img_tags_find_all:
  img_url_list.append(img_src_list.get('src'))
print(img_url_list)
coffee_list = []
for coffee_p_list in coffee_p_tags_find_all:
  coffee_list.append(coffee_p_list.get_text())
coffee_p = ''.join(coffee_list)
sakura_list = []
for sakura_p_list in sakura_p_tags_find_all:
  sakura_list.append(sakura_p_list.get_text())
sakura_p = ''.join(sakura_list)
mtg_list = []
for mtg_p_list in mtg_p_tags_find_all:
  mtg_list.append(mtg_p_list.get_text())
mtg_p = ''.join(mtg_list)
camp_list = []
for camp_p_list in camp_p_tags_find_all:
  camp_list.append(camp_p_list.get_text())
camp_p = ''.join(camp_list)

all_article = []
all_article.append(coffee_p)
all_article.append(sakura_p)
all_article.append(mtg_p)
all_article.append(camp_p)
print(all_article)
scraping_test = {
   "タイトル": title_list,
   "画像URL": img_url_list,
   "記事": all_article
}

print(pd.DataFrame(scraping_test))
df = pd.DataFrame(scraping_test)
df.to_csv("scraping_test.csv", index=False, encoding='utf-8_sig')

