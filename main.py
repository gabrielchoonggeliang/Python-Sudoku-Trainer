from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import sudoku


class Sudoku:
    def __init__(self):
        self.main_window()

    # First Page of Sudoku Solver
    # Prompt user to input their names
    def main_window(self):
        self.main = Tk()
        self.f1 = tk.Frame(self.main, bg="#60795C")
        self.l1 = tk.Label(self.f1, text="Please enter your name:", bg="#60795C", fg="#E9EBD9", font="Broadway 15")
        self.l2 = tk.Entry(self.f1)
        self.b1 = tk.Button(self.f1, font="Broadway 10", fg="#60795C", bg="#E9EBD9", text='OK',
                            command=self.window1)
        self.f1.pack()
        self.l1.pack()
        self.l2.pack()
        self.b1.pack(pady=5)
        self.main.mainloop()

    # Second Page of Sudoku Solver
    def window1(self):
        self.window = Toplevel(self.main)
        self.window.title("Sudoku")
        self.window.geometry("1000x550")
        self.name = f'Hi, {self.l2.get()}!\nWelcome to Sudoku Solver!'  # show user's name
        self.f1 = tk.Frame(self.window, bg="#60795C")
        self.l1 = tk.Label(self.f1, text=self.name, bg="#60795C", fg="#E9EBD9", font="Broadway 40")
        self.Progress_Bar = Progressbar(self.f1, orient=HORIZONTAL, length=550, mode='determinate')  # loading bar
        self.b1 = tk.Button(self.f1, font="Broadway 15", fg="#60795C", bg="#E9EBD9", text='Start',
                            command=lambda: [self.Slide(), self.NewWindow()])

        self.f1.pack(fill=BOTH, expand=1)
        self.l1.pack(ipady=150)
        self.Progress_Bar.pack(pady=15)
        self.b1.pack(ipadx=20)

        self.window.mainloop()

    # Animation of the loading bar
    # https://pythonguides.com/python-tkinter-animation/
    def Slide(self):
        import time
        self.Progress_Bar['value'] = 20
        self.window.update_idletasks()
        time.sleep(1)
        self.Progress_Bar['value'] = 50
        self.window.update_idletasks()
        time.sleep(1)
        self.Progress_Bar['value'] = 80
        self.window.update_idletasks()
        time.sleep(1)
        self.Progress_Bar['value'] = 100

    # Third Page of Sudoku Solver
    # User can choose which option to continue (Easy, Medium, Hard, Exit)
    def NewWindow(self):
        self.win = Toplevel(self.window)
        self.win.geometry("1000x550")
        self.f2 = tk.Frame(self.win, bg="#60795C")
        self.f3 = tk.Frame(self.win, bg="#60795C")
        self.b2 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit', command=self.close)
        self.b3 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy', command=self.easy)
        self.b4 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Medium', command=self.medium)
        self.b5 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Hard', command=self.hard)

        self.f2.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')
        self.f3.pack(ipadx=10, ipady=10, expand=True, fill='both', side='right')
        self.b3.pack(pady=150, ipady=5, ipadx=25)
        self.b4.pack(pady=150, ipady=5, ipadx=25)
        self.b2.pack(ipady=5, ipadx=25)
        self.b5.pack(ipady=5, ipadx=25)
        self.win.mainloop()

    # Back to page two
    def close(self):
        self.win.destroy()

    # Forth Page of Sudoku Solver
    # User can choose which game to play first
    def easy(self):
        self.eas = Toplevel(self.win)
        self.eas.geometry("1000x550")
        self.f2 = tk.Frame(self.eas, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 1', command=self.easy1)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 2', command=self.easy2)
        self.b3 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 3', command=self.easy3)
        self.b4 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 4', command=self.easy4)
        self.b5 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 5', command=self.easy5)
        self.f3 = tk.Frame(self.eas, bg="#60795C")
        self.b6 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 6', command=self.easy6)
        self.b7 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 7', command=self.easy7)
        self.b8 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 8', command=self.easy8)
        self.b9 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 9', command=self.easy9)
        self.b10 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Easy 10',
                             command=self.easy10)
        self.b11 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                             command=lambda: [self.eas.destroy(), self.win.deiconify])
        self.b12 = tk.Button(self.f3, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                             command=self.close)

        self.f2.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')
        self.f3.pack(ipadx=10, ipady=10, expand=True, fill='both', side='right')
        self.b1.pack(pady=20, ipady=5, ipadx=25)
        self.b2.pack(pady=20, ipady=5, ipadx=25)
        self.b3.pack(pady=20, ipady=5, ipadx=25)
        self.b4.pack(pady=20, ipady=5, ipadx=25)
        self.b5.pack(pady=20, ipady=5, ipadx=25)
        self.b6.pack(pady=20, ipady=5, ipadx=25)
        self.b7.pack(pady=20, ipady=5, ipadx=25)
        self.b8.pack(pady=20, ipady=5, ipadx=25)
        self.b9.pack(pady=20, ipady=5, ipadx=25)
        self.b10.pack(pady=20, ipady=5, ipadx=25)
        self.b11.pack(ipady=5, ipadx=25, side="left")
        self.b12.pack(ipady=5, ipadx=25, side="right")

    # Forth Page of Sudoku Solver
    # User can choose which game to play first
    def medium(self):
        self.med = Toplevel(self.win, bg="#60795C")
        self.med.geometry("1000x550")

        self.b1 = tk.Button(self.med, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Medium 1',
                            command=self.med1)
        self.b2 = tk.Button(self.med, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Medium 2',
                            command=self.med2)
        self.b3 = tk.Button(self.med, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Medium 3',
                            command=self.med3)
        self.b4 = tk.Button(self.med, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Medium 4',
                            command=self.med4)
        self.b5 = tk.Button(self.med, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Medium 5',
                            command=self.med5)
        self.b6 = tk.Button(self.med, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.med.destroy(), self.win.deiconify])
        self.b7 = tk.Button(self.med, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)

        self.b1.pack(pady=20, ipady=5, ipadx=25)
        self.b2.pack(pady=20, ipady=5, ipadx=25)
        self.b3.pack(pady=20, ipady=5, ipadx=25)
        self.b4.pack(pady=20, ipady=5, ipadx=25)
        self.b5.pack(pady=20, ipady=5, ipadx=25)
        self.b6.pack(ipady=5, ipadx=25, side="left")
        self.b7.pack(ipady=5, ipadx=25, side="right")

    # Forth Page of Sudoku Solver
    # User can choose which game to play first
    def hard(self):
        self.har = Toplevel(self.win, bg="#60795C")
        self.har.geometry("1000x550")

        self.b1 = tk.Button(self.har, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Hard 1', command=self.hard1)
        self.b2 = tk.Button(self.har, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Hard 2', command=self.hard2)
        self.b3 = tk.Button(self.har, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Hard 3', command=self.hard3)
        self.b4 = tk.Button(self.har, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Hard 4', command=self.hard4)
        self.b5 = tk.Button(self.har, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Hard 5', command=self.hard5)
        self.b6 = tk.Button(self.har, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.har.destroy(), self.win.deiconify])
        self.b7 = tk.Button(self.har, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)

        self.b1.pack(pady=20, ipady=5, ipadx=25)
        self.b2.pack(pady=20, ipady=5, ipadx=25)
        self.b3.pack(pady=20, ipady=5, ipadx=25)
        self.b4.pack(pady=20, ipady=5, ipadx=25)
        self.b5.pack(pady=20, ipady=5, ipadx=25)
        self.b6.pack(ipady=5, ipadx=25, side="left")
        self.b7.pack(ipady=5, ipadx=25, side="right")

    # Fifth Page of Sudoku Solver
    # User can start to play the game by entering the numbers
    def easy1(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e1)  # User can check their answers after the game
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e1[i][j]))
                if e1[i][j] != 0:
                    self.table.config(state="disabled")

    def easy2(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e2)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e2[i][j]))
                if e2[i][j] != 0:
                    self.table.config(state="disabled")

    def easy3(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e3)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e3[i][j]))
                if e3[i][j] != 0:
                    self.table.config(state="disabled")

    def easy4(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e4)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e4[i][j]))
                if e4[i][j] != 0:
                    self.table.config(state="disabled")

    def easy5(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e5)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e5[i][j]))
                if e5[i][j] != 0:
                    self.table.config(state="disabled")

    def easy6(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e6)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e6[i][j]))
                if e6[i][j] != 0:
                    self.table.config(state="disabled")

    def easy7(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e7)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e7[i][j]))
                if e7[i][j] != 0:
                    self.table.config(state="disabled")

    def easy8(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e8)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e8[i][j]))
                if e8[i][j] != 0:
                    self.table.config(state="disabled")

    def easy9(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e9)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e9[i][j]))
                if e9[i][j] != 0:
                    self.table.config(state="disabled")

    def easy10(self):
        self.ea = Toplevel(self.eas, bg="#60795C")
        self.ea.geometry("1000x550")
        self.f1 = tk.Frame(self.ea, bg="#60795C")
        self.f2 = tk.Frame(self.ea, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_e10)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ea.destroy(), self.eas.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(e10[i][j]))
                if e10[i][j] != 0:
                    self.table.config(state="disabled")

    def med1(self):
        self.me = Toplevel(self.med, bg="#60795C")
        self.me.geometry("1000x550")
        self.f1 = tk.Frame(self.me, bg="#60795C")
        self.f2 = tk.Frame(self.me, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_m1)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.me.destroy(), self.med.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(m1[i][j]))
                if m1[i][j] != 0:
                    self.table.config(state="disabled")

    def med2(self):
        self.me = Toplevel(self.med, bg="#60795C")
        self.me.geometry("1000x550")
        self.f1 = tk.Frame(self.me, bg="#60795C")
        self.f2 = tk.Frame(self.me, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_m2)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.me.destroy(), self.med.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(m2[i][j]))
                if m2[i][j] != 0:
                    self.table.config(state="disabled")

    def med3(self):
        self.me = Toplevel(self.med, bg="#60795C")
        self.me.geometry("1000x550")
        self.f1 = tk.Frame(self.me, bg="#60795C")
        self.f2 = tk.Frame(self.me, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_m3)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.me.destroy(), self.med.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(m3[i][j]))
                if m3[i][j] != 0:
                    self.table.config(state="disabled")

    def med4(self):
        self.me = Toplevel(self.med, bg="#60795C")
        self.me.geometry("1000x550")
        self.f1 = tk.Frame(self.me, bg="#60795C")
        self.f2 = tk.Frame(self.me, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_m4)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.me.destroy(), self.med.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(m4[i][j]))
                if m4[i][j] != 0:
                    self.table.config(state="disabled")

    def med5(self):
        self.me = Toplevel(self.med, bg="#60795C")
        self.me.geometry("1000x550")
        self.f1 = tk.Frame(self.me, bg="#60795C")
        self.f2 = tk.Frame(self.me, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_m5)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.me.destroy(), self.med.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(m5[i][j]))
                if m5[i][j] != 0:
                    self.table.config(state="disabled")

    def hard1(self):
        self.ha = Toplevel(self.har, bg="#60795C")
        self.ha.geometry("1000x550")
        self.f1 = tk.Frame(self.ha, bg="#60795C")
        self.f2 = tk.Frame(self.ha, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_h1)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ha.destroy(), self.har.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(h1[i][j]))
                if h1[i][j] != 0:
                    self.table.config(state="disabled")

    def hard2(self):
        self.ha = Toplevel(self.har, bg="#60795C")
        self.ha.geometry("1000x550")
        self.f1 = tk.Frame(self.ha, bg="#60795C")
        self.f2 = tk.Frame(self.ha, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_h2)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ha.destroy(), self.har.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(h2[i][j]))
                if h2[i][j] != 0:
                    self.table.config(state="disabled")

    def hard3(self):
        self.ha = Toplevel(self.har, bg="#60795C")
        self.ha.geometry("1000x550")
        self.f1 = tk.Frame(self.ha, bg="#60795C")
        self.f2 = tk.Frame(self.ha, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_h3)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ha.destroy(), self.har.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(h3[i][j]))
                if h3[i][j] != 0:
                    self.table.config(state="disabled")

    def hard4(self):
        self.ha = Toplevel(self.har, bg="#60795C")
        self.ha.geometry("1000x550")
        self.f1 = tk.Frame(self.ha, bg="#60795C")
        self.f2 = tk.Frame(self.ha, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_h4)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ha.destroy(), self.har.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(h4[i][j]))
                if h4[i][j] != 0:
                    self.table.config(state="disabled")

    def hard5(self):
        self.ha = Toplevel(self.har, bg="#60795C")
        self.ha.geometry("1000x550")
        self.f1 = tk.Frame(self.ha, bg="#60795C")
        self.f2 = tk.Frame(self.ha, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Show Answer',
                            command=self.show_h5)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.ha.destroy(), self.har.deiconify])
        # https://github.com/Morqos/GUI-Sudoku-Solver/blob/master/SudokuSolver.py
        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=0,
                                      highlightcolor='yellow', highlightthickness=1, highlightbackground='black')
                self.f1.pack(ipadx=10, ipady=10, pady=100, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.table.grid(row=i, column=j)
                self.table.insert(END, str(h5[i][j]))
                if h5[i][j] != 0:
                    self.table.config(state="disabled")

    # show the answers
    def show_e1(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e1, 0, 0):
            sudoku.puzzle(e1)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e1[i][j]))
                self.table.config(state="disabled")

    def show_e2(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e2, 0, 0):
            sudoku.puzzle(e2)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e2[i][j]))
                self.table.config(state="disabled")

    def show_e3(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e3, 0, 0):
            sudoku.puzzle(e3)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e3[i][j]))
                self.table.config(state="disabled")

    def show_e4(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e4, 0, 0):
            sudoku.puzzle(e4)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e4[i][j]))
                self.table.config(state="disabled")

    def show_e5(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e5, 0, 0):
            sudoku.puzzle(e5)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e5[i][j]))
                self.table.config(state="disabled")

    def show_e6(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e6, 0, 0):
            sudoku.puzzle(e6)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e6[i][j]))
                self.table.config(state="disabled")

    def show_e7(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e7, 0, 0):
            sudoku.puzzle(e7)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e7[i][j]))
                self.table.config(state="disabled")

    def show_e8(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e8, 0, 0):
            sudoku.puzzle(e8)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e8[i][j]))
                self.table.config(state="disabled")

    def show_e9(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e9, 0, 0):
            sudoku.puzzle(e9)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e9[i][j]))
                self.table.config(state="disabled")

    def show_e10(self):
        self.sh = Toplevel(self.ea, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ea.deiconify])
        if sudoku.sudoku(e10, 0, 0):
            sudoku.puzzle(e10)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(e10[i][j]))
                self.table.config(state="disabled")

    def show_m1(self):
        self.sh = Toplevel(self.me, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.me.deiconify])
        if sudoku.sudoku(m1, 0, 0):
            sudoku.puzzle(m1)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(m1[i][j]))
                self.table.config(state="disabled")

    def show_m2(self):
        self.sh = Toplevel(self.me, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.me.deiconify])
        if sudoku.sudoku(m2, 0, 0):
            sudoku.puzzle(m2)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(m2[i][j]))
                self.table.config(state="disabled")

    def show_m3(self):
        self.sh = Toplevel(self.me, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.me.deiconify])
        if sudoku.sudoku(m3, 0, 0):
            sudoku.puzzle(m3)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(m3[i][j]))
                self.table.config(state="disabled")

    def show_m4(self):
        self.sh = Toplevel(self.me, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.me.deiconify])
        if sudoku.sudoku(m4, 0, 0):
            sudoku.puzzle(m4)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(m4[i][j]))
                self.table.config(state="disabled")

    def show_m5(self):
        self.sh = Toplevel(self.me, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.me.deiconify])
        if sudoku.sudoku(m5, 0, 0):
            sudoku.puzzle(m5)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(m5[i][j]))
                self.table.config(state="disabled")

    def show_h1(self):
        self.sh = Toplevel(self.ha, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ha.deiconify])
        if sudoku.sudoku(h1, 0, 0):
            sudoku.puzzle(h1)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(h1[i][j]))
                self.table.config(state="disabled")

    def show_h2(self):
        self.sh = Toplevel(self.ha, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ha.deiconify])
        if sudoku.sudoku(h2, 0, 0):
            sudoku.puzzle(h2)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(h2[i][j]))
                self.table.config(state="disabled")

    def show_h3(self):
        self.sh = Toplevel(self.ha, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ha.deiconify])
        if sudoku.sudoku(h3, 0, 0):
            sudoku.puzzle(h3)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(h3[i][j]))
                self.table.config(state="disabled")

    def show_h4(self):
        self.sh = Toplevel(self.ha, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ha.deiconify])
        if sudoku.sudoku(h4, 0, 0):
            sudoku.puzzle(h4)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(h4[i][j]))
                self.table.config(state="disabled")

    def show_h5(self):
        self.sh = Toplevel(self.ha, bg="#60795C")
        self.sh.geometry("1000x550")
        self.f1 = tk.Frame(self.sh, bg="#60795C")
        self.f2 = tk.Frame(self.sh, bg="#60795C")
        self.b1 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Exit',
                            command=self.close)
        self.b2 = tk.Button(self.f2, font="Broadway 20", fg="#60795C", bg="#E9EBD9", text='Back',
                            command=lambda: [self.sh.destroy(), self.ha.deiconify])
        if sudoku.sudoku(h5, 0, 0):
            sudoku.puzzle(h5)

        for i in range(0, 9):
            for j in range(0, 9):
                self.table = tk.Entry(self.f1, width=5, font="Arial 20", bg="#E9EBD9", borderwidth=1)
                self.table.grid(row=i, column=j)
                self.f1.pack(ipadx=10, ipady=10, pady=80, expand=True, fill='both', side='left')
                self.f2.pack(ipadx=10, ipady=8, pady=180, expand=True, fill='both', side='right')
                self.b2.pack(pady=20, ipady=5, ipadx=25)
                self.b1.pack(pady=20, ipady=5, ipadx=25)
                self.table.insert(END, str(h5[i][j]))
                self.table.config(state="disabled")

