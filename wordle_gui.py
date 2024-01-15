# Name: Zuhair Merali
# UTEID: zsm386
#
# On my honor, Zuhair Merali, this programming assignment is my own work
# and I have not provided this code to any other student.
#
# Explain your addded feature here:
# My added feature was that I made a hint button that when pressed randomly
# gives the user one of the letters that he has not already guessed
# correctly. The user has the freedom to decide how many hints he would
# like to use.
# I also made it so backspace/delete works as undo letter and
# enter/return works as enter guess
#

import random
from tkinter import *
from tkinter import ttk


def get_words():
    """ Read the words from the dictionary files.
        We assume the two required files are in the current working
        directory.
        The file with the words that may be picked as the secret words is
        assumed to be names secret_words.txt. The file with the rest of the
        words that are valid user input but will not be picked as the
        secret
        word are assumed to be in a file named other_valid_words.txt.
        Returns a sorted tuple with the words that can be
        chosen as the secret word and a set with ALL the words,
        including both the ones that can be chosen as the secret word
        combined with other words that are valid user guesses.
    """
    temp_secret_words = []
    with open('secret_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            temp_secret_words.append(line.strip().upper())
    temp_secret_words.sort()
    secret_words = tuple(temp_secret_words)
    all_words = set(secret_words)
    with open('other_valid_words.txt', 'r') as data_file:
        all_lines = data_file.readlines()
        for line in all_lines:
            all_words.add(line.strip().upper())
    return secret_words, all_words


class WordleBoard:
    def __init__(self):
        self.__secret_words, self.__all_words = get_words()
        self.__target_word = random.choice(self.__secret_words)
        print(self.__target_word)
        self.__feedback = []

    def guess_check(self, guess):
        self.__feedback = ['-'] * len(self.__target_word)
        already_checked = list(self.__target_word)
        for i in range(len(self.__target_word)):
            if self.__target_word[i] == guess[i]:
                self.__feedback[i] = 'G'
                already_checked.remove(guess[i])

        for i in range(len(self.__target_word)):
            if guess[i] in self.__target_word and (
                    guess[i] != self.__target_word[i]) and guess[i] \
                    in already_checked:
                self.__feedback[i] = 'O'
                already_checked.remove(guess[i])

        return self.__feedback

    def valid_word(self, guess):
        if guess in self.__all_words:
            return True
        else:
            return False

    def get_hint(self, labels, guess_num):
        green_indices = []
        for row in labels:
            curr_index = 0
            for let in row:
                if let.cget("background") == "green":
                    green_indices.append(curr_index)
                curr_index += 1
        non_green_indices = [0, 1, 2, 3, 4]
        for num in reversed(non_green_indices):
            if green_indices.__contains__(num):
                non_green_indices.remove(num)
        print(non_green_indices)
        if not non_green_indices:
            return None, None

        hint_index = random.choice(non_green_indices)
        return hint_index, self.__target_word[hint_index]

    def get_secret_word(self):
        return self.__target_word


def set_letter(let, labels, guess_num, info_var):
    if labels[guess_num[0]-1][4].cget("text") != ' ':
        info_var.set(
            "You must enter your guess before proceeding")
    done = 0
    curr_row = 1
    if let == "Delete":
        undo_last_pick(labels, guess_num)
    let = let.upper()
    if let.isalpha():
        for i in labels:
            for j in i:
                if j.cget("text") == ' ' and done == 0 and guess_num[0] \
                        == curr_row:
                    j.config(text=let)
                    done += 1
            curr_row += 1


def main():
    guess_num = [1]
    root = Tk()
    root.title("Wordle")
    root.geometry('700x550')
    root.resizable(False, False)
    board = [WordleBoard()]
    labels = create_labels(root)
    guess = []
    info_label, info_var = create_control_buttons(root, labels, guess,
                                                  board, guess_num)
    root.bind('<KeyPress>', lambda event: set_letter(
        event.char, labels, guess_num, info_var))

    root.bind('<BackSpace>',
              lambda event:  undo_last_pick(labels, guess_num))
    root.bind('<Return>',
              lambda event: enter_guess(labels, board, info_var,
                                        guess_num))
    # A list of Strings of length 1 that stores the current user guess.

    root.mainloop()


def create_labels(root):
    """
    Create the frame for the color labels and feedback.
    The letter labels are used to show what letters/word the user
    has guessed for the current round of Wordle.
    The feedback variables shall be used to show the result of
    black or white when the user enters a guess.
    :param root: The root window.
    :return: Two lists. The list of feedback StringVars to place
    feedback from guesses and a list of lists of labels.
    """
    label_frame = ttk.Frame(root, padding="3 3 3 3")
    label_frame.grid(row=1, column=2)
    labels = []
    for row in range(1, 7):
        label_row = []
        for col in range(1, 6):
            label = Label(label_frame, font='Courier 60 bold', text=' ',
                          borderwidth=3, relief='solid', )
            label.grid(row=row, column=col, padx=2, pady=2)
            label_row.append(label)
        labels.append(label_row)
    return labels


def create_control_buttons(root, labels, guess, board, guess_num):
    """
    Create the main control buttons to undo a guess and
    enter a guess. Also, a label for information to show user.
    :param root: The root window.
    :param labels: The labels. These color of these will change in response
    to  the user pressing a button.
    :param guess: A list of strings of length 1 that stores the current
    user guess
    :param board: The Wordle board.
    """
    bottom_frame = ttk.Frame(root)
    bottom_frame.grid(row=3, column=1, columnspan=3)
    # To give the user information on errors and inform them when they win.
    info_var = StringVar()

    hint_button = Button(bottom_frame, font='Arial 24 bold',
                         text='Hint',
                         command=lambda: provide_hint(labels, board,
                                                      guess_num, info_var))
    hint_button.grid(row=1, column=4, padx=5, pady=5)

    new_game_button = Button(bottom_frame, font='Arial 24 bold',
                             text='New Game',
                             command=lambda: reset_game(labels, board,
                                                        guess_num,
                                                        info_var))
    new_game_button.grid(row=1, column=1, padx=5, pady=5)
    undo_button = Button(bottom_frame, font='Arial 24 bold',
                         text='Undo Guess',
                         command=lambda: undo_last_pick(labels, guess_num))
    undo_button.grid(row=1, column=2, padx=5, pady=5)
    enter_guess_button = Button(bottom_frame, font='Arial 24 bold',
                                text='Enter Guess',
                                command=lambda: enter_guess(labels, board,
                                                            info_var,
                                                            guess_num))
    enter_guess_button.grid(row=1, column=3, padx=5, pady=5)
    info_var.set("Enter a 5 letter word")
    info_label = ttk.Label(bottom_frame, font='Arial 18 bold',
                           textvariable=info_var)
    info_label.grid(row=3, column=1, columnspan=3)

    return info_label, info_var


def enter_guess(labels, board, info_var, guess_num):
    curr_row = 1
    for row in labels:
        if row[4].cget("text") != ' ' and curr_row == guess_num[0]:
            guess_str = ''
            guessList = []
            for letter in row:
                guessList.append(letter.cget("text"))
                guess_str += letter.cget("text")
            print(guessList)
            if board[0].valid_word(guess_str):
                feedback = board[0].guess_check(guessList)
                print(feedback)
                set_colors(row, feedback)
                if feedback == ['G', 'G', 'G', 'G', 'G']:
                    won_game(curr_row, info_var)
                else:
                    guess_num[0] += 1
            else:
                info_var.set("Word is invalid. Please Try again")
            break
        else:
            info_var.set("Guess must be 5 letters")
        curr_row += 1
    for let in labels[5]:
        if let.cget("text") != ' ' and let.cget("background") != "green":
            info_var.set("Game over. Secret Word was " +
                         board[0].get_secret_word())


def set_colors(wordRow, feedback):
    for i in range(len(wordRow)):
        if feedback[i] == 'G':
            wordRow[i].configure(background="green")
        if feedback[i] == 'O':
            wordRow[i].configure(background="yellow")
        if feedback[i] == '-':
            wordRow[i].configure(background="light gray")


def won_game(num_guesses, info_var):
    if num_guesses == 1:
        info_var.set("You win. Genius!")
    elif num_guesses == 2:
        info_var.set("You win. Magnificent!")
    elif num_guesses == 3:
        info_var.set("You win. Impressive!")
    elif num_guesses == 4:
        info_var.set("You win. Splendid!")
    elif num_guesses == 5:
        info_var.set("You win. Great!")
    elif num_guesses == 6:
        info_var.set("You win. Phew!")


def undo_last_pick(labels, guessNum):

    row_num = 1
    undo_switch = 0
    for row in labels:
        if row_num == guessNum[0]:
            for let in row:
                if let.cget("background") == "green":
                    undo_switch += 1
            if undo_switch != 5:
                for i in reversed(range(len(row))):
                    if row[i].cget("text") != ' ':
                        row[i].configure(text=' ')
                        break
        row_num += 1


def reset_game(labels, board, guessNum, info_var):
    for row in labels:
        for let in row:
            let.configure(text=' ', background="white")

    board[0] = WordleBoard()
    guessNum[0] = 1
    info_var.set(" ")


def provide_hint(labels, board, guess_num, info_var):
    hint_index, hint_letter = board[0].get_hint(labels, guess_num)
    if hint_index is None:
        info_var.set("All correct letters have been guessed.")
        return

    row_num = 1
    for row in labels:
        if row_num == guess_num[0]:
            row[hint_index].configure(text=hint_letter)
            break
        row_num += 1
    info_var.set(f"Hint: Letter {hint_index + 1} is {hint_letter}")


if __name__ == '__main__':
    main()
