#!/usr/bin/env python3
# This program calculates the sequence generated by the Collatz proces

def collatz(number):
	if number % 2 == 0: # divide by 2 if even number
		number = number // 2
	else :
		number = 3 * number + 1 # recalculate if odd nummber
	return number

number = input("Please enter a number greater than or equal to 2: ")

try: #check if a non-numeric value is input
	number = int(number)

	if number < 2: # check if the input number is valid
		print("You entered " + str(number) + ". Please enter a number greater " + \
		"than or equal to 2.") 
	else:
		print(number)
		while number > 1:   #check if the Collatz process is completed, i.e. 1 is
                                    #reached
			number = collatz(number)
			print(number)
except ValueError: #issue error msg if non-numeric value is input
	print("You entered " + number + ". Please enter a number greater " + \
	"than or equal to 2.") 
	

