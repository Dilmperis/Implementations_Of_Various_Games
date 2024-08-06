import turtle
import pandas as pd

usa_states = pd.read_csv("50_states.csv")

# Create display screen
screen = turtle.Screen()
screen.title("U.S.A states Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def show_all_states():
    for remaining_state in states.copy():  # Use a copy of the list to iterate safely
        if remaining_state in states:  # Ensure the state is still in the list
            x = usa_states[usa_states["state"] == remaining_state]["x"].iloc[0]
            y = usa_states[usa_states["state"] == remaining_state]["y"].iloc[0]

            states.remove(remaining_state)

            tk = turtle.Turtle()
            tk.hideturtle()
            tk.penup()
            tk.goto(x, y)
            tk.write(remaining_state, align="center", font=("Arial", 10, "bold"))


# Button drawing for 'Give Up'
button_turtle = turtle.Turtle()
button_turtle.penup()
button_turtle.hideturtle()

#  button dimensions
button_width = 200
button_height = 40

# Bottom-left corner of the button
button_x = -300
button_y = -300

button_turtle.goto(button_x, button_y)
button_turtle.pendown()
button_turtle.begin_fill()
button_turtle.fillcolor("lightblue")
for _ in range(2):
    button_turtle.forward(button_width)
    button_turtle.left(90)
    button_turtle.forward(button_height)
    button_turtle.left(90)
button_turtle.end_fill()
button_turtle.penup()

# Calculate the center position for the text
text_x = button_x + (button_width / 2)
text_y = button_y + (button_height / 2) - 10

button_turtle.goto(text_x, text_y)
button_turtle.write("For Giving up, type exit", align="center", font=("Arial", 12, "normal"))

remaining_states = 50
states = usa_states["state"].tolist()

while remaining_states > 0:
    user_input = screen.textinput(f"Remaining states: {remaining_states}", "Please enter a state:").title()

    if user_input in states:
        x = usa_states[usa_states["state"] == user_input]["x"].iloc[0]
        y = usa_states[usa_states["state"] == user_input]["y"].iloc[0]

        remaining_states -= 1
        states.remove(user_input)

        tk = turtle.Turtle()
        tk.hideturtle()
        tk.penup()
        tk.goto(x, y)
        tk.write(user_input, align="center", font=("Arial", 10, "bold"))
    elif user_input == "Exit":
        show_all_states()
        break  # Exit the loop after showing all states

turtle.mainloop()
screen.exitonclick()