# sudoku questions
# sudoku questions obtained from: https://www.rd.com/list/printable-sudoku-puzzles/
e1 = [[0, 7, 0, 0, 2, 0, 0, 4, 6],
      [0, 6, 0, 0, 0, 0, 8, 9, 0],
      [2, 0, 0, 8, 0, 0, 7, 1, 5],
      [0, 8, 4, 0, 9, 7, 0, 0, 0],
      [7, 1, 0, 0, 0, 0, 0, 5, 9],
      [0, 0, 0, 1, 3, 0, 4, 8, 0],
      [6, 9, 7, 0, 0, 2, 0, 0, 8],
      [0, 5, 8, 0, 0, 0, 0, 6, 0],
      [4, 3, 0, 0, 8, 0, 0, 7, 0]]
e2 = [[0, 0, 4, 0, 5, 0, 0, 0, 0],
      [9, 0, 0, 7, 3, 4, 6, 0, 0],
      [0, 0, 3, 0, 2, 1, 0, 4, 9],
      [0, 3, 5, 0, 9, 0, 4, 8, 0],
      [0, 9, 0, 0, 0, 0, 0, 3, 0],
      [0, 7, 6, 0, 1, 0, 9, 2, 0],
      [3, 1, 0, 9, 7, 0, 2, 0, 0],
      [0, 0, 9, 1, 8, 2, 0, 0, 3],
      [0, 0, 0, 0, 6, 0, 1, 0, 0]]
