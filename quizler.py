#!/usr/bin/python3
# GameFinder.py
# Connor Gray, and austin Heidemann
# 3/9/2020

#thisl be like the game finder program but GUI based

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




        self.lbl_title = tk.Label(self,text="Game Library",font=("Arial","25"))
        self.lbl_title.grid(row=0,column=0,sticky="news")

        self.btn_add=tk.Button(self,text="Add",bg="blue",font=("Arial","15"))
        self.btn_add.grid(row=1,column=0)



        self.btn_edit=tk.Button(self,text="Play select",bg="blue",font=("Arial","15"))
        self.btn_edit.grid(row=2,column=0)

        self.btn_search=tk.Button(self,text="Highscore", bg="blue",
                                          font=("Arial","15"))
        self.btn_search.grid(row=3,column=0)

 

        #you can search stuff up here



  
        
        
        
if __name__ == "__main__":
        root = tk.Tk()
        root.geometry("1280x720")
        root.title("Quizler, the trivia game")
    
        root.grid_columnconfigure(0,weight=1)
        root.grid_rowconfigure(0,weight=1)

        
        
        
        screens=[]                
        screens.append(MainMenu())
     
        
        screens[0].grid(row=0, column=0,sticky="news")

        
        Screen.current=0
        Screen.switch_frame()     
        
        root.mainloop() 