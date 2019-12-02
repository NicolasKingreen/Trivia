import random

def replacements_with_3():
	list = [int(random.random() * 3 + 1)]
	if list[0] == 1:
		if int(random.random() * 2) == 0:
			list.append(2)
			list.append(3)
		else:
			list.append(3)
			list.append(2)
	elif list[0] == 2:
		if int(random.random() * 2) == 0:
			list.append(1)
			list.append(3)
		else:
			list.append(3)
			list.append(1)
	else:
		if int(random.random() * 2) == 0:
			list.append(1)
			list.append(2)
		else:
			list.append(2)
			list.append(1)
	return list


if __name__ == "__main__":
	print("Please, run Game.py")
	