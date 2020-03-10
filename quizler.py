#!/usr/bin/python3
# GameFinder.py
# Connor Gray, and austin Heidemann
# 3/9/2020

'''allow the user to take quizzes, view their high scores, and add their own
questions to the quizzes'''

import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import *

class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)

    def switch_frame():
        screens[Screen.current].tkraise()

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        #Frame Header
        self.lbl_frame_title = tk.Label(self, text = "QUIZLER",
                                        font = ("Arial", "25"))
        self.lbl_frame_title.grid(row = 0, column = 0, sticky = "news")
        
        #Play Button
        self.btn_play = tk.Button(self, text = "Play!", bg="blue",
                                 font = ("Arial", "15"))
        self.btn_play.grid(row = 1, column = 0)
        
        #Scoreboard Button
        self.btn_scoreboard = tk.Button(self, text = "Scoreboard", bg = "blue",
                                        font = ("Arial","15"))
        self.btn_scoreboard.grid(row = 2, column = 0)

        self.btn_add=tk.Button(self, text = "Add Questions", bg="blue",
                                          font=("Arial","15"))
        self.btn_add.grid(row = 3,column = 0)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Quizler, the Trivia Game")

    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    
    screens=[]                
    screens.append(MainMenu())
    
    screens[0].grid(row=0, column=0,sticky="news")
    
    Screen.current=0
    Screen.switch_frame()     
    
    root.mainloop() 