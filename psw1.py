
key = 'a123456'
i=3
while i:
	i-=1
	answer = input('請輸入密碼: ')
	if answer == key:
		print('登入成功')
		break
	if i != 0:
		print('"密碼錯誤! 還有', i, '次機會"')
