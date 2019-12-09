import Items

class Shop():

	def __init__(self, day, player):
		print("You've found a shop!")
		shopping_list = self.generate_list(day)
		while True:
			print("Today there're:")
			for i in range(3):
				print(f"{i+1}. {shopping_list[i]}")
			print("4. Exit")
			decision = int(input("Make your Choice: "))
			if decision == 1:
				shopping_list[0] = ""
				player.grab_armor(shopping_list[0])
			elif decision == 2:
				shopping_list[1] = ""
				player.grab_armor(shopping_list[1])
			elif decision == 3:
				shopping_list[2] = ""
				player.grab_consum(shopping_list[2])
			elif decision == 4:
				break
	
	def generate_list(self, day):
		shopping_list = list()
		if day < 10:
			#Low Quality Items - generate common items
			shopping_list.append(Items.Helmet("Wooden"))
			shopping_list.append(Items.Chest("Wooden"))
			shopping_list.append(Items.HealPotion())
		elif day < 20:
			#Mid Quality Items - generate rare items
			pass 
		elif day < 30:
			#High Quality Items - generate mythical items
			pass 
		return shopping_list
