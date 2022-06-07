from Dice import *

gamer1Dice = sixDice()
gamer2Dice = sixDice()
gamer3Dice = sixDice()

for i in range(5):
	gamer1Dice.playDice()
	gamer2Dice.playDice()
	gamer3Dice.playDice()

sumGamer1 = gamer1Dice.getSum()
sumGamer2 = gamer2Dice.getSum()
sumGamer3 = gamer3Dice.getSum()

print('Gamer1:', gamer1Dice.getNumbers())
print('Sum of Gamer1:', sumGamer1)
print('======')
print('Gamer2:', gamer2Dice.getNumbers())
print('Sum of Gamer2:', sumGamer2)
print('======')
print('Gamer3:', gamer3Dice.getNumbers())
print('Sum of Gamer3:', sumGamer3)
print('======')

sortedNumbers = sortNumbers(sumGamer1, sumGamer2, sumGamer3)
print("Winner's Score:", sortedNumbers[0])