e3 = [[8, 0, 6, 0, 1, 0, 0, 0, 0],
      [0, 0, 3, 0, 6, 4, 0, 9, 0],
      [9, 0, 0, 0, 0, 0, 8, 1, 6],
      [0, 8, 0, 3, 9, 6, 0, 0, 0],
      [7, 0, 2, 0, 4, 0, 3, 0, 9],
      [0, 0, 0, 5, 7, 2, 0, 8, 0],
      [5, 2, 1, 0, 0, 0, 0, 0, 4],
      [0, 3, 0, 7, 5, 0, 2, 0, 0],
      [0, 0, 0, 0, 2, 0, 1, 0, 5]]
e4 = [[3, 8, 0, 9, 0, 0, 2, 0, 5],
      [0, 0, 0, 0, 0, 8, 7, 3, 0],
      [0, 6, 0, 3, 0, 0, 9, 8, 0],
      [0, 0, 0, 0, 0, 3, 5, 0, 1],
      [9, 1, 0, 5, 0, 7, 0, 2, 3],
      [7, 0, 3, 1, 0, 0, 0, 0, 0],
      [0, 3, 5, 0, 0, 1, 0, 9, 0],
      [0, 7, 4, 6, 0, 0, 0, 0, 0],
      [8, 0, 1, 0, 0, 2, 0, 6, 7]]
