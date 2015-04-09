from random import randint
from util import util
import time
import datetime

# Keep track of correct answers
correct = 0

# Number of iterations in the test
ITERATIONS = 10

# Coordinates of bones to be tested
C1 = (0, 0, 0)
T1 = (0, 0, 0)
L1 = (0, 0, 0)

def askForBone(expectedPosition):
	global correct

	# Set up button
	buttonZ = polyModel(buttonPath, buttonModel)
	buttonPosition = buttonZ.getPositionOffset()

	# Set up button hand and navigation hand
	hand = polyModel(handPath, handButtModel)
	navHand = polyModel(navPath, handNavModel)

	# Wait for button press
	while (1):
		handPosition = hand.getPositionOffset()
		if (util.isOver(buttonPosition, handPosition, 1.5, 1.5)):
			# Get the position of the navigation hand and check if it is in the right place
			navPosition = navHand.getPositionOffset()
			if (util.isOver(navPosition, expectedPosition, 1.5, 1.5)):
				correct += 1

			# Draw a circle at the expected position

			time.sleep(2)
			# Delete circle


			break
	return


if __name__ == '__main__':
	old = 0
	new = 0

	# Begin timer
	startTime = time.time()

	for i in range(ITERATIONS):
		# Randomly choose a bone. Make sure we don't ask for same bone twice.
		while new == old:
			new = randint(1, 3)

		if new == 1:
			# Display text for bone we want in projector view

			askForBone(C1)

			# Delete text from view

		elif new == 2:
			# Display text for bone we want in projector view

			askForBone(T1)

			# Delete text from view
		else:
			# Display text for bone we want in projector view

			askForBone(L1)

			# Delete text from view

	# Get the time after the 10 iterations
	endTime = time.time()
	elapsedTime = endTime - startTime
	elapsedTime = str(elapsedTime)+" Seconds"

	# Calculate the accuracy
	accuracy = str((correct/ITERATIONS) * 100);

	# Write results to a file
	date = datetime.datetime.now().strftime("%B %d %I:%M%p")
	testName = "Skeleton Full"
	fileName = 'Results'+date;
	f = open(fileName,'w')
	f.write(testName+'\n')
	f.write(date+'\n')
	f.write(accuracy+'\n')
	f.write(elapsedTime+'\n')
	f.close()


