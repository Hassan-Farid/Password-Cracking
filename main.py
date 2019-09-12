import tkinter as tk
import passw_crack as pc

def main():
    myApp = tk.Tk()
    myApp.title("Password Cracker")
    myApp.configure(bg = "black")
    myApp.wm_state("zoomed")
    appWin = pc.mainWin(myApp)
    myApp.mainloop()


if __name__ == "__main__":
    main()