e5 = [[6, 0, 0, 0, 0, 9, 0, 0, 4],
      [0, 8, 9, 5, 0, 0, 0, 1, 6],
      [5, 0, 0, 0, 6, 0, 3, 0, 9],
      [8, 3, 1, 0, 0, 0, 7, 0, 5],
      [0, 2, 0, 0, 0, 0, 0, 6, 0],
      [9, 0, 7, 0, 0, 0, 8, 4, 2],
      [2, 0, 6, 0, 1, 0, 0, 0, 8],
      [3, 7, 0, 0, 0, 6, 9, 2, 0],
      [1, 0, 0, 3, 0, 0, 0, 0, 7]]
# sudoku questions obtained from: https://sudokuessentials.com/easy_sudoku/
e6 = [[8, 0, 0, 9, 3, 0, 0, 0, 2],
      [0, 0, 9, 0, 0, 0, 0, 4, 0],
      [7, 0, 2, 1, 0, 0, 9, 6, 0],
      [2, 0, 0, 0, 0, 0, 0, 9, 0],
      [0, 6, 0, 0, 0, 0, 0, 7, 0],
      [0, 7, 0, 0, 0, 6, 0, 0, 5],
      [0, 2, 7, 0, 0, 8, 4, 0, 6],
      [0, 3, 0, 0, 0, 0, 5, 0, 0],
      [5, 0, 0, 0, 6, 2, 0, 0, 8]]
