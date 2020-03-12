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
        
        self.btn_history = tk.Button(self, text = "History", bg="blue", font = ("Arial", "15"),command = self.go_history)
        self.btn_history.grid(row = 2, column = 0)
        
        self.btn_geography = tk.Button(self, text = "Geography", bg="blue", font = ("Arial", "15"), command = self.go_geo)
        self.btn_geography.grid(row = 2, column = 2)
        
        self.btn_games = tk.Button(self, text = "Games", bg="blue", font = ("Arial", "15"), command = self.go_games)
        self.btn_games.grid(row = 3, column = 0)
        
        self.btn_music = tk.Button(self, text = "Music", bg="blue", font = ("Arial", "15"),command = self.go_music)
        self.btn_music.grid(row = 3, column = 2)      
        
        self.btn_back = tk.Button(self, text = "Go Back", bg="blue", font = ("Arial", "15"), command=self.go_main)
        self.btn_back.grid(row = 4, column = 1)        
        
    def go_main(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def go_games(self):        
        Screen.current = 4
        Screen.switch_frame()
            
    def go_music(self):        
        Screen.current = 5
        Screen.switch_frame()
        
    def go_history(self):        
        Screen.current = 6
        Screen.switch_frame()
        
    def go_geo(self):        
        Screen.current = 7
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
        self.questions = pickle.load(pickle_file)
        pickle_file.close()        
        
        self.score = 0
        self.question_numb = 1
        self.used_questions = list()
        self.q = random.randint(1,len(self.questions))
        self.used_questions.append(self.q)
        self.correct_answer = int(self.questions[self.q][5])
        self.chosen_answer = tk.IntVar(self)
        self.chosen_answer.set(0)
        
        self.lbl_title=tk.Label(self, text = self.questions[self.q][0], font = ("Arial","20"))
        self.lbl_title.grid(row = 1, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_score=tk.Label(self, text = ("Score:" + str(self.score)), font = ("Arial", "20"))
        self.lbl_score.grid(row = 0, column = 3, sticky = "news")
        
        self.lbl_question_num=tk.Label(self, text = ("Question:" + str(self.question_numb)), font = ("Arial", "20"))
        self.lbl_question_num.grid(row = 0, column = 0, sticky = "news")        
        
        self.a1=tk.Radiobutton(self, text = self.questions[self.q][1], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 1)
        self.a1.grid(row = 2, column = 1)
        
        self.a2=tk.Radiobutton(self, text = self.questions[self.q][2], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 2)
        self.a2.grid(row = 2, column = 2)
        
        self.a3=tk.Radiobutton(self, text = self.questions[self.q][3], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 3)
        self.a3.grid(row = 3, column = 1)
        
        self.a4=tk.Radiobutton(self, text = self.questions[self.q][4], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 4)
        self.a4.grid(row = 3, column = 2)        
        
        self.btn_give_up=tk.Button(self, text = "Give Up", bg="blue", font = ("Arial", "15"), command = self.go_main)
        self.btn_give_up.grid(row = 4, column = 1)        
        
        self.btn_next=tk.Button(self, text = "Next", bg="blue", font = ("Arial", "15"), command = self.go_next)
        self.btn_next.grid(row = 4, column =2)
        
    def go_main(self):
        #print(self.correct_answer, self.chosen_answer.get())
        #if self.correct_answer == self.chosen_answer.get():
        self.score=0
        self.lbl_score.configure(text="Score:" + str(self.score))
        Screen.current = 0
        Screen.switch_frame()
    
    def go_next(self):
        if self.correct_answer == self.chosen_answer.get():
            self.score += 10
            self.question_numb += 1
            if self.question_numb <= 10:
                while self.q in self.used_questions:
                    self.q = random.randint(1, len(self.questions))
                self.used_questions.append(self.q)
                self.lbl_score.configure(text="Score:" + str(self.score))
                self.lbl_question_num.configure(text="Question:"+str(self.question_numb))
                self.lbl_title.configure(text=self.questions[self.q][0])
                self.a1.configure(text=self.questions[self.q][1])
                self.a2.configure(text=self.questions[self.q][2])
                self.a3.configure(text=self.questions[self.q][3])
                self.a4.configure(text=self.questions[self.q][4])
                self.correct_answer = self.questions[self.q][5]
                self.update
                
            if self.question_numb == 10: 
                Screen.current = 0
                Screen.switch_frame()                
                
        else:
            self.score -= 5
            self.lbl_score.configure(text="Score:" + str(self.score))
            self.update
    #def randomize(self, ls):
        
    #def answer_sumbit(self, choice):
    
class MusicQuiz(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        pickle_file = open("music.pickle", "rb")
        self.questions = pickle.load(pickle_file)
        pickle_file.close()        
        
        self.score = 0
        self.question_numb = 1
        self.used_questions = list()
        self.q = random.randint(1,len(self.questions))
        self.used_questions.append(self.q)
        self.correct_answer = int(self.questions[self.q][5])
        self.chosen_answer = tk.IntVar(self)
        self.chosen_answer.set(0)
        
        self.lbl_title=tk.Label(self, text = self.questions[self.q][0], font = ("Arial","20"))
        self.lbl_title.grid(row = 1, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_score=tk.Label(self, text = ("Score:" + str(self.score)), font = ("Arial", "20"))
        self.lbl_score.grid(row = 0, column = 3, sticky = "news")
        
        self.lbl_question_num=tk.Label(self, text = ("Question:" + str(self.question_numb)), font = ("Arial", "20"))
        self.lbl_question_num.grid(row = 0, column = 0, sticky = "news")        
        
        self.a1=tk.Radiobutton(self, text = self.questions[self.q][1], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 1)
        self.a1.grid(row = 2, column = 1)
        
        self.a2=tk.Radiobutton(self, text = self.questions[self.q][2], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 2)
        self.a2.grid(row = 2, column = 2)
        
        self.a3=tk.Radiobutton(self, text = self.questions[self.q][3], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 3)
        self.a3.grid(row = 3, column = 1)
        
        self.a4=tk.Radiobutton(self, text = self.questions[self.q][4], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 4)
        self.a4.grid(row = 3, column = 2)        
        
        self.btn_give_up=tk.Button(self, text = "Give Up", bg="blue", font = ("Arial", "15"), command = self.go_main)
        self.btn_give_up.grid(row = 4, column = 1)        
        
        self.btn_next=tk.Button(self, text = "Next", bg="blue", font = ("Arial", "15"), command = self.go_next)
        self.btn_next.grid(row = 4, column =2)
        
    def go_main(self):
        #print(self.correct_answer, self.chosen_answer.get())
        #if self.correct_answer == self.chosen_answer.get():
        self.score=0
        self.lbl_score.configure(text="Score:" + str(self.score))
        Screen.current = 0
        Screen.switch_frame()
    
    def go_next(self):
        if self.correct_answer == self.chosen_answer.get():
            self.score += 10
            self.question_numb += 1
            if self.question_numb <= 10:
                while self.q in self.used_questions:
                    self.q = random.randint(1, len(self.questions))
                self.used_questions.append(self.q)
                self.lbl_score.configure(text="Score:" + str(self.score))
                self.lbl_question_num.configure(text="Question:"+str(self.question_numb))
                self.lbl_title.configure(text=self.questions[self.q][0])
                self.a1.configure(text=self.questions[self.q][1])
                self.a2.configure(text=self.questions[self.q][2])
                self.a3.configure(text=self.questions[self.q][3])
                self.a4.configure(text=self.questions[self.q][4])
                self.correct_answer = self.questions[self.q][5]
                self.update
                
            if self.question_numb == 10: 
                Screen.current = 0
                Screen.switch_frame()                
                
        else:
            self.score -= 5
            self.lbl_score.configure(text="Score:" + str(self.score))
            self.update
            
            
            
            
            
            
class HistoryQuiz(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        pickle_file = open("history.pickle", "rb")
        self.questions = pickle.load(pickle_file)
        pickle_file.close()        
        
        self.score = 0
        self.question_numb = 1
        self.used_questions = list()
        self.q = random.randint(1,len(self.questions))
        self.used_questions.append(self.q)
        self.correct_answer = int(self.questions[self.q][5])
        self.chosen_answer = tk.IntVar(self)
        self.chosen_answer.set(0)
        
        self.lbl_title=tk.Label(self, text = self.questions[self.q][0], font = ("Arial","20"))
        self.lbl_title.grid(row = 1, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_score=tk.Label(self, text = ("Score:" + str(self.score)), font = ("Arial", "20"))
        self.lbl_score.grid(row = 0, column = 3, sticky = "news")
        
        self.lbl_question_num=tk.Label(self, text = ("Question:" + str(self.question_numb)), font = ("Arial", "20"))
        self.lbl_question_num.grid(row = 0, column = 0, sticky = "news")        
        
        self.a1=tk.Radiobutton(self, text = self.questions[self.q][1], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 1)
        self.a1.grid(row = 2, column = 1)
        
        self.a2=tk.Radiobutton(self, text = self.questions[self.q][2], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 2)
        self.a2.grid(row = 2, column = 2)
        
        self.a3=tk.Radiobutton(self, text = self.questions[self.q][3], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 3)
        self.a3.grid(row = 3, column = 1)
        
        self.a4=tk.Radiobutton(self, text = self.questions[self.q][4], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 4)
        self.a4.grid(row = 3, column = 2)        
        
        self.btn_give_up=tk.Button(self, text = "Give Up", bg="blue", font = ("Arial", "15"), command = self.go_main)
        self.btn_give_up.grid(row = 4, column = 1)        
        
        self.btn_next=tk.Button(self, text = "Next", bg="blue", font = ("Arial", "15"), command = self.go_next)
        self.btn_next.grid(row = 4, column =2)
        
    def go_main(self):
        #print(self.correct_answer, self.chosen_answer.get())
        #if self.correct_answer == self.chosen_answer.get():
        self.score=0
        self.lbl_score.configure(text="Score:" + str(self.score))
        Screen.current = 0
        Screen.switch_frame()
    
    def go_next(self):
        if self.correct_answer == self.chosen_answer.get():
            self.score += 10
            self.question_numb += 1
            if self.question_numb <= 10:
                while self.q in self.used_questions:
                    self.q = random.randint(1, len(self.questions))
                self.used_questions.append(self.q)
                self.lbl_score.configure(text="Score:" + str(self.score))
                self.lbl_question_num.configure(text="Question:"+str(self.question_numb))
                self.lbl_title.configure(text=self.questions[self.q][0])
                self.a1.configure(text=self.questions[self.q][1])
                self.a2.configure(text=self.questions[self.q][2])
                self.a3.configure(text=self.questions[self.q][3])
                self.a4.configure(text=self.questions[self.q][4])
                self.correct_answer = self.questions[self.q][5]
                self.update
                
            if self.question_numb == 10: 
                Screen.current = 0
                Screen.switch_frame()                
                
        else:
            self.score -= 5
            self.lbl_score.configure(text="Score:" + str(self.score))
            self.update    
            


class GeoQuiz(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        pickle_file = open("geo.pickle", "rb")
        self.questions = pickle.load(pickle_file)
        pickle_file.close()        
        
        self.score = 0
        self.question_numb = 1
        self.used_questions = list()
        self.q = random.randint(1,len(self.questions))
        self.used_questions.append(self.q)
        self.correct_answer = int(self.questions[self.q][5])
        self.chosen_answer = tk.IntVar(self)
        self.chosen_answer.set(0)
        
        self.lbl_title=tk.Label(self, text = self.questions[self.q][0], font = ("Arial","20"))
        self.lbl_title.grid(row = 1, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_score=tk.Label(self, text = ("Score:" + str(self.score)), font = ("Arial", "20"))
        self.lbl_score.grid(row = 0, column = 3, sticky = "news")
        
        self.lbl_question_num=tk.Label(self, text = ("Question:" + str(self.question_numb)), font = ("Arial", "20"))
        self.lbl_question_num.grid(row = 0, column = 0, sticky = "news")        
        
        self.a1=tk.Radiobutton(self, text = self.questions[self.q][1], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 1)
        self.a1.grid(row = 2, column = 1)
        
        self.a2=tk.Radiobutton(self, text = self.questions[self.q][2], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 2)
        self.a2.grid(row = 2, column = 2)
        
        self.a3=tk.Radiobutton(self, text = self.questions[self.q][3], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 3)
        self.a3.grid(row = 3, column = 1)
        
        self.a4=tk.Radiobutton(self, text = self.questions[self.q][4], bg="blue", font = ("Arial", "15"), variable = self.chosen_answer,value = 4)
        self.a4.grid(row = 3, column = 2)        
        
        self.btn_give_up=tk.Button(self, text = "Give Up", bg="blue", font = ("Arial", "15"), command = self.go_main)
        self.btn_give_up.grid(row = 4, column = 1)        
        
        self.btn_next=tk.Button(self, text = "Next", bg="blue", font = ("Arial", "15"), command = self.go_next)
        self.btn_next.grid(row = 4, column =2)
        
    def go_main(self):
        #print(self.correct_answer, self.chosen_answer.get())
        #if self.correct_answer == self.chosen_answer.get():
        self.score=0
        self.lbl_score.configure(text="Score:" + str(self.score))
        Screen.current = 0
        Screen.switch_frame()
    
    def go_next(self):
        if self.correct_answer == self.chosen_answer.get():
            self.score += 10
            self.question_numb += 1
            if self.question_numb <= 10:
                while self.q in self.used_questions:
                    self.q = random.randint(1, len(self.questions))
                self.used_questions.append(self.q)
                self.lbl_score.configure(text="Score:" + str(self.score))
                self.lbl_question_num.configure(text="Question:"+str(self.question_numb))
                self.lbl_title.configure(text=self.questions[self.q][0])
                self.a1.configure(text=self.questions[self.q][1])
                self.a2.configure(text=self.questions[self.q][2])
                self.a3.configure(text=self.questions[self.q][3])
                self.a4.configure(text=self.questions[self.q][4])
                self.correct_answer = self.questions[self.q][5]
                self.update
                
            if self.question_numb == 10: 
                Screen.current = 0
                Screen.switch_frame()                
                
        else:
            self.score -= 5
            self.lbl_score.configure(text="Score:" + str(self.score))
            self.update    
                    
        
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
    screens.append(MusicQuiz())
    screens.append(HistoryQuiz())
    screens.append(GeoQuiz())
    
    screens[0].grid(row=0, column=0,sticky="news")
    screens[1].grid(row=0, column=0,sticky="news")
    screens[2].grid(row=0, column=0,sticky="news")
    screens[3].grid(row=0, column=0,sticky="news")    
    screens[4].grid(row=0, column=0,sticky="news")
    screens[5].grid(row=0, column=0,sticky="news")
    screens[6].grid(row=0, column=0,sticky="news")
    screens[7].grid(row=0, column=0,sticky="news")
    
    Screen.current=0
    Screen.switch_frame()     
    
    root.mainloop()  