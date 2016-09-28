age = int(input("Введите пожалуйста возраст:  "))
if age <= 6:
	print("Дуй в детский сад")
elif age >6:
	if age <= 16:
		print("Дуй в школу")
	elif age > 16:
		if age <= 20:
			print("Дуй в ВУЗ")
		else:
			print("Дуй на работу")
	