e7 = [[0, 0, 0, 0, 0, 6, 0, 8, 0],
      [0, 0, 9, 1, 0, 5, 3, 7, 2],
      [0, 8, 0, 7, 0, 0, 0, 1, 6],
      [0, 0, 0, 0, 0, 0, 0, 3, 4],
      [0, 0, 0, 3, 5, 1, 0, 0, 0],
      [7, 3, 0, 0, 0, 0, 0, 0, 0],
      [6, 1, 0, 0, 0, 8, 0, 2, 0],
      [8, 2, 3, 9, 0, 4, 6, 0, 0],
      [0, 7, 0, 6, 0, 0, 0, 0, 0]]
e8 = [[8, 3, 0, 0, 2, 9, 0, 0, 0],
      [0, 9, 0, 7, 0, 0, 0, 6, 0],
      [4, 0, 0, 0, 1, 0, 2, 0, 0],
      [0, 4, 8, 0, 0, 2, 0, 1, 9],
      [0, 0, 9, 0, 0, 0, 4, 0, 0],
      [1, 2, 0, 9, 0, 0, 3, 5, 0],
      [0, 0, 4, 0, 6, 0, 0, 0, 7],
      [0, 5, 0, 0, 0, 1, 0, 2, 0],
      [0, 0, 0, 3, 5, 0, 0, 4, 1]]
