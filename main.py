import random
from turtle import Turtle, Screen


def getWinner(listOfTurtles):
    contender = listOfTurtles[0]
    for t in listOfTurtles:
        if t.xcor() > contender.xcor():
            contender = t
    return contender


screen = Screen()
screen.title("Turtle Race")
t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")
turtles = [t1, t2, t3, t4, t5]
startingPositions = [-100, -50, 0, 50, 100]
turtleColors = ["purple", "pink", "blue", "green", "orange"]

for index in range(0, 5):
    turtles[index].penup()
    turtles[index].color(turtleColors[index])
    turtles[index].setx(-450)
    turtles[index].sety(startingPositions[index])

# TODO 1. Make betting optional so game doesn't crash on blank entry
# TODO 2. Verify entry so game doesn't accept invalid entries
playerBet = screen.textinput("Place your bet!", "Who do you want to bet on?\n(Purple/Pink/Blue/Green/Orange)").lower()

# TODO 3. Make the game replayable without exiting the program

while True:
    if t1.xcor() >= 450 or t2.xcor() >= 450 or t3.xcor() >= 450 or t4.xcor() >= 450 or t5.xcor() >= 450:
        break
    else:
        for turtle in turtles:
            turtle.forward(random.randint(1, 6))

winner = getWinner(turtles)

if winner == t1:
    print("The winner is Purple!")
elif winner == t2:
    print("The winner is Pink!")
elif winner == t3:
    print("The winner is Blue!")
elif winner == t4:
    print("The winner is Green!")
elif winner == t5:
    print("The winner is Orange!")

if winner == t1 and playerBet == "purple":
    print("You've won the bet!")
elif winner == t2 and playerBet == "pink":
    print("You've won the bet!")
elif winner == t3 and playerBet == "blue":
    print("You've won the bet!")
elif winner == t4 and playerBet == "green":
    print("You've won the bet!")
elif winner == t5 and playerBet == "orange":
    print("You've won the bet!")
else:
    print(f"Unfortunately {playerBet.capitalize()} didn't win the race this time...\n")

screen.screensize()
screen.exitonclick()
