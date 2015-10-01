import sys
from random import randint

#de grbuiker kiest hier een optie
user = raw_input("Chose one! rock, paper, scissors, spock, lizard?\n")

#deze functie genereerd een willekeurig nummer vanaf de 0 tot en met de 4
random = randint(0,4)

#deze if elif else kijtk wat het resultaat is van de willekeurig gegenereerde nummer in de functie hier boven
#vervolgens koppeld die een nummer aan een string, 1 = paper , 3 = spok enzovoort
if random == 0:
    computer = "rock"
elif random == 1:
    computer = "paper"
elif random == 2:
    computer = "scissors"
elif random == 3:
	computer = "spock"
else:
	computer = "lizard"

sys.stdout.write(' you have chosen: '+ user + '!\n')
sys.stdout.write(' the computer has chosen: '+ computer + '!\n')
#rock
if computer == "rock" and user == "lizard":
	sys.stdout.write('the computer won! Rock smashes Lizard!\n')
elif computer == "rock" and user == "scissors":
	sys.stdout.write('the computer won! Rock crushes scissors\n')

elif computer == "rock" and user == "spock":
	sys.stdout.write('the user won! spock vaporize rock\n')
elif computer == "rock" and user == "paper":
	sys.stdout.write('the user won! paper covers rock!\n')

#lizard
elif computer == "lizard" and user == "paper":
	sys.stdout.write('the computer won! lizard eats paper!\n')
elif computer == "lizard" and user == "spock":
	sys.stdout.write('the computer won! lizard poisons spock!\n')

elif computer == "lizard" and user == "scissors":
	sys.stdout.write('the user won! scissor decapitates lizard!\n')
elif computer == "lizard" and user == "rock":
	sys.stdout.write('the user won! rock crushes lizard!\n')

#spock
elif computer == "spock" and user == "scissors":
	sys.stdout.write('the computer won! spock smashes scissors!\n')
elif computer == "spock" and user == "rock":
	sys.stdout.write('the computer won! spock vaporizes rock!\n')

elif computer == "spock" and user == "paper":
	sys.stdout.write('the user won! paper disproves spock\n')
elif computer == "spock" and user == "lizard":
	sys.stdout.write('the user won! lizard poisons spock!\n')

#scissors
elif computer == "scissors" and user == "paper":
	sys.stdout.write('the computer won! scissors cuts paper\n')
elif computer == "scissors" and user == "lizard":
	sys.stdout.write('the computer won! scissors decapitates lizard\n')

elif computer == "scissors" and user == "spock":
	sys.stdout.write('the user won! spock smashes scissors \n')
elif computer == "scissors" and user == "rock":
	sys.stdout.write('the user won! rock crushes scissors\n')

#paper
elif computer == "paper" and user == "spock":
	sys.stdout.write('the computer won! paper disproves spock!\n')
elif computer == "paper" and user == "rock":
	sys.stdout.write('the computer won! paper covers rock!\n')

elif computer == "paper" and user == "lizard":
	sys.stdout.write('the user won! lizard eats paper!\n')
elif computer == "paper" and user == "scissors":
	sys.stdout.write('the user won! scissors cuts paper!\n')

#gelijkspel user en computer heben dezelfde keus
else:
	sys.stdout.write('draw!\n')