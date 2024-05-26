import turtle as t
import random
is_race_on = False
screen = t.Screen()
screen.setup(width=800, height=500)
user_bet=screen.textinput(title = "Do you wanna bet?", prompt= "Type a color you want to bet on." )
screen.title("Turtle Race Game")
y_position = [-120,-60,0,60,120]
colours = ["red" , "blue", "green" , "purple", "orange"]
all_turtles = []
for turtle_index in range(5):
    tim = t.Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.speed(0)
    tim.penup()
    tim.goto(-350,y_position[turtle_index])
    all_turtles.append(tim)
if user_bet:
    is_race_on =bool(user_bet)

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 355:
                is_race_on =False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"Yay!, You Win with color {winner} turtle")
                else:
                    print(f"You lose, The winner is {winner} turtle")
                


            pace= random.randint(0,10)
            turtle.forward(pace)


screen.exitonclick()