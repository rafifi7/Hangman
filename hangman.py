# Practice for coding and making guis
# Hangman
# Author: Rafee Adnan
# Date created: 12/21/2023

import tkinter as tk
from tkinter import font as tkFont
import customtkinter as ctk
from PIL import Image, ImageTk
import timer

#Global strings

g_letter_count = 0
g_blanks = ""
g_current_board = ""
g_phrase = ""
g_letters_guessed_display = ""
g_letters_guessed_dict = {}
g_phrase_dict = {}
g_blanks_indices = {}


#Picture 
g_pic = 0
file_path = "hangman_images/"
png= ".png"


#Global Fonts

title_font = ('Helvetica', 100, 'bold')
heading_font = ('Helvetica', 70, 'bold')
letters_font = ('Helvetica', 50, 'bold')
button_font =('Helvetica', 35, 'bold')
text_font=('Helvetica', 20, 'bold')

#GUI Functions

def press_play():
    for widget in root.winfo_children():
        widget.destroy()
    
    title_label = ctk.CTkLabel(root, text="Enter a word or phrase:", bg_color='lightblue', font=heading_font, text_color='black')
    title_label.place(relx=.5, rely=.15, anchor='center')

    text_var = tk.StringVar(root)

    def on_type(*args):
        current_text = text_var.get()
        uppercase_text = current_text.upper()
        text_var.set(uppercase_text)

    word_entry = ctk.CTkEntry(root, height=75, width=500, bg_color='lightblue', text_color='black', fg_color='white', placeholder_text='    Custom Word or Phrase', font=button_font, textvariable=text_var)

    text_var.trace_add('write', on_type)

    word_entry.place(relx=.5, rely=.35, anchor='center')

    submit_button = ctk.CTkButton(root, text="Submit", bg_color='lightblue', command=lambda: create_board(word_entry.get()), corner_radius=16, font=button_font, text_color='black', width=240, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    submit_button.place(relx=.5, rely=.55, anchor='center')

    main_menu_button = ctk.CTkButton(root, text="Main Menu", bg_color='lightblue', command=show_main_menu, corner_radius=16, font=button_font, text_color='black', width=240, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    main_menu_button.place(relx=.5, rely=.75, anchor='center')

def create_board(user_input):
    for widget in root.winfo_children():
        widget.destroy()

    global g_blanks, g_phrase, g_phrase_dict, g_current_board, g_blanks_indices
    g_phrase = user_input

    blanks_arr = []
    for letter in g_phrase: #fix this with regex in future
        if letter == " ":
            blanks_arr.append("   ")
        else:
            blanks_arr.append("_ ")

    blanks = ''.join(blanks_arr)

    blanks_indices = []

    g_phrase_with_spaces = g_phrase.split(" ")
    g_phrase = ''.join(g_phrase_with_spaces)

    for i in range(len(blanks)): #blanks_indices holds the index of each blank in order of the phrase
        if blanks[i] == '_':
            blanks_indices.append(i)

    for letter in g_phrase:
        if letter not in g_phrase_dict:
            g_phrase_dict[letter] = 1

    for let in range(len(g_phrase)):
        if g_phrase[let] not in g_blanks_indices:
            g_blanks_indices[g_phrase[let]] = [blanks_indices[let]]
        else:
            g_blanks_indices[g_phrase[let]].append(blanks_indices[let])

    g_blanks = blanks
    g_current_board = g_blanks
    
    blanks_label = ctk.CTkLabel(root, text=g_blanks, bg_color='lightblue', font=heading_font, text_color='black')
    blanks_label.place(relx=0.5, rely = 0.15, anchor='center')

    letters_used_frame = ctk.CTkFrame(root, height=400, width=260, bg_color='lightgreen', fg_color='lightgreen', border_color='black', border_width=8, corner_radius=0)
    letters_used_frame.place(relx=0.175, rely=.55, anchor='center')

    root.update_idletasks()

    letters_used_label = ctk.CTkLabel(letters_used_frame, text="Letters Used\n-------------------", font=button_font, text_color='black', bg_color='lightgreen')
    letters_used_label.place(relx=.5, rely=.15, anchor='center')

    show_image(g_pic)

    text_var = tk.StringVar(root)

    def limit_size(*args): #limits to single letter entry and makes letters capital
        value = text_var.get()
        if len(value) > 1 or not value.isalpha():
            text_var.set(value[:1].upper())
            return
        if value in g_letters_guessed_dict: #prevents them from guessing letters already guessed
            text_var.set("")
            return
        text_var.set(value.upper())

    letter_entry = ctk.CTkEntry(root, height = 75, width=80, bg_color='lightblue', fg_color='white', text_color='black', font=heading_font, textvariable=text_var)
    letter_entry.place(relx=.5, rely=.45, anchor='center')

    text_var.trace_add('write', limit_size)

    guess_button = ctk.CTkButton(root, text="Guess", bg_color='lightblue', command=lambda: update_board(letter_entry.get()), corner_radius=16, font=button_font, text_color='black', width=200, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    guess_button.place(relx=.5, rely=.65, anchor='center')



def game_over_checker():
    global g_pic, g_phrase_dict, g_phrase, g_blanks, g_current_board, g_letters_guessed_dict, g_letters_guessed_display, g_phrase_dict, g_letter_count
    if g_pic == 6:
        
        #create window that says you lose!
        lose_window = ctk.CTkToplevel(root)
        lose_window.title("Game Over")
        lose_window.geometry("400x300")
        lose_window.config(background='lightblue')
        lose_window.attributes('-topmost', True)

        lose_label = ctk.CTkLabel(lose_window, text="YOU LOSE!", font=heading_font, text_color='black', bg_color='lightblue')
        lose_label.place(relx=.5, rely=.25, anchor='center')

        main_menu_button = ctk.CTkButton(lose_window, text="Main Menu", bg_color='lightblue', command=show_main_menu, corner_radius=16, font=button_font, text_color='black', width=240, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
        main_menu_button.place(relx=.5, rely=.75, anchor='center')

        g_pic = 0
        g_letter_count = 0
        g_blanks=""
        g_current_board=""
        g_letters_guessed_display=""
        g_phrase=""
        g_letters_guessed_dict.clear()
        g_phrase_dict.clear()

        while(1):
            timer.sleep(20)
    
        
    #if intersection of g_phrase_dict and g_letters_guessed_dict == len(g_phrase_dict)
    if len(set(g_phrase_dict.keys()) & set(g_letters_guessed_dict.keys())) == len(g_phrase_dict):
        lose_window = ctk.CTkToplevel(root)
        lose_window.title("Game Over")
        lose_window.geometry("400x300")
        lose_window.config(background='lightblue')
        lose_window.attributes('-topmost', True)

        lose_label = ctk.CTkLabel(lose_window, text="YOU WIN!", font=heading_font, text_color='black', bg_color='lightblue')
        lose_label.place(relx=.5, rely=.25, anchor='center')

        main_menu_button = ctk.CTkButton(lose_window, text="Main Menu", bg_color='lightblue', command=show_main_menu, corner_radius=16, font=button_font, text_color='black', width=240, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
        main_menu_button.place(relx=.5, rely=.75, anchor='center')
        g_pic = 0
        g_letter_count = 0
        g_blanks=""
        g_current_board=""
        g_letters_guessed_display=""
        g_phrase=""
        g_letters_guessed_dict.clear()
        g_phrase_dict.clear()

        while (1):
            timer.sleep(20)

def update_board(letter):
    game_over_checker()

    for widget in root.winfo_children():
        widget.destroy()

    global g_pic, g_blanks, g_letters_guessed_dict, g_letters_guessed_display, g_current_board, g_blanks_indices, g_phrase_dict, g_letter_count

    g_letters_guessed_dict[letter] = 1 #add to dict

    if (g_letter_count == 4):
        g_letters_guessed_display = g_letters_guessed_display + ("\n" + letter + " ")
        g_letter_count = 0
    else:
        g_letters_guessed_display = g_letters_guessed_display + (letter + " ")
        g_letter_count += 1

    if letter in g_phrase_dict: #update g_blanks to have the correct guess shown
        temp = list(g_current_board) #temp is g_blanks
        for x in range(len(g_blanks_indices[letter])):
           temp[g_blanks_indices[letter][x]] = letter
        g_current_board = ''.join(temp)
    else:
        g_pic += 1

    current_board = ctk.CTkLabel(root, text=g_current_board, bg_color='lightblue', font=heading_font, text_color='black')
    current_board.place(relx=0.5, rely = 0.15, anchor='center')

    letters_used_frame = ctk.CTkFrame(root, height=400, width=260, bg_color='lightgreen', fg_color='lightgreen', border_color='black', border_width=8, corner_radius=0)
    letters_used_frame.place(relx=0.175, rely=.55, anchor='center')
    
    root.update_idletasks()

    letters_used_label = ctk.CTkLabel(letters_used_frame, text="Letters Used\n-------------------", font=button_font, text_color='black', bg_color='lightgreen')
    letters_used_label.place(relx=.5, rely=.15, anchor='center')

    letters_used_text = ctk.CTkLabel(letters_used_frame, text=g_letters_guessed_display, font=letters_font, text_color='black', bg_color='lightgreen')
    letters_used_text.place(relx=.5, rely=.45, anchor='center')

    show_image(g_pic)

    text_var = tk.StringVar(root)

    def limit_size(*args): #limits to single letter entry and makes letters capital
        value = text_var.get()
        if len(value) > 1 or not value.isalpha():
            text_var.set(value[:1].upper())
            return
        if value in g_letters_guessed_dict: #prevents them from guessing letters already guessed
            text_var.set("")
            return
        text_var.set(value.upper())

    letter_entry = ctk.CTkEntry(root, height = 75, width=80, bg_color='lightblue', fg_color='white', text_color='black', font=heading_font, textvariable=text_var)
    letter_entry.place(relx=.5, rely=.45, anchor='center')

    text_var.trace_add('write', limit_size)

    guess_button = ctk.CTkButton(root, text="Guess", bg_color='lightblue', command=lambda: update_board(letter_entry.get()), corner_radius=16, font=button_font, text_color='black', width=200, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    guess_button.place(relx=.5, rely=.65, anchor='center')

    game_over_checker()


def show_image(integer):
    file = file_path + str(integer) + png
    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo, background='lightblue')
    image_label.image = photo
    image_label.place(relx=.8, rely=.55, anchor='center')

def press_instr():
    for widget in root.winfo_children():
        widget.destroy()

    title_label = ctk.CTkLabel(root, text="Instructions", bg_color='lightblue', font=heading_font, text_color='black')
    title_label.place(relx=.5, rely=.15, anchor='center')

    instr_text = ctk.CTkLabel(root, text = """2 Players Needed
            \nPlayer 1 will enter a custom phrase for the other player to guess.
            \nPlayer 2 will then enter letters to guess the phrase.
            \nCorrect letters will show up in the blanks while incorrect letters will cause the hangman to show up limb by limb.
            \nIf the hangman is fully shown (5 incorrect guesses), Player 2 has lost.
            \nIf Player 2 figures out the phrase before the hangman shows up, Player 1 has lost.
            """, bg_color='lightblue', font=text_font, text_color='black')
    
    instr_text.place(relx=.5, rely=.45, anchor='center')

    main_menu_button = ctk.CTkButton(root, text="Main Menu", bg_color='lightblue', command=show_main_menu, corner_radius=16, font=button_font, text_color='black', width=240, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    main_menu_button.place(relx=.5, rely=.75, anchor='center')

def press_quit():
    root.destroy()

def show_main_menu():
    for widget in root.winfo_children():
        widget.destroy()
    
    title_label = ctk.CTkLabel(root, text="Hangman", bg_color='lightblue', font=title_font, text_color = 'black')
    title_label.place(relx=.5, rely=.2, anchor ='center')
    
    play_button = ctk.CTkButton(root, text="Play", bg_color='lightblue', command=press_play, corner_radius=16, font=button_font, text_color='black', width=240,border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    play_button.place(relx=.5, rely=.45, anchor='center')  

    instr_button = ctk.CTkButton(root, text="Instructions", bg_color='lightblue', command=press_instr, corner_radius=16, font=button_font, text_color='black', width=240, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    instr_button.place(relx=.5, rely=.6, anchor='center') 

    quit_button = ctk.CTkButton(root, text="Quit", bg_color='lightblue', command=press_quit, corner_radius=16, font=button_font, text_color='black', width=240, border_color='black', border_width=4, fg_color='lightgreen', hover_color='green')
    quit_button.place(relx=.5, rely=.75, anchor='center')


root = ctk.CTk()
root.title("Hangman")
root.resizable(True, True)
root.geometry("1280x720")
root.config(background='lightblue')


show_main_menu()


root.mainloop()