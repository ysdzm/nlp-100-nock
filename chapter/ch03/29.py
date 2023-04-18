import re
import json
import requests

filename = "jawiki-country.json"
with open(filename, mode="r") as f:
    for line in f:
        line = json.loads(line)
        if line["title"] == "イギリス":
            text_uk = line["text"]
            break

# テンプレートの抽出
pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
template = re.findall(pattern, text_uk, re.MULTILINE + re.DOTALL)
print(template)

# フィールド名と値を辞書オブジェクトに格納
pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
for k, v in result.items():
    print(k + ': ' + v)


def get_url(text):
    url_file = text['国旗画像'].replace(' ', '_')
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + \
        url_file + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    return re.search(r'"url":"(.+?)"', data.text).group(1)


print(get_url(result))
