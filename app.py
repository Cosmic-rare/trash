# coding: UTF-8
import time
from urllib import request
import time
from bs4 import BeautifulSoup
import os
import re
from tqdm import tqdm

# SSLのおまじない(安全じゃない)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 本のコードを記入
ncode = "n2267be"


# ディレクトリーがあるのかを調べる(なければ作る)
if not os.path.exists(ncode):
    os.makedirs(ncode)

# ページ数を取得
url = "https://ncode.syosetu.com/novelview/infotop/ncode/{}/".format(ncode)
res = request.urlopen(url)

# 解析
soup = BeautifulSoup(res, "html.parser")
pre_info = soup.select_one("#pre_info").text

# 正規表現でページ数を取得
num_parts = int(re.search(r"全([0-9]+)部分", pre_info).group(1))

# ページ数を表示(print)
print(num_parts)

num_parts = int(num_parts)

# 進捗の合計値を設定
bar = tqdm(total = num_parts + 1)


# ページ数の数だけ繰り返す
for part in range(1, 1+num_parts):
     
    bar.update(1)

    # forで本文のurlを整形
    url = "https://ncode.syosetu.com/{}/{:d}/".format(ncode, part)

    # リクエストして解析
    res = request.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    honbun = soup.select_one("#novel_honbun").text

    # サーバーに負荷がかからないように1秒待つ
    time.sleep(1)

    # ページ数のファイルを作成する
    with open(ncode + "/" + str(part) + ".txt", "w") as fr:
        fr.write(honbun)