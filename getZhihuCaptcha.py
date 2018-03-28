import requests
import json
import os
import base64
import time

headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
	'x-udid':'AHBvRsIDUg2PTm1lihb_y4bLF684cbDbvR8=',
	'x-xsrftoken':'276a5f89-1585-49e1-b906-24afab993feb'
}
proxy = {'http':'113.207.44.70:3128'}
url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'

def get_img_data():
	try:
		first_request = requests.get('https://www.zhihu.com/signup?next=%2F', headers = headers)
		headers['Cookie'] = first_request.headers['Set-Cookie']
		r = requests.get(url, headers = headers, proxies = proxy)
		cap_ticket = r.headers['Set-Cookie']
		headers['Cookie'] += ';' + cap_ticket;
		r = requests.put(url, headers = headers, proxies = proxy)
		imageSrc = json.loads(r.text)['img_base64']
		return imageSrc
	except:
		print('connection failed')
		return 'FAILED'

def save_img(imageSrc, path):
	try:
		img_data = base64.b64decode(imageSrc)
		file = open(path, 'wb')
		file.write(img_data)
		file.close()
		print('save img successfully')
	except:
		print('save img failed')

def get_captcha_img():
	for i in range(100):
		src = get_img_data()
		path = './captcha/' + str(i) + '.jpg'
		if(src != 'FAILED'):
			save_img(src, path)
		time.sleep(1)

get_captcha_img()