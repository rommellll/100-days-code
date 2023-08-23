import pandas
import turtle
from board import Board


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
board = Board()
guessed = []
missed_state = []
score = 0
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/ {len(all_states)} States correct",
                                    prompt="What's another state?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed:
                missed_state.append(state)

        data = pandas.DataFrame(missed_state)
        data.to_csv("./learning.csv")
        break
    if (answer_state in all_states) and (answer_state not in guessed):
        state_data = data[data.state == answer_state]
        state_x_pos = int(state_data.x.item())
        state_y_pos = int(state_data.y.item())
        board.update_board(answer_state, state_x_pos, state_y_pos)
        guessed.append(answer_state)
        score += 1
    if score == 50:
        game_is_on = False
        board.game_over()