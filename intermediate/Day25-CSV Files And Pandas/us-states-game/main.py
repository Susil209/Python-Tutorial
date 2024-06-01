import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")

image_path = 'blank_states_img.gif'
# add image to the screen
screen.addshape(image_path)

turtle.shape(image_path)

states = pd.read_csv('50_states.csv')
list_of_states = states['state'].to_list()  # covert to list
# print(list_of_states)

guessed_states = []


# print(answer_state)

# for state in list_of_states:
#     if state.lower() == answer_state.lower():
#         print(f"{states['x']},{states['y']}")


while len(guessed_states) < len(list_of_states):

    # popup box
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/{len(list_of_states)} Guess the state?",
                                    prompt='Enter the next state:').title()  # title case

    # exit out of the loop
    # if answer_state == 'Exit':
    #     missed_states = []
    #     for state in list_of_states:
    #         if state not in guessed_states:
    #             missed_states.append(state)
    #
    #     # print(missed_states)
    #     # create a new dataframe for missing states
    #     new_df = pd.DataFrame(missed_states)
    #
    #     # convert to csv
    #     new_df.to_csv("states_to_learn.csv")
    #     break

    # using list comprehension
    if answer_state == 'Exit':
        missed_states = [state for state in list_of_states if state not in guessed_states]
        print(missed_states)
        new_df = pd.DataFrame(missed_states)
        new_df.to_csv("states_to_learn.csv")
        break

    # if the provided answer state is in the list of states
    if answer_state in list_of_states:
        # add answer in guessed states
        guessed_states.append(answer_state)

        # create a turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = states[states['state'] == answer_state]
        # print(state_data)
        # print(type(state_data))

        x_cor = int(state_data.iloc[0, 1])
        y_cor = int(state_data.iloc[0, 2])
        t.goto(x_cor, y_cor)  # goto states x and y coordinate

        # write the name of state
        t.write(arg=state_data.iloc[0, 0])


# screen.exitonclick()


