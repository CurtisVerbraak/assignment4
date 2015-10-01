import sys
from random import randint

#de grbuiker kiest hier een optie
user2 = raw_input("type true or false for user 2 to join\n")
user = raw_input("Chose one! rock, paper, scissors, spock, lizard?\n")


if user2 == "false":
#deze functie genereerd een willekeurig nummer vanaf de 0 tot en met de 4
	player2 = "the computer"
	random = randint(0,4)

	#deze if elif else kijtk wat het resultaat is van de willekeurig gegenereerde nummer in de functie hier boven
	#vervolgens koppeld die een nummer aan een string, 1 = paper , 3 = spock enzovoort
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

else:
	player2 = "user2"
	computer = raw_input("user2 Chose one! rock, paper, scissors, spock, lizard?\n")

sys.stdout.write(' you have chosen for: '+ user + '!\n')
sys.stdout.write(' '+ player2 +' has chosen for: '+ computer + '!\n')

#rock, computer or user2 win siutuation
if computer == "rock" and user == "lizard":
	sys.stdout.write(''+ player2 +' won! Rock smashes Lizard!\n')
elif computer == "rock" and user == "scissors":
	sys.stdout.write(''+ player2 +' won! Rock crushes scissors\n')
#user win situation
elif computer == "rock" and user == "spock":
	sys.stdout.write('the user won! spock vaporize rock\n')
elif computer == "rock" and user == "paper":
	sys.stdout.write('the user won! paper covers rock!\n')

#lizard, computer or user2 win siutuation
elif computer == "lizard" and user == "paper":
	sys.stdout.write(''+ player2 +' won! lizard eats paper!\n')
elif computer == "lizard" and user == "spock":
	sys.stdout.write(''+ player2 +' won! lizard poisons spock!\n')
#user win situation
elif computer == "lizard" and user == "scissors":
	sys.stdout.write('the user won! scissor decapitates lizard!\n')
elif computer == "lizard" and user == "rock":
	sys.stdout.write('the user won! rock crushes lizard!\n')

#spock, computer or user2 win siutuation
elif computer == "spock" and user == "scissors":
	sys.stdout.write(''+ player2 +' won! spock smashes scissors!\n')
elif computer == "spock" and user == "rock":
	sys.stdout.write(''+ player2 +' won! spock vaporizes rock!\n')
#user win situation
elif computer == "spock" and user == "paper":
	sys.stdout.write('the user won! paper disproves spock\n')
elif computer == "spock" and user == "lizard":
	sys.stdout.write('the user won! lizard poisons spock!\n')

#scissors, computer or user2 win siutuation
elif computer == "scissors" and user == "paper":
	sys.stdout.write(''+ player2 +' won! scissors cuts paper\n')
elif computer == "scissors" and user == "lizard":
	sys.stdout.write('the '+ player2 +' won! scissors decapitates lizard\n')
#user win situation
elif computer == "scissors" and user == "spock":
	sys.stdout.write('the user won! spock smashes scissors \n')
elif computer == "scissors" and user == "rock":
	sys.stdout.write('the user won! rock crushes scissors\n')

#paper, computer or user2 win siutuation
elif computer == "paper" and user == "spock":
	sys.stdout.write(''+ player2 +' won! paper disproves spock!\n')
elif computer == "paper" and user == "rock":
	sys.stdout.write(''+ player2 +' won! paper covers rock!\n')
#user win situation
elif computer == "paper" and user == "lizard":
	sys.stdout.write('the user won! lizard eats paper!\n')
elif computer == "paper" and user == "scissors":
	sys.stdout.write('the user won! scissors cuts paper!\n')

#gelijkspel user en computer heben dezelfde keus
else:
	sys.stdout.write('draw!\n')