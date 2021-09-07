# coding' UTF-8
import time
from urllib import request
import time
from bs4 import BeautifulSoup
import os
import re
from tqdm import tqdm
import ssl
import sys

from functions import check

# SSLのおまじない
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def setup(ncode):
    # ディレクトリの作成
    if not os.path.exists(ncode):
        os.makedirs(ncode)

def is_str(v):
    return type(v) is str

def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True

def part(ncode):
    # ページ数を取得する
    url = 'https://ncode.syosetu.com/novelview/infotop/ncode/{}/'.format(ncode)
    res = request.urlopen(url)

    # 解析する
    soup = BeautifulSoup(res, 'html.parser')
    pre_info = soup.select_one('#pre_info').text

    # 正規表現でページ数を取得
    num_parts = int(re.search(r'全([0-9]+)部分', pre_info).group(1))

    return num_parts

def get_range(ncode):

    url = 'https://ncode.syosetu.com/{}/{:d}'

    while True:
    # 整数値を取得する
        start = input('Start Range > ')
        end = input('End Range > ')

        # どちらかが空の場合は抜ける
        if start=='' or end=='':
            break
        
        # どちらかが文字列の場合はもう一度
        if not isint(start) or isint(end):
            print('Enter an integer')
        else:
            # 整数値に変換して調べる
            start, end = int(start), int(end)

            # 有効でない場合
            if not check_range(start, end):
                pass
            else:
                break
                return start, end
    
def check_range(start, end):
    # 最大値、最小値で調べる(404)
    try:
        request.urlopen(url.format(ncode, start))
    except:
        print('Orver Page(start)')
        return False
    try:
        request.urlopen(url.format(ncode, end))
    except:
        print('Orver Pagr(end)')
        return False        

def mode_all(ncode):
    parts = part(ncode)

    # 進捗バーの設定
    bar = tqdm(total=parts)

    for i in range(1, parts+1):
        res_url = 'https://ncode.syosetu.com/{}/{:d}'.format(ncode, i)
        
        # リクエストして解析
        res = request.urlopen(res_url)
        soup = BeautifulSoup(res, 'html.parser')
        honbun = soup.select_one('#novel_honbun').text

        # 改行コードを変換する
        honbun = honbun.replace('\n', '\r\n')

        # ページ数のファイルを生成する
        with open(ncode + '/' + str(i) + '.txt', 'w', encoding='shift_jis') as fr:
            pass

        # 一文字ずつ保存していく
        with open(ncode + '/' + str(i) + '.txt', 'w', encoding='shift_jis') as fr:
            for j in honbun:
                try:
                    fr.write(j)
                except:
                    fr.write('?')
        
        # 進捗を更新 => 待つ
        bar.update(1)
        time.sleep(0.75)

def mode_range(ncode, start, end):
    # 進捗バーの設定
    bar = tqdm(total=end-start+1)

    for i in range(start, end+1):
        res_url = 'https://ncode.syosetu.com/{}/{:d}'.format(ncode, i)
        
        # リクエストして解析
        res = request.urlopen(res_url)
        soup = BeautifulSoup(res, 'html.parser')
        honbun = soup.select_one('#novel_honbun').text

        # 改行コードを変換する
        honbun = honbun.replace('\n', '\r\n')

        # ページ数のファイルを生成する
        with open(ncode + '/' + str(i) + '.txt', 'w', encoding='shift_jis') as fr:
            pass

        # 一文字ずつ保存していく
        with open(ncode + '/' + str(i) + '.txt', 'w', encoding='shift_jis') as fr:
            for j in honbun:
                try:
                    fr.write(j)
                except:
                    fr.write('?')
        
        # 進捗を更新 => 待つ
        bar.update(1)
        time.sleep(0.75)


# ncodeの取得
while True:
    ncode = input('Ncode (If you use default, press Enter)> ')
    if ncode == '':
        ncode = 'n2267be'
    
    # 有効かどうかを調べる
    if check(ncode):
        break

setup(ncode)

# Modeの選択
print('Mode 1:All 2:range 3:OnePage')
while True:
    mode_input = input('Select Mode > ')
    if mode_input == '1':
        mode_all(ncode)
        break
    elif mode_input == '2':
        start, end = get_range(ncode)
        if is_str(start) or is_str(end):
            sys.exit()
        mode_range(ncode, start, end)
        break
    elif mode_input == '3':
        mode = 3
        break
    else:
        pass
