import tkinter as tk
from tkinter import messagebox
import random
import string
class Window:

    def __init__(self):
        
        self.window = tk.Tk()

        self.window.geometry("800x600")
       
        self.window.title("PasswordGenerator")
        
        self.window.attributes('-topmost', True)
        self.window.after(100, lambda: self.window.attributes('-topmost', False))

        self.label = tk.Label(self.window,text="This is a Password Generator", font=('Helvetica', 18))
        self.label.pack(padx=20,pady=20)

        self.check_state_1 = tk.IntVar()
        self.check_state_2 = tk.IntVar()
        self.check_state_3 = tk.IntVar()

        self.button = tk.Checkbutton(self.window, text='Include symbols', font=('Arial', 16), variable=self.check_state_1)
        self.button.pack(pady=5)

        self.button2 = tk.Checkbutton(self.window, text='Include numbers', font=('Arial', 16), variable=self.check_state_2)
        self.button2.pack(pady=5)

        self.button3 = tk.Checkbutton(self.window, text='Include capital letters', font=('Arial', 16), variable=self.check_state_3)
        self.button3.pack(pady=5)

        self.label2 = tk.Label(self.window,text="Enter length", font=('Helvetica', 18))
        self.label2.pack(padx=20,pady=20)

        self.input = tk.Entry(self.window,font=('Arial', 16))
        self.input.pack()

        self.button = tk.Button(self.window,text="Generate password",font=('Arial', 16), command=self.generate_password)
        self.button.pack(padx=20,pady=20)

        self.window.mainloop()
    
    def generate_password(self):
        if self.input.get().isdigit():
            length = int(self.input.get()) 
            password = ""
            character_pool = string.ascii_lowercase

            if self.check_state_1.get() == 1:
                character_pool += string.punctuation
            if self.check_state_2.get() == 1:
                character_pool += string.digits
            if self.check_state_3.get() == 1:
                character_pool += string.ascii_uppercase
            
            while len(password) != length:
                password += random.choice(character_pool)

            self.window.clipboard_clear()
            self.window.clipboard_append(password)
            self.window.update() 
            messagebox.showinfo(title="Success!", message="Password was sent to clipboard: " + password)
        else:
            messagebox.showerror(title="Error", message="Your password could not be generated. 😭")
            


Window()