from urllib import request

with request.urlopen("http://www.hao123.com") as f:
	with open("baidu1.html","w",encoding="utf-8") as wf:
		wf.write(f.read().decode("utf-8"))
		