e9 = [[0, 8, 2, 0, 0, 0, 7, 0, 0],
      [0, 9, 0, 2, 0, 6, 0, 4, 0],
      [3, 0, 0, 0, 8, 0, 0, 0, 5],
      [0, 0, 3, 0, 0, 0, 0, 0, 6],
      [0, 5, 8, 0, 0, 1, 2, 3, 0],
      [7, 0, 0, 0, 0, 3, 8, 0, 0],
      [6, 0, 0, 0, 4, 0, 0, 0, 2],
      [0, 2, 0, 9, 0, 7, 0, 5, 0],
      [0, 0, 5, 0, 0, 0, 4, 7, 0]]
e10 = [[0, 0, 0, 2, 0, 4, 0, 9, 0],
       [5, 0, 0, 0, 1, 0, 8, 0, 4],
       [7, 3, 0, 9, 0, 0, 0, 0, 0],
       [0, 0, 6, 0, 0, 0, 0, 1, 0],
       [0, 0, 9, 0, 0, 0, 4, 0, 0],
       [0, 5, 0, 0, 0, 0, 9, 0, 0],
       [0, 0, 0, 0, 0, 2, 0, 7, 1],
       [4, 0, 5, 0, 3, 0, 0, 0, 2],
       [0, 1, 0, 8, 0, 6, 0, 0, 0]]
