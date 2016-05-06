from urllib import request

x = request.urlopen("http://www.asriran.com")
y = x.read()

print(y)