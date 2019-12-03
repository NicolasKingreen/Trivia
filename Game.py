import Entities
import Items
import Helper
import random

def spawn_monster(player, level):
	enemy = Entities.Enemy(level)
	print("1. Fight")
	print("2. Escape")
	decision = int(input("Make your Turn: "))
	print("")
	if decision == 1:
		damage = enemy.get_hp()
		earned_gold = enemy.get_gold_on_drop()
		earned_xp = enemy.get_xp_on_kill()

		player.set_hp(player.get_hp() - damage)
		player.set_gold(player.get_gold() + earned_gold)
		player.set_xp(player.get_xp() + earned_xp)
	else:
		damage = int(enemy.get_hp() / 2)
		earned_xp = int(enemy.get_xp_on_kill() / 2)

		player.set_hp(player.get_hp() - damage)
		player.set_xp(player.get_xp() + earned_xp)
	print(f"*You Lost {damage} HP and Earn {earned_gold} gold & {earned_xp} XP*")

def main():
	day = 1
	player = Entities.Player("Kingreen")
	while player.is_alive == True:
		print(f"\n------------Day {day} - {player.get_nickname()} ({player.get_hp()} HP): {player.get_gold()} gold, {player.get_level()} level ({player.get_xp()}/100 xp)------------\n")
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
		day += 1
	print("You're dead!")


if __name__ == '__main__':
	main()