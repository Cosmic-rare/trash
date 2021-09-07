import ssl

# SSLのおまじない
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def check(ncode):
    # ncodeが有効であるかチェックする
    url = 'https://ncode.syosetu.com/novelview/infotop/ncode/{}/'.format(ncode)
    try:
        request.urlopen(url)
    except:
        boo = False
    else:
        boo = True
    # 有効でない場合Falseが帰ってくる
    return boo

