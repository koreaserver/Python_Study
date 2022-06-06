import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com/covid19/map?hl=ko&mid=/m/06qd3&gl=KR&ceid=KR:ko'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    count = soup.select_one('#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div.FVeGwb.ARbOBb > div.BP0hze > div.y3767c > div > div > div.zRzGke.EA71Tc.pym81b > div.UnO7qd > div:nth-child(1) > div > div.fNm5wd.qs41qe > div.UvMayb')
    print("확진자 수 : " + count.get_text())
    dead = soup.select_one('#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div.FVeGwb.ARbOBb > div.BP0hze > div.y3767c > div > div > div.zRzGke.EA71Tc.pym81b > div.UnO7qd > div:nth-child(1) > div > div.fNm5wd.ckqIZ > div.UvMayb')
    print("사망자 수 : " + dead.get_text())

else : 
    print(response.status_code)
