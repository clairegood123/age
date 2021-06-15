driving = input('請輸入有沒有開過車:')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請輸入年齡:')
age = int(age)
if driving == '有':
	if age >= 18:
		print('很棒~可以開車車了')
	else:
		print('你怎麼可以開車呢?')
elif driving == '沒有':
	if age >= 18:
		print('你年紀到了，可以考啦~')
	else:
		print('加油~再幾年就可以考啦~')