# sudoku obtained from: https://www.rd.com/list/printable-sudoku-puzzles/
m1 = [[5, 0, 7, 2, 0, 0, 0, 9, 0],
      [0, 0, 6, 0, 3, 0, 7, 0, 1],
      [4, 0, 0, 0, 0, 0, 0, 6, 0],
      [1, 0, 0, 4, 9, 0, 0, 0, 7],
      [0, 0, 0, 5, 0, 8, 0, 0, 0],
      [8, 0, 0, 0, 2, 7, 0, 0, 5],
      [0, 7, 0, 0, 0, 0, 0, 0, 9],
      [2, 0, 9, 0, 8, 0, 6, 0, 0],
      [0, 4, 0, 0, 0, 9, 3, 0, 8]]
m2 = [[2, 0, 0, 0, 0, 0, 6, 9, 0],
      [0, 5, 0, 0, 0, 3, 0, 0, 0],
      [1, 7, 0, 0, 0, 9, 4, 0, 5],
      [0, 0, 3, 0, 2, 5, 0, 1, 8],
      [0, 0, 0, 0, 4, 0, 0, 0, 0],
      [7, 2, 0, 3, 8, 0, 5, 0, 0],
      [5, 0, 2, 6, 0, 0, 0, 4, 1],
      [0, 0, 0, 5, 0, 0, 0, 7, 0],
      [0, 6, 7, 0, 0, 0, 0, 0, 3]]
m3 = [[1, 5, 0, 2, 0, 9, 0, 0, 4],
      [0, 4, 0, 0, 0, 6, 0, 0, 0],
      [0, 0, 0, 0, 4, 0, 0, 6, 3],
      [0, 7, 0, 0, 0, 0, 8, 0, 6],
      [6, 0, 0, 0, 0, 0, 0, 0, 5],
      [2, 0, 8, 0, 0, 0, 0, 1, 0],
      [4, 6, 0, 0, 8, 0, 0, 0, 0],
      [0, 0, 0, 6, 0, 0, 0, 7, 0],
      [8, 0, 0, 5, 0, 1, 0, 4, 9]]
