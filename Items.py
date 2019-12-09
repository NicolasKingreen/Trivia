import random

class Item():

	def __init__(self, name, id, price, size):
		self.name = name
		self.id = id
		self.price = price
		self.size = size

	def add_to_inventory(self, player):
		player.add_to_inventory(self)

	def remove_from_inventory(self, player):
		player.remove_from_inventory(self)

#Weapons

class Weapon(Item):
	
	def __init__(self, name, id, price, size, damage):
		super().__init__(name, id, price, size)
		self.damage = damage

class Sword(Weapon):

	pass

#Armor

class Armor(Item):
	
	def __init__(self, name, id, price, size, ap):
		super().__init__(name, id, price, size)
		self.ap = ap

class Helmet(Armor):
	
	pass

class Chest(Armor):

	pass

#Consumables

class Consumable(Item):

	def __init__(self, name, id, price, size, amount):
		super().__init__(name, id, price, size)
		self.amount = amount

class Potion(Consumable):

	pass

class HealPotion(Potion):

	pass

class DamageReductionPotion(Potion):
	
	pass


if __name__ == "__main__":
	print("Items.py")
