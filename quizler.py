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
import random

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
                                        font = ("Arial", "35"))
        self.lbl_frame_title.grid(row = 0, column = 0, sticky = "news")
        
        #Play Button
        self.btn_play = tk.Button(self, text = "Play!", bg="blue", font = ("Arial", "15"), command = self.go_play)
        self.btn_play.grid(row = 1, column = 0)
        
        #Scoreboard Button
        self.btn_scoreboard = tk.Button(self, text = "Scoreboard", bg = "blue",command=self.go_highscore,
                                        font = ("Arial","15"))
        self.btn_scoreboard.grid(row = 2, column = 0)

        self.btn_add=tk.Button(self, text = "Add Questions", bg="blue", command=self.go_new,
                                          font=("Arial","15"))
        self.btn_add.grid(row = 3,column = 0)
        
        
    def go_play(self):
        Screen.current=1
        Screen.switch_frame()
        
    def go_new(self):
        Screen.current=2
        Screen.switch_frame()
        
    def go_highscore(self):
        Screen.current=3
        Screen.switch_frame()        
        
        
        
        
class PlaySelect(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title=tk.Label(self, text = "Select your Category",
                                font = ("Arial","25"))
        self.lbl_title.grid(row = 0, column = 1, sticky = "news")
        
        
        self.btn_random = tk.Button(self, text = "Random", bg="blue", font = ("Arial", "15"))
        self.btn_random.grid(row = 1, column = 1)
        
        self.btn_history = tk.Button(self, text = "History", bg="blue", font = ("Arial", "15"))
        self.btn_history.grid(row = 2, column = 0)
        
        self.btn_geography = tk.Button(self, text = "Geography", bg="blue", font = ("Arial", "15"))
        self.btn_geography.grid(row = 2, column = 2)
        
        self.btn_games = tk.Button(self, text = "Games", bg="blue", font = ("Arial", "15"), command = self.go_games)
        self.btn_games.grid(row = 3, column = 0)
        
        self.btn_music = tk.Button(self, text = "Music", bg="blue", font = ("Arial", "15"))
        self.btn_music.grid(row = 3, column = 2)      
        
        self.btn_back = tk.Button(self, text = "Go Back", bg="blue", font = ("Arial", "15"), command=self.go_main)
        self.btn_back.grid(row = 4, column = 1)        
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def go_games(self):        
        Screen.current = 4
        Screen.switch_frame()
        
class NewSelect(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title=tk.Label(self, text = "Select your Category",
                                font = ("Arial","25"))
        self.lbl_title.grid(row = 0, column = 1, sticky = "news")
        
        
        self.btn_random = tk.Button(self, text = "Random", bg="blue", font = ("Arial", "15"))
        self.btn_random.grid(row = 1, column = 1)
        
        self.btn_history = tk.Button(self, text = "History", bg="blue", font = ("Arial", "15"))
        self.btn_history.grid(row = 2, column = 0)
        
        self.btn_geography = tk.Button(self, text = "Geography", bg="blue", font = ("Arial", "15"))
        self.btn_geography.grid(row = 2, column = 2)
        
        self.btn_games = tk.Button(self, text = "Games", bg="blue", font = ("Arial", "15"))
        self.btn_games.grid(row = 3, column = 0)
        
        self.btn_music = tk.Button(self, text = "Music", bg="blue", font = ("Arial", "15"))
        self.btn_music.grid(row = 3, column = 2) 
        
        self.btn_back = tk.Button(self, text = "Go Back", bg="blue", font = ("Arial", "15"), command=self.go_main)
        self.btn_back.grid(row = 4, column = 1)        
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()        
        
        
class HighscoreSelect(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.lbl_title=tk.Label(self, text = "Select your Category",
                                font = ("Arial","25"))
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        
        self.btn_random = tk.Button(self, text = "Random", bg="blue", font = ("Arial", "15"))
        self.btn_random.grid(row = 1, column = 0, columnspan = 2)
        
        self.btn_history = tk.Button(self, text = "History", bg="blue", font = ("Arial", "15"))
        self.btn_history.grid(row = 2, column = 0)
        
        self.btn_geography = tk.Button(self, text = "Geography", bg="blue", font = ("Arial", "15"))
        self.btn_geography.grid(row = 2, column = 1)
        
        self.btn_games = tk.Button(self, text = "Games", bg="blue", font = ("Arial", "15"))
        self.btn_games.grid(row = 3, column = 0)
        
        self.btn_music = tk.Button(self, text = "Music", bg="blue", font = ("Arial", "15"))
        self.btn_music.grid(row = 3, column = 1)         
        
        self.btn_back = tk.Button(self, text = "Go Back", bg="blue", font = ("Arial", "15"), command=self.go_main)
        self.btn_back.grid(row = 4, column = 0, columnspan = 2)        
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()        
    
    
class GamesQuiz(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        pickle_file = open("games.pickle", "rb")
        questions = pickle.load(pickle_file)
        pickle_file.close()        
        
        q = random.randint(1,2)
        self.correct_answer = questions[q][-1]
        self.chosen_answer = tk.IntVar(self)
        self.chosen_answer.set(0)
        
        self.lbl_title=tk.Label(self, text = questions[q][0], font = ("Arial","20"))
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.a1=tk.Radiobutton(self, text = questions[q][1], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 1)
        self.a1.grid(row = 1, column = 0)
        
        self.a2=tk.Radiobutton(self, text = questions[q][2], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 2)
        self.a2.grid(row = 1, column = 1)
        
        self.a3=tk.Radiobutton(self, text = questions[q][3], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 3)
        self.a3.grid(row = 2, column = 0)
        
        self.a4=tk.Radiobutton(self, text = questions[q][4], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 4)
        self.a4.grid(row = 2, column = 1)        
        
        #self.btn_give_up=tk.Button(self, text = "Give Up", bg="blue", font = ("Arial", "15"), command = self.go_main)
        #self.btn_give_up.grid(row = 3, column = 0, columnspan = 2)        
        
        self.btn_give_up=tk.Button(self, text = "Give Up", bg="blue", font = ("Arial", "15"), command = self.go_main)
        self.btn_give_up.grid(row = 3, column = 0, columnspan = 2)
        
    def go_main(self):
        if self.chosen_answer == self.correct_answer:
            Screen.current = 0
            Screen.switch_frame()
        
    #def answer_sumbit(self, choice):
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Quizler, the Trivia Game")

    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    
    screens=[]                
    screens.append(MainMenu())
    screens.append(PlaySelect())
    screens.append(NewSelect())
    screens.append(HighscoreSelect())
    screens.append(GamesQuiz())
    
    screens[0].grid(row=0, column=0,sticky="news")
    screens[1].grid(row=0, column=0,sticky="news")
    screens[2].grid(row=0, column=0,sticky="news")
    screens[3].grid(row=0, column=0,sticky="news")    
    screens[4].grid(row=0, column=0,sticky="news")
    
    Screen.current=0
    Screen.switch_frame()     
    
    root.mainloop() 