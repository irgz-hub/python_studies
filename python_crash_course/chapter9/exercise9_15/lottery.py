from random import choice

def winner_ticket():
    list_lottery = list(range(10))
    string = "abcde"

    for letter in string:
        list_lottery.append(letter)

    char_choice = ""
    for i in range(4):
        char_choice += f"{choice(list_lottery)}"

    return char_choice
