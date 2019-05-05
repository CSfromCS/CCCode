#simple rock paper scissors game vs. bot! please enjoy lol
from random import choice

actions=["rock", "paper", "scissors"]
botP = 0
playerP = 0
    
def game():
    bot=choice(actions)

    player = askChoice()
    
    print("\nThe bot played", str.capitalize(bot) + ".")

    fight(player, bot)
    dispScores()
    askReplay()
        
def askChoice():
        choice=input("What hand will you play? [rock, paper, scissors]: ")
        if choice in actions:
                return choice
        else:
                print("\nInvalid keyword. Please enter a correct value.\n")
                return askChoice()

def fight(hand1, hand2):
    hand1 = actions.index(hand1)
    hand2 = actions.index(hand2)

    global botP, playerP
    if(hand1 == hand2):
            print("Draw! You both played",actions[hand1]+"!")
            botP += 0.5
            playerP += 0.5
    elif(hand1 == (hand2 + 1)%3):
            print("Congratulations! You won against this bot! You must be proud!")
            playerP += 1
    else:
            print("You loser! You lost to a simple bot!")
            botP += 1

def dispScores():
        print("\n-----SCORE BOARD------")
        print("  Bot - - - - - -",botP)
        print("  You - - - - - -",playerP)
        if(botP == playerP):
                print("----------TIE---------\n")
        elif(botP > playerP):
                print("----Bot is Winning----\n")
        else:
                print("----You are Winning----\n")

def askReplay():
        if input("Do you want to play again? [yes/no]") == "yes":
                game()
        else:
                print("\n\nGame over. Thank you for playing. Goodbye!")


if __name__ == "__main__":
    print("Welcome to rps.py! Let's play RockPaperScissors.\n")
    game()

#ronyobhelcastro04.05.19
        
#cs 05-5-19
