import tkinter
import random

root = tkinter.Tk()
root.title("Welcome to Rock, Paper, Scissors,Lizard,Spock")
root.geometry("600x700")

random_number = random.randint(1, 5)
if random_number == 1:
    computer_choice = "R"
elif random_number == 2:
    computer_choice = "P"
elif random_number == 3:
    computer_choice = "S"
elif random_number == 4:
    computer_choice = "L"
elif random_number == 5:
    computer_choice = "SP"

rock_image = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper_image = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)"""

scissors_image = """
    _______
---'   ____)____
          ______)   
       __________)   
      (____)
---.__(___)"""

lizard_image = """/_
             _.--..---"-,--c_
        \L..'           ._O__)_
,-.     _.+  _  \..--( /           
  `\.-''__.-' \ (     \_      
    `'''       `\__   /
                """

spock_image = "🖖"


# Create functions
def rock():
    label_user_choice['text'] = rock_image
    
    if computer_choice == "R":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "S":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = scissors_image
    
def paper():
    label_user_choice['text'] = paper_image
    
    if computer_choice == "P":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "S":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = scissors_image
    elif computer_choice == "R":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = rock_image
    
def scissors():
    label_user_choice['text'] = scissors_image
    
    if computer_choice == "S":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = scissors_image
    elif computer_choice == "R":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = paper_image
def lizard():
    label_user_choice['text'] = lizard_image

    if computer_choice == "L":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = lizard_image
    elif computer_choice == "R":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "SP":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = spock_image
def spock():
    label_user_choice['text'] = spock_image
    
    if computer_choice == "SP":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = spock_image
    elif computer_choice == "R":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "L":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = lizard_image
    
def reset():
    global computer_choice
    random_number = random.randint(1, 5)
    if random_number == 1:
        computer_choice = "R"
    elif random_number == 2:
        computer_choice = "P"
    elif random_number == 3:
        computer_choice = "S"
    elif random_number == 4:
        computer_choice = "L"
    elif random_number == 5:
        computer_choice = "SP"
        
    label_computer_choice['text'] = ""
    label_user_choice['text'] = ""
    label_result['text'] = "Choose..."


# Create widgets
button_rock = tkinter.Button(root, text="Rock", command = rock)
button_rock.pack()

button_paper = tkinter.Button(root, text="Paper", command = paper)
button_paper.pack()

button_scissors = tkinter.Button(root, text="Scissors", command = scissors)
button_scissors.pack()

button_lizard = tkinter.Button(root, text="Lizard", command = lizard)
button_lizard.pack()

button_spock = tkinter.Button(root, text="Spock", command = spock)
button_spock.pack()

label_computer_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
label_computer_choice.pack()

label_user_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
label_user_choice.pack()

label_result = tkinter.Label(root, text="Choose...")
label_result.pack()

button_reset = tkinter.Button(root, text="Reset", command = reset)
button_reset.pack()

root.mainloop()
