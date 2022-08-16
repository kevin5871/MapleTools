import requests
import math
from bs4 import BeautifulSoup


def GetCharInfo(nick) :
    url = 'https://maple.gg/u/' + nick
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        lvlexp = soup.select_one('li.user-summary-item:nth-child(1)').text
        tmp = lvlexp.split('(')
        lvl = tmp[0][3:]
        exp = tmp[1].replace(')','').replace('%','')
        img = soup.select_one('.col-md-8 > img:nth-child(1)')['src']
        expn = requests.get("http://wachan.me/exp_api.php?exp1=%s&option=n"%lvl).json()['result']
        expn = math.floor(float(expn) * (float(exp) * 0.01))
        return {'Lev' : lvl, 'AvatarImgURL' : img, 'Exp' : expn}

if __name__ == '__main__' :
    print(GetCharInfo(''))