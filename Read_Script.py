import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.ttk as ttk
import time

class Script_GUI(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid()

        # Getting the script to read
        self.script = tk.StringVar()
        self.script.set("")

        #Setting the play speed 
        self.speed = tk.IntVar()
        self.speed.set(1)

        self.make_widgets()
    
    def make_widgets(self):
        # Creating the widgets

        #Display the script to read
        self.script_display = tk.Text(self, width=50, height=1)
        self.script_display.grid(row=0, column=0)

        #Taking in the speed
        ttk.Label(self, text='Speed:').grid(row=1, column=0)
        self.play_speed = ttk.Entry(self, textvariable=self.speed)
        self.play_speed.grid(row=1, column=1)

        ttk.Button(self, text= 'Play', command=self.play_script).grid(row=0, column=1)

    def play_script(self):
        # Get the script file path
        script_path = 'script.txt'

        # Get the play speed
        speed = self.speed.get()

        # Read the script file
        with open(script_path, 'r') as file:
            script = file.read()

        # Split the script into individual words
        words = script.split()

        # Initialize the word index and the displayed text
        word_index = 0
        displayed_text = ""

        # Loop through each word in the script
        for word in words:
            # Replace newlines with tabs
            if word == "\n":
                word = "__________"

            # Add the word to the displayed text
            displayed_text += word + " "
            
            # Remove the first word from the displayed text if the displayed text is too long
            if len(displayed_text) > 50:
                displayed_text = displayed_text.split(" ", 1)[1]
            # Update the text box
            self.script_display.delete("1.0", tk.END)
            self.script_display.insert(tk.END, displayed_text)
            self.script_display.see(tk.END)
            self.script_display.update()

            # Delay the next word based on the play speed
            time.sleep(1 / speed)

            # Increment the word index
            word_index += 1


root = tk.Tk()
Script_GUI(parent=root)
root.mainloop()