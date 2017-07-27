import requests
import sys
import subprocess



THREAD_URL = 'https://lab.facepunch.com/api/post/get/{}/100/'.format(sys.argv[1])
deetz = requests.get('https://lab.facepunch.com/api/thread/info/{}'.format(sys.argv[1])).json()
pc = 0

while True:
	req = requests.get(THREAD_URL + str(pc)).json()
	f = open(sys.argv[1] + '.txt', 'a', encoding='utf-8')
	for post in req['Posts']:
		f.write(post['Text'].replace("\n", " ") + "\n\r")
		print('#{} of #{}'.format(post['PostNumber'], deetz['PostCount']))
		pc = post['PostNumber']
		if post['PostNumber'] == deetz['PostCount']:
			f.close()
			subprocess.call('py cloud.py --text {0}.txt --imagefile {0}.png --width=1800 --height=1200 --margin=10 --stopwords stopwords.txt'.format(sys.argv[1]))
			subprocess.call('rm {0}.txt'.format(sys.argv[1]))
			sys.exit(1)