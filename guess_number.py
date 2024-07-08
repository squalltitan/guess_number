import random
r = random.randint(1,100)
count = 0
while True:
	count +=1
	number = input('請輸入你的數字')
	number = int(number)
	if number == r:
		print('你猜對了')
		print('這是你猜的第', count, '次')
		break
	else:
		if number > r:
			print('你猜的數字太大了')
		else:
			print('你猜的數字太小了')
	print('這是你猜的第', count, '次')