import pickle

Questions = {1:["Question 1", "Answer 1", "Answer 2", "Answer 3", "Answer 4", 2], 2:["Question 2", "A1", "A2", "A3", "A4", 4]}

games = open("games.pickle","wb")
pickle.dump(Questions, games)
games.close

