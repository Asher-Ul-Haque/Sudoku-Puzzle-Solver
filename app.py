#IMPORTS-
import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int

#===============================================================================

#FONTS-
mainFont=('Consolas', 64, 'bold')
sideFont=('Consolas', 30, 'bold')

#===============================================================================

#COLORS-
lightModeMain='#42CBF5'
darkModeMain='#F7AA05'

#===============================================================================

# SETTING UP THE ROOT
class App(ctk.CTk):
    def __init__(self): #basic setup
        super().__init__()
        self.geometry('480x360')
        self.title('Sudoku-Puzzle-Solver')
        self.resizable(False, False)
        ctk.set_appearance_mode('light')
        #window color
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0xF5CB42)), sizeof(c_int))
        except:
            pass
root=App()

#===============================================================================

#START WINDOW BUTTONS
class startWindowButtons(ctk.CTkButton):
    def __init__(self, text, command):
        super().__init__(text=text,
                         command=command,
                         master=root,
                         font=sideFont,
                         fg_color='transparent',
                         text_color=(lightModeMain, darkModeMain))

startButton=startWindowButtons(text='START GAME',
                               command=lambda: print('start'))
#===============================================================================

#START WINDOW LABELS
nameLabel=ctk.CTkLabel(text='Sudoku',
                       master=root,
                       font=mainFont,
                       text_color=(lightModeMain, darkModeMain),
                       fg_color='transparent',
                       width=100)

nameLabel.place(relx=0.75, rely=0.1, anchor='center')

#===============================================================================

root.mainloop()
