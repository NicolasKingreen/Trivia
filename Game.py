import Entities
import Items
import Helper
import random

def spawn_monster(player, level):
	enemy = Entities.Enemy(level)
	print("1. Fight")
	print("2. Escape")
	decision = int(input("Make your Turn: "))
	if decision == 1:
		player.set_hp(player.get_hp() - enemy.get_hp())
		player.set_gold(player.get_gold() + enemy.get_gold_on_drop())
		player.set_xp(player.get_xp() + enemy.get_xp_on_kill())
	else:
		player.set_hp(player.get_hp() - int(enemy.get_hp() / 2))
		player.set_xp(player.get_xp() + int(enemy.get_xp_on_kill() / 2))

def main():
	day = 1
	player = Entities.Player("Kingreen")
	while player.is_alive == True:
		print(f"\n\t\t\tDay {day} - {player.get_nickname()} ({player.get_hp()} HP): {player.get_gold()} gold, {player.get_level()} level ({player.get_xp()}/100 xp)\n")
		today_monster_levels = Helper.replacements_with_3()
		print(f"Today's Chanses: {today_monster_levels}")
		print("1. Go Forward")
		print("2. Go Right")
		print("3. Go Left")
		decision = int(input("Make your Turn: "))
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