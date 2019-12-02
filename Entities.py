import random

class Player():

	#Attributes

	is_alive = True
	hp = 100
	gold = 0
	inventory = list()
	level = 0
	xp = 0

	#Constructors

	def __init__(self, nickname):
		self.nickname = nickname;

	#Setter & Getters

	def set_hp(self, hp):
		self.hp = hp

	def get_hp(self):
		return self.hp

	def set_gold(self, gold):
		self.gold = gold

	def get_gold(self):
		return self.gold

	def set_level(self, level):
		self.level = level

	def get_level(self):
		return self.level

	def set_xp(self, xp):
		self.xp = xp

	def get_xp(self):
		return self.xp

	def set_level(self, level):
		self.level = level

	def get_level(self):
		return self.level

	def set_nickname(self, nickname):
		self.nickname = nickname

	def get_nickname(self):
		return self.nickname

	#Methods

	def grab_item(self, item):
		inventory.append(item)

	def level_up(self):
		print(f"You have been prooted! Your level now is {level}")

	def die(self):
		self.is_alive = False

	def update(self):
		#Level Check
		if self.xp > 99:
			self.xp = self.xp - 100
			self.level_up()
		#HP Check
		if self.hp < 1:
			self.die()

	def level_up():
		print(f"œ You've been promoted! Your level now is {level}.")
		print("1. +60 HP")
		print("2. Get Random Item")
		print("3. Get Random Weapon")
		decision = int(input("Make your Choice: "))
		if decision == 1:
			self.xp += 60
		elif decision == 2:
			self.get_random_item()
		else:
			self.get_random_weapon()

	def get_random_item():
		pass

	def get_radnom_weapon():
		pass


class Enemy():

	def __init__(self, level):
		if level == 1:
			self.level = 1
			self.hp = 20
			self.gold_on_drop = int(random.random() * 10)
			self.xp_on_kill = int(random.random() * 12 + 6)
		elif level == 2:
			self.level = 2
			self.hp = 30
			self.gold_on_drop = int(random.random() * 10 + 10)
			self.xp_on_kill = int(random.random() * 12 + 12)
		elif level == 3:
			self.level = 3
			self.hp = 40
			self.gold_on_drop = int(random.random() * 10 + 20)
			self.xp_on_kill = int(random.random() * 12 + 18)
		print(f"There is a Monster [Level {self.level}]")

	#Setter & Getters

	def set_hp(self, hp):
		self.hp = hp

	def get_hp(self):
		return self.hp

	def set_gold_on_drop(self, gold_on_drop):
		self.gold_on_drop = gold_on_drop

	def get_gold_on_drop(self):
		return self.gold_on_drop

	def set_xp_on_kill(self, xp_on_kill):
		self.xp_on_kill = xp_on_kill

	def get_xp_on_kill(self):
		return self.xp_on_kill


if __name__ == "__main__":
	print("Please, run Game.py")
