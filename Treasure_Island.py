#Steven Vandegrift 2022
print("Welcome to Treasure Island")
choice1 = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n")
if choice1 == 'left':
	choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
	if choice2 == "wait":
		choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
		if choice3 == "red":
			print("It's a room full of fire. Game Over.")
		elif choice3 == "yellow":
			print("You found the treasure! You Win!")
		elif choice3 == "blue":
			print("You enter a room of beasts. Game Over.")
		else:
			print("You chose a door that doesn't exist. Game Over.")
	elif choice2 == "swim":
		print("You get attacked by an angry trout. Game Over.")
	else:
		print("Not an option, Game Over")
elif choice1 == 'right':
	print("You fell into a hole. Game Over.")
else:
	print("Not an option, Game Over")