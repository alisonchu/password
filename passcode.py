x = 3
while True:
	p = input('請輸入密碼: ')
	if p == 'a123456':
		print('登入成功')
		break
	if p != 'a123456' and x > 1:
		print('密碼錯誤! 還有', x - 1, '次機會')
	if p != 'a123456' and x <= 1:
		print('超過3次密碼錯誤, 請大俠重新再來')
		break
	x = x - 1

# 自己寫出來的!!
