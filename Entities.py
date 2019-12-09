import random
import Items

#PLAYER CLASS

class Player():

	#Constructors

	def __init__(self, nickname):
		self.nickname = nickname
		self.is_alive = True
		self.hp = 100 
		self.ap = 0 
		self.gold = 0
		self.gold_earned = 0
		self.inventory = [[], [], []] #weapons, armor, consumables
		self.level = 0
		self.xp = 0
		self.day = 1

	#Setter & Getters

	def set_hp(self, hp):
		self.hp = hp

	def get_hp(self):
		return self.hp

	def set_ap(self, ap):
		self.ap = ap

	def get_ap(self):
		return self.ap	

	def set_gold(self, gold):
		self.gold = gold

	def get_gold(self):
		return self.gold

	def set_gold_earned(self, gold_earned):
		self.gold_earned = gold_earned

	def get_gold_earned(self):
		return self.gold_earned

	def set_level(self, level):
		self.level = level

	def get_level(self):
		return self.level

	def set_xp(self, xp):
		self.xp = xp

	def get_xp(self):
		return self.xp

	def set_nickname(self, nickname):
		self.nickname = nickname

	def get_nickname(self):
		return self.nickname

	def set_day(self, day):
		self.day = day

	def get_day(self):
		return self.day

	#Methods

	def add_to_inventory(self, item):
		if isinstance(item, Items.Weapon):
			self.inventory[0].append(item)
		elif isinstance(item, Items.Armor):
			self.inventory[1].append(item)
		elif isinstance(item, Items.Consumable):
			self.inventory[2].append(item)

	def remove_from_inventory(self, item):
		if item in self.inventory:
			self.inventory.remove(item)

	def die(self):
		self.is_alive = False

	def resurrect(self):
		self.is_alive = True

	def update(self):
		#Armor Check
		if len(self.inventory[2]) != 0:
			self.ap = 0
			for slot in self.inventory[2]:
				self.ap += slot.ap

		#Level Check
		if self.xp > 99:
			self.xp = self.xp - 100
			self.level_up()

		#HP Check
		if self.hp < 1:
			self.die()

	def level_up(self):
		self.level += 1
		print(f"\nœ You've been promoted! Your level now is {self.level}.\n")
		print("1. +60 HP")
		print("2. Get Random Item [not working]")
		print("3. Get Random Weapon [not working]")
		decision = int(input("Make your Choice: "))
		if decision == 1:
			self.hp += 60
		elif decision == 2:
			pass
		else:
			pass

	def get_random_item(self):
		pass

	def get_radnom_weapon(self):
		pass


class Enemy():

	def __init__(self, level):
		if level == 1:
			self.level = 1
			self.hp = 10
			self.gold_on_drop = int(random.random() * 10)
			self.xp_on_kill = int(random.random() * 12 + 6)
		elif level == 2:
			self.level = 2
			self.hp = 15
			self.gold_on_drop = int(random.random() * 10 + 10)
			self.xp_on_kill = int(random.random() * 12 + 12)
		elif level == 3:
			self.level = 3
			self.hp = 20
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
	print("Entities.py")
