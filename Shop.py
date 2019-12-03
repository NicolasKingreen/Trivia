class Shop():

	def __init__(self, day):
		print("You've found a shop!")
		shopping_list = generate_list(day)
		while True:
			print("Today there'are:")
			for i in range(3):
				print(f"{i+1}. {shopping_list[i]}")
			print("4. Exit")
			decision = int(input("Make your Choice: "))
			if decision == 4:
				break
	
	def generate_list(self, day)
		shopping_list = list()
		if day < 10:
			#Low Quality Items - generate common items
			pass
		elif day < 20:
			#Mid Quality Items - generate rare items
			pass 
		elif day < 30:
			#High Quality Items - generate mythical items
			pass 
		return shopping_list
