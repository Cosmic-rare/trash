import hashlib
from datetime import datetime
import random


def hash(filename):

	date = (datetime.now().strftime('%Y%m%d%H%M%S%f'))
	rand = random.randint(1,10000000000000)
	dat = filename + date + str(rand)

	hs = hashlib.sha224(dat.encode()).hexdigest()

	# 拡張子をつけてファイル名を返す
	return hs + "." + filename[filename.find(".")+1:]


if __name__ == "__main__":
	print(hash("IMG_0276.jpg"))
