import random


class Weapon():
	
	def __init__(self, name, type):
		self.name = name;
		if type == 0:
			self.damage = int(random() * 6)
			self.ammo = 18
			self.price = 30 + int(random.random() * 6)
		elif type == 1:
			self.damage = int(random.random() * 12 + 6)
			self.ammo = 12
			self.price = 46 + int(random.random() * 6)
		else:
			self.damage = int(random.random() * 18 + 12)
			self.ammo = 6
			self.price = 62 + int(random.random() * 6)


class Potion():
	pass


if __name__ == "__main__":
	print("Please, run Game.py")
