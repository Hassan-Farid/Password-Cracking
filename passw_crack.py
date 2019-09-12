import tkinter as tk
from itertools import product
import string
import time
import Message as msg

class mainWin():

    def reset_passw(self):
        self.passwordEntry.delete(0, 'end')
        self.crackLabel.config(text = '')
        self.timeLabel.config(text = '')
        self.combinationLabel.config(text = '')
    
    def check_guess(self, passWord, guessWord):
        if guessWord == passWord:
            return True
        return False
    
    def crack_passw(self, passw):
        self.passw = str(passw)

        if len(self.passw) >= 1 and len(self.passw) < 5:
            start_time = time.time()
            for i in range(1, 5):
                for guess in product(string.printable, repeat = i):
                    self.count += 1
                    if self.check_guess(self.passw, ''.join(guess)):
                        elapsed_time = time.time() - start_time
                        minute_time = elapsed_time // 60
                        second_time = elapsed_time % 60
                        self.crackLabel.config(text = ''.join(guess))
                        self.timeLabel.config(text = "{}m {}s".format(minute_time, round(second_time, 3)))
                        self.combinationLabel.config(text = "{} combinations".format(self.count))
                        break
                if self.check_guess(self.passw, ''.join(guess)):
                    break
        else:
            mes = msg.Message(self.master, "Password not eligible")
        

    def __init__(self, master):
        self.master = master
        self.password = tk.StringVar()
        self.count = 0

        self.titleLabel = tk.Label(self.master, text = "PASSWORD CRACKER", fg = "green", bg = "black", font = "Times 32 bold italic", relief = tk.RAISED)
        self.titleLabel.place(x = 400, y = 10, width = 500)

        self.instructLabel = tk.Label(self.master, text = "Instructions: Enter any password in the range of 4 digits and this application will crack it for you\nAlthough it might take a few minutes...",
                                         fg = "green", bg = "black", bd = 10, font = "Times 18 bold", relief = tk.RAISED)
        self.instructLabel.place(x = 75, y = 110, width = 1175)

        self.passwordEntryLabel = tk.Label(self.master, text = "Enter a password (4 digits or less): ", fg = "green", bg = "black", font = "Times 24 italic", relief = tk.RAISED)
        self.passwordEntryLabel.place(x = 100, y = 210, width = 500)

        self.passwordEntry = tk.Entry(self.master, textvariable = self.password, fg = "green", bg = "black", show = "*", font = "Times 24 italic")
        self.passwordEntry.place(x = 700, y = 210, width = 250)

        self.breakPassBtn = tk.Button(self.master, text = "Crack Password", fg = "green", bg = "black", font = "Times 20 italic", relief = tk.RAISED, command = lambda: self.crack_passw(self.passwordEntry.get()))
        self.breakPassBtn.place(x = 350, y = 310, width = 250)

        self.resetPassBtn = tk.Button(self.master, text = "Reset Password", fg = "green", bg = "black", font = "Times 20 italic", relief = tk.RAISED, command = self.reset_passw)
        self.resetPassBtn.place(x = 700, y = 310, width = 250)

        self.cracktextLabel = tk.Label(self.master, text = "Your Password:" , fg = "green", bg = "black", font = "Times 24 italic", relief = tk.RAISED)
        self.cracktextLabel.place(x = 300, y = 410, width = 300)
        
        self.crackLabel = tk.Label(self.master, text = "" , fg = "green", bg = "black", font = "Times 24 italic", relief = tk.RAISED)
        self.crackLabel.place(x = 700, y = 410, width = 200)

        self.combinationtextLabel = tk.Label(self.master, text = "Combinations Taken to Crack:", fg = "green", bg = "black", font = "Times 24 italic", relief = tk.RAISED)
        self.combinationtextLabel.place(x = 150, y = 510, width = 450)
        
        self.combinationLabel = tk.Label(self.master, text = "", fg = "green", bg = "black", font = "Times 24 italic", relief = tk.RAISED)
        self.combinationLabel.place(x = 700, y = 510, width = 400)

        self.timetextLabel = tk.Label(self.master, text = "Time Taken to Crack:", fg = "green", bg = "black", font = "Times 24 italic", relief = tk.RAISED)
        self.timetextLabel.place(x = 300, y = 610, width = 300)
        
        self.timeLabel = tk.Label(self.master, text = "", fg = "green", bg = "black", font = "Times 24 italic", relief = tk.RAISED)
        self.timeLabel.place(x = 700, y = 610, width = 400)

