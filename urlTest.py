from urllib import request
from urllib import response
import sys

x = request.urlopen("http://www.tabnak.ir/")


y = x.read().decode('cp850').encode(sys.stdout.encoding,'replace').decode(sys.stdout.encoding)

print(y)

