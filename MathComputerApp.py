# Import Libraries
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from threading import Timer
import subprocess

# Define GUI window
math_App = tb.Window(themename='superhero')

# Define GUI window properties
math_App.geometry("800x800")
math_App.title("MathApp")

# Add a label
WelcomeUserLabel = tb.Label(math_App, text='MATH TIME', font=('Luckiest Guy', 40))
WelcomeUserLabel.place(relx=0.5, rely=0.05, anchor='center')

WelcomeUserLabel2 = tb.Label(math_App, text='MATH TIME', font=('Luckiest Guy', 40))
WelcomeUserLabel2.place(relx=0.5, rely=0.75, anchor='center')

Theodore = tb.Label(math_App, text='for Theo', font=('Luckiest Guy', 40))
Theodore.place(relx=0.5, rely=0.9, anchor='center')

# Define custom styles with larger font
style = tb.Style()
style.configure("InfoButton.TButton", font=('Helvetica', 60), background='#5bc0de', foreground='white')
style.configure("SuccessButton.TButton", font=('Helvetica', 60), background='#5cb85c', foreground='white')
style.configure("WarningButton.TButton", font=('Helvetica', 60), background='#f0ad4e', foreground='white')
style.configure("DangerButton.TButton", font=('Helvetica', 60), background='#d9534f', foreground='white')
style.configure("Highlight.TButton", font=('Helvetica', 60), background='#007bff', foreground='white')

# Create a frame for grouping buttons
button_frame = tb.Frame(math_App)
button_frame.place(relx=0.5, rely=0.4, anchor='center')  # Center the frame on the window

#Get Button for Operation
clicked_Button_Text = ''

# Event handler for button clicks
def highlight_button(button):
    global clicked_Button_Text
    clicked_Button_Text = button.cget("text")
    # Change the button style temporarily
    button.configure(style="Highlight.TButton")
    # Reset the style back to the original after 0.2 seconds
    Timer(0.2, lambda: button.configure(style=button.default_style)).start()

# Function to open the other script
def open_other_script():
    math_App.withdraw()  # Hide the main window
    process = subprocess.Popen(["python", "PlusMinusTimesDivide.py", clicked_Button_Text])
    process.wait()  # Wait for the secondary script to finish
    math_App.deiconify()  # Show the main window again

# Define Math Buttons using styles and grid layout
Plus_Button = tb.Button(button_frame, text="+", style="InfoButton.TButton", padding=50)
Plus_Button.grid(row=0, column=0, padx=20, pady=20)
Plus_Button.default_style = "InfoButton.TButton"
Plus_Button.configure(command=lambda: [highlight_button(Plus_Button), open_other_script()])

Minus_Button = tb.Button(button_frame, text="-", style="SuccessButton.TButton", padding=50)
Minus_Button.grid(row=0, column=1, padx=20, pady=20)
Minus_Button.default_style = "SuccessButton.TButton"
Minus_Button.configure(command=lambda:[highlight_button(Minus_Button), open_other_script()])

Times_Button = tb.Button(button_frame, text="x", style="WarningButton.TButton", padding=50)
Times_Button.grid(row=1, column=0, padx=20, pady=20)
Times_Button.default_style = "WarningButton.TButton"
Times_Button.configure(command=lambda: [highlight_button(Times_Button), open_other_script()])

Divide_Button = tb.Button(button_frame, text="/", style="DangerButton.TButton", padding=50)
Divide_Button.grid(row=1, column=1, padx=20, pady=20)
Divide_Button.default_style = "DangerButton.TButton"
Divide_Button.configure(command=lambda: [highlight_button(Divide_Button), open_other_script()])

# Keep GUI window Running
math_App.mainloop()

