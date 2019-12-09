#Version 0.1.101a

import Entities
import Items
import Shop
import Helper

import os
import random
import pickle

VERSION = "0.1.101a"

def spawn_monster(player, level):
	enemy = Entities.Enemy(level)
	print("1. Fight")
	print("2. Escape")
	decision = int(input("Make your Turn: "))
	print("")
	if decision == 1:
		damage = enemy.get_hp() - player.get_ap()
		earned_gold = enemy.get_gold_on_drop()
		earned_xp = enemy.get_xp_on_kill()

		player.set_hp(player.get_hp() - damage)
		player.set_gold(player.get_gold() + earned_gold)
		player.set_gold_earned(player.get_gold_earned() + earned_gold)
		player.set_xp(player.get_xp() + earned_xp)
	else:
		damage = int(enemy.get_hp() / 2)
		earned_gold = 0
		earned_xp = int(enemy.get_xp_on_kill() / 2)

		player.set_hp(player.get_hp() - damage)
		player.set_xp(player.get_xp() + earned_xp)
	print(f"*You Lost {damage} HP and Earn {earned_gold} gold & {earned_xp} XP*")


def load_game():
	try:
		with open("Save.pickle", "rb") as load_file:
			player = pickle.load(load_file)
		return player
	except IOError as error:
		print("Error While Loading: ", str(error))
		return Entities.Player(input("Your name: "))
	except pickle.PickleError as error:
		print("Pickle Error: ", str(error))


def save_game(player):
	try:
		with open("Save.pickle", "wb") as save_file:
			pickle.dump(player, save_file)
			print("[Game has been saved...]")
	except IOError as error:
		print("Error While Saving: ", str(error))
	except pickle.PickleError as error:
		print("Picle Error: ", str(error))


def append_highscores(player):
	try:
		with open("High Scores.txt", "a") as highscores:
			highscores.write(f"{player.get_nickname()} (Level {player.get_level()}) died on day {player.get_day()} and earned {player.get_gold_earned()} gold\n")
	except IOError as error:
		print("Error While Appending High Scores: ", str(error))


def main():
	print(f"TRIVIA GAME - Lost & Earn ({VERSION})")
	player = load_game()
	#Game Loop
	while player.is_alive == True:

		#Info Bar
		print(f"\n------------Day {player.get_day()} - {player.get_nickname()} ({player.get_hp()} HP): {player.get_gold()} gold, {player.get_level()} level ({player.get_xp()}/100 xp)------------\n")

		today_monster_levels = Helper.replacements_with_3()
		#print(f"Today's Chanses: {today_monster_levels}")
		print("Menu")
		print("1. Go Forward")
		print("2. Go Right")
		print("3. Go Left")
		decision = int(input("Make your Turn: "))
		print("")
		if decision == 1:
			spawn_monster(player, today_monster_levels[0])
		elif decision == 2:
			spawn_monster(player, today_monster_levels[1])
		else:
			spawn_monster(player, today_monster_levels[2])
		player.update()
		player.set_day(player.get_day() + 1)
		save_game(player)
	print("You're dead!")
	os.remove("Save.pickle")
	append_highscores(player)



if __name__ == '__main__':
	main()