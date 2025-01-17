#Import Libaries
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import random
from threading import Timer
import sys

# Retrieve operation from command-line arguments
if len(sys.argv) > 1:
    clicked_Button_Text = sys.argv[1]
else:
    clicked_Button_Text = "+"  # Default fallbackWW


#Window GUI
window = tb.Window(themename='superhero')
window.geometry("800x800")
window.title("Plus Screen")

#Window Addons
howToLabel = tb.Label(window, text="Questions will be random from 1 to 10!", font=('Luckiest Guy', 20))
haveFunLabel = tb.Label(window, text="Have Fun and PRACTICE!", font=('Luckiest Guy', 20))

howToLabel.place(relx=0.5, rely=0.2, anchor='center')   #Place Labels
haveFunLabel.place(relx=0.5, rely=0.25, anchor='center') #Place Labels

#Styles for button
style = tb.Style()
style.configure("SuccessButton.TButton", font=('Luckiest Guy', 25), background='#5cb85c', foreground='white')
style.configure("Highlight.TButton", font=('Luckiest Guy', 25), background='white', foreground='grey')

#Return to Main Screen
returnLabel = tb.Button(window, text='Return', style='SuccessButton.TButton', padding=10, command=window.destroy)
returnLabel.place(relx=0.1, rely=0.05, anchor='center')
#       Items above here are at the top of the screen.      #


# Event handler for button clicks
def highlight_button(button):
    # Change the button style temporarily
    button.configure(style="Highlight.TButton")
    # Reset the style back to the original after 0.2 seconds
    Timer(0.2, lambda: button.configure(style="SuccessButton.TButton")).start()


# Globals to store the clicked number and the correct answer
clicked_text = None
correct_answer = None

# Function to ask a math question
def ask_question():
    global correct_answer, clicked_text, operation_symbol

    # Ensure clicked_text has a valid value
    if clicked_text is None:
        clicked_text = 0

    # Generate a random number
    random_number = random.randint(1, 10)

    # Handle operations dynamically based on clicked_Button_Text
    if clicked_Button_Text == "+":
        correct_answer = clicked_text + random_number
        operation_symbol = "+"
    elif clicked_Button_Text == "-":
        correct_answer = clicked_text - random_number
        operation_symbol = "-"
    elif clicked_Button_Text == "x":
        correct_answer = clicked_text * random_number
        operation_symbol = "x"
    elif clicked_Button_Text == "/":
        # Avoid division by zero
        if random_number != 0:
            correct_answer = clicked_text // random_number  # Integer division
        else:
            correct_answer = clicked_text  # Default fallback
        operation_symbol = "/"
    else:
        # Default case if no valid operation
        correct_answer = clicked_text
        operation_symbol = "?"

    # Update the question label
    questionLabel.configure(text=f"What is {clicked_text} {operation_symbol} {random_number}?")

# Create a feedback label for the correct answer
feedbackLabel = tb.Label(window, text="", font=('Luckiest Guy', 20), foreground="blue")
feedbackLabel.place(relx=0.5, rely=0.35, anchor='center')  # Place it above the question

# Function to clear the feedback label
def clear_feedback():
    feedbackLabel.configure(text="")  # Clear the feedback text

# Function to check the user's answer
def check_answer():
    highlight_button(submitButton)
    user_input = answerEntry.get()  # Get the user's input
    try:
        user_answer = int(user_input)  # Convert to integer
        if user_answer == correct_answer:
            # Correct answer: highlight green and display feedback
            answerEntry.configure(bootstyle="success")
            feedbackLabel.configure(text=f"Correct! The answer is {correct_answer}", foreground="green")
        else:
            # Incorrect answer: highlight red and display feedback
            answerEntry.configure(bootstyle="danger")
            feedbackLabel.configure(text=f"Incorrect! The correct answer is {correct_answer}", foreground="red")
    except ValueError:
        # Invalid input: highlight red and display feedback
        answerEntry.configure(bootstyle="danger")
        feedbackLabel.configure(text="Invalid input! Please enter a number.", foreground="red")

    # Schedule clearing of the feedback label after 2 seconds
    window.after(2000, clear_feedback)

    # Clear the entry box and ask the next question after a short delay
    window.after(1000, next_question)

# Function to proceed to the next question
def next_question():
    answerEntry.delete(0, 'end')  # Clear the entry box
    answerEntry.configure(bootstyle="")  # Reset entry style
    ask_question()

# Function to show the math question screen
def show_entry_and_label(button):
    global clicked_text

    # Get the button's text
    clicked_text = int(button.cget("text"))  # Convert text to integer
    
    # Hide all buttons in the frame except the clicked one
    for child in number_frame.winfo_children():
        if child != button:
            child.grid_remove()

    # Remove the clicked button
    button.destroy()
    
    # Create and place the label displaying the selected button
    clickedLabel = tb.Label(window, text=f"{clicked_text}'s Selected!", font=('Luckiest Guy', 20), foreground='red')
    clickedLabel.place(relx=0.5, rely=0.3, anchor='center')
    
    # Create and place the question label
    global questionLabel
    questionLabel = tb.Label(window, text="", font=('Luckiest Guy', 20))
    questionLabel.place(relx=0.5, rely=0.4, anchor='center')
    
    # Create and place the entry box
    global answerEntry
    answerEntry = tb.Entry(window, font=('Luckiest Guy', 18))
    answerEntry.place(relx=0.5, rely=0.45, anchor='center')
    
    # Button to submit the answer
    global submitButton
    submitButton = tb.Button(window, text="Submit", style="SuccessButton.TButton", command=check_answer)
    submitButton.place(relx=0.5, rely=0.55, anchor='center')

    # Start asking the first question
    ask_question()

# Window Main Algorithm
number_frame = tb.Frame(window)
number_frame.place(relx=0.5, rely=0.5, anchor='center')

# Create Buttons (Created Individually for ease, I know I couldve done a for loop and maybe just stored them somewhere, but this makes it easier.)
startButton0 = tb.Button(number_frame, text='0', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton0))
startButton0.grid(row=0, column=0, padx=10, pady=10)

startButton1 = tb.Button(number_frame, text='1', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton1))
startButton1.grid(row=0, column=1, padx=10, pady=10)

startButton2 = tb.Button(number_frame, text='2', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton2))
startButton2.grid(row=0, column=2, padx=10, pady=10)

startButton3 = tb.Button(number_frame, text='3', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton3))
startButton3.grid(row=0, column=3, padx=10, pady=10)

startButton4 = tb.Button(number_frame, text='4', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton4))
startButton4.grid(row=0, column=4, padx=10, pady=10)

startButton5 = tb.Button(number_frame, text='5', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton5))
startButton5.grid(row=0, column=5, padx=10, pady=10)

startButton6 = tb.Button(number_frame, text='6', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton6))
startButton6.grid(row=1, column=0, padx=10, pady=10)

startButton7 = tb.Button(number_frame, text='7', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton7))
startButton7.grid(row=1, column=1, padx=10, pady=10)

startButton8 = tb.Button(number_frame, text='8', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton8))
startButton8.grid(row=1, column=2, padx=10, pady=10)

startButton9 = tb.Button(number_frame, text='9', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton9))
startButton9.grid(row=1, column=3, padx=10, pady=10)

startButton10 = tb.Button(number_frame, text='10', style='SuccessButton.TButton', padding=5, command=lambda: show_entry_and_label(startButton10))
startButton10.grid(row=1, column=4, padx=10, pady=10)

# Window Running Loop
window.mainloop()
