import random
import time

roll_again ="yes"
bet_more = "no"

while roll_again == "yes" or roll_again == "y":
	time.sleep(0.2)
	roll1 = random.randint(1,6)
	roll2 = random.randint(1,6)
	roll3 = random.randint(1,6)
	rolls = sorted([roll1, roll2, roll3])
	print(rolls)
	time.sleep(0.5)
	roll_again = input("Should I roll again? (yes or no) >> " )

while roll_again == "no":
	roll_again = input("You want to bet more? (yes or no) >> ")
	bet_more ="yes"
	print("Add more money to the pile... (you have 10 seconds)")

while bet_more == "yes":
	time.sleep(0.2)
	roll1 = random.randint(1,6)
	roll2 = random.randint(1,6)
	roll3 = random.randint(1,6)
	rolls = sorted([roll1, roll2, roll3])
	print(rolls)
	roll_again = input("Should I roll again? (yes or no) >> " )



	




	
	

	