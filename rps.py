#simple rock paper scissors game vs. bot! please enjoy lol

def welcome():
	print("\nLet's play Rock, Paper, Scissors! What hand will you play?")
def rpsfunction():
	#bot
	player1=["rock", "paper", "scissors"]
	import random
	x=random.choice(player1)
	r="rock"
	p="paper"
	s="scissors"
	
	play=input()
	
	#if bot is rock
	print("\nThe bot played "+str.capitalize(x))
	if x==r:
		if play==r:
			print("Draw! Pick a hand again!")
			rpsfunction()
		elif play==p:
			print("Congratulations! You won against this bot! You must be proud!")
			print("Try again? (yes or no)")
			yn=input()
			if yn=="yes":
				welcome()
				rpsfunction()
			if yn=="no":
				print("Game Over.")
				return
		elif play==s:
			print("You loser! You lost to a simple bot!")
			print("Try again? (yes or no)")
			yn=input()
			if yn=="yes":
				welcome()
				rpsfunction()
			if yn=="no":
				print("Game Over.")
				return
		else:
			print("Invalid keyword")
			rpsfunction()
	
	#if bot is paper
	if x==p:
		if play==p:
			print("Draw! Pick a hand again!")
			rpsfunction()
		elif play==s:
			print("Congratulations! You won against this bot! You must be proud!")
			print("Try again? (yes or no)")
			yn=input()
			if yn=="yes":
				welcome()
				rpsfunction()
			if yn=="no":
				print("Game Over.")
				return
		elif play==r:
			print("You loser! You lost to a simple bot!")
			print("Try again? (yes or no)")
			yn=input()
			if yn=="yes":
				welcome()
				rpsfunction()
			if yn=="no":
				print("Game Over.")
				return
		else:
			print("Invalid keyword")
			rpsfunction()
		
	#if bot is scissors
	if x==s:
		if play==s:
			print("Draw! Pick a hand again!")
			rpsfunction()
		elif play==r:
			print("Congratulations! You won against this bot! You must be proud!")
			print("Try again? (yes or no)")
			yn=input()
			if yn=="yes":
				welcome()
				rpsfunction()
			if yn=="no":
				print("Game Over.")
				return
		elif play==p:
			print("You loser! You lost to a simple bot!")
			print("Try again? (yes or no)")
			yn=input()
			if yn=="yes":
				welcome()
				rpsfunction()
			if yn=="no":
				print("Game Over.")
				return
		else:
			print("Invalid keyword")
			rpsfunction()		
	
print("Let's play Rock, Paper, Scissors! What hand will you play?\n(pick: rock, paper, or scissors?)")
rpsfunction()

#ronyobhelcastro04.05.19