m4 = [[3, 4, 0, 0, 6, 0, 2, 0, 9],
      [2, 0, 8, 4, 9, 0, 0, 0, 6],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 2, 1, 3, 1, 0, 0, 0, 0],
      [0, 0, 4, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 2, 5, 0, 4, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [9, 0, 0, 0, 5, 1, 4, 0, 3],
      [4, 0, 3, 0, 7, 0, 0, 6, 8]]
m5 = [[0, 2, 6, 0, 3, 0, 0, 0, 8],
      [9, 0, 0, 6, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 9, 0, 4, 0],
      [0, 0, 7, 3, 0, 2, 0, 0, 0],
      [0, 0, 4, 0, 7, 0, 8, 0, 0],
      [0, 0, 0, 8, 0, 6, 7, 0, 0],
      [0, 5, 0, 7, 2, 0, 0, 0, 0],
      [0, 0, 9, 0, 0, 5, 0, 0, 4],
      [4, 0, 0, 0, 6, 0, 2, 1, 0]]
h1 = [[0, 0, 6, 5, 0, 0, 0, 0, 8],
      [0, 9, 5, 0, 0, 0, 0, 2, 0],
      [7, 0, 0, 9, 0, 0, 3, 0, 0],
      [0, 0, 0, 0, 4, 0, 2, 7, 0],
      [0, 0, 0, 8, 7, 3, 0, 0, 0],
      [0, 7, 9, 0, 5, 0, 0, 0, 0],
      [0, 0, 2, 0, 0, 8, 0, 0, 9],
      [0, 5, 0, 0, 0, 0, 8, 1, 0],
      [3, 0, 0, 0, 0, 5, 4, 0, 0]]
h2 = [[0, 9, 1, 0, 7, 0, 0, 0, 0],
      [2, 0, 3, 0, 0, 0, 0, 5, 0],
      [0, 0, 0, 4, 0, 2, 9, 0, 7],
      [0, 0, 2, 8, 0, 6, 0, 0, 9],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [9, 0, 0, 1, 0, 4, 6, 0, 0],
      [1, 0, 5, 2, 0, 7, 0, 0, 0],
      [0, 8, 0, 0, 0, 0, 5, 0, 1],
      [0, 0, 0, 0, 1, 0, 7, 6, 0]]
h3 = [[0, 0, 2, 7, 8, 0, 0, 0, 3],
      [0, 0, 0, 0, 0, 9, 8, 0, 1],
      [4, 0, 0, 0, 0, 3, 0, 7, 0],
      [9, 0, 5, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 7, 0, 0, 0, 0],
      [0, 0, 0, 5, 0, 0, 4, 0, 8],
      [0, 6, 0, 4, 0, 0, 0, 0, 7],
      [3, 0, 9, 8, 0, 0, 0, 0, 0],
      [8, 0, 0, 0, 3, 1, 6, 0, 0]]
h4 = [[0, 8, 7, 3, 0, 4, 0, 0, 0],
      [0, 3, 0, 5, 0, 0, 0, 4, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 7],
      [0, 0, 0, 0, 0, 2, 4, 5, 0],
      [0, 9, 6, 0, 1, 0, 8, 3, 0],
      [0, 2, 5, 8, 0, 0, 0, 0, 0],
      [8, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 5, 0, 0, 0, 7, 0, 1, 0],
      [0, 0, 0, 2, 0, 1, 7, 6, 0]]
h5 = [[0, 0, 1, 3, 0, 2, 0, 0, 0],
      [0, 0, 3, 0, 0, 7, 0, 4, 5],
      [0, 0, 7, 0, 0, 0, 0, 0, 9],
      [0, 0, 6, 5, 0, 0, 0, 7, 0],
      [2, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 9, 0, 0, 0, 1, 4, 0, 0],
      [5, 0, 0, 0, 0, 0, 9, 0, 0],
      [6, 1, 0, 2, 0, 0, 8, 0, 0],
      [0, 0, 0, 9, 0, 8, 5, 0, 0]]

Sudoku()
