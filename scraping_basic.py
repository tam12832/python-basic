import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://hosh-it.github.io/scraping-practice/practice.html"
response = requests.get(url)

print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify)

# タグ名で取得
img_find = soup.find('img')
print(img_find)
imgs_find_all = soup.find_all('img')
print(imgs_find_all)

# クラス名で取得(グループ毎に複数取得できる)
class_find = soup.find('img', class_='size-middle')
print(class_find)

# id名で取得
id_find = soup.find('img', id='small-size')
print(id_find)

# 欲しい情報の取得(要素の属性情報や要素内の文字列)
property_once = class_find.get('src')
print(property_once)
img_src_list = []
for imgs_get in imgs_find_all:
  # print(imgs_get.get('src'))
  img_src_list.append(imgs_get.get('src'))
print(img_src_list)

# リンク先の取得例
links_get_list = soup.find_all("a")
link_src_list = []
for link_get_list in links_get_list:
  link_src_list.append(link_get_list.get('href'))
print(link_src_list)

# タグ内のテキスト文の取得例
sentences_get = soup.find_all("a")
sentences_list = []
for sentence in sentences_get:
  sentences_list.append(sentence.get_text())
print(sentences_list)

# def get_sentence():
#   sentences_get = soup.find_all("a")
#   sentences_list = []
#   for sentence in sentences_get:
#     sentences_list.append(sentence.get_text())
#   # print(sentences_list)

# print(get_sentence())
# csv形式で保存(pandas使用)
csv_list = {
  'a_text_list': sentences_list,
  'a_href_list': link_src_list,
  'img_src_list': img_src_list,
}
print(pd.DataFrame(csv_list))
df = pd.DataFrame(csv_list)
df.to_csv('scraping_basic.csv', index=False, encoding='utf-8_sig')

