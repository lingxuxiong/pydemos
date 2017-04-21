# Python program to illustrate a loop with condition at the bottom
# Roll a dice untill user chooses to exit
# https://www.programiz.com/python-programming/looping-technique

import random


while True:
	raw_input('Press Enter to roll the dice:')
	
	num = random.randint(1, 6)
	print('You got {}'.format(num))

	choice = raw_input('Roll agin?(y/n)')

	if (choice == 'n'):
		break; 