import pickle

Questions = {1:["What is the main character of Halo?", "Private Pile", "Master Chief", "Frost", "Soap", 2],
             2:["Which pokemon has no type disadvantage?", "Dugtrio", "Shuckle", "Tepig", "Eelectros", 4], 
             3:["What are the proffesions of Mario and his brother Luigi?", "Teachers", "Exterminators", "Plumbers", "Zookeepers", 3],
             4:["In which of these countries did the Nintendo Wii NOT come bundled with a copy of Wii Sports?", "South Korea", "Russia", "Canada", "Japan", 4],
             5:["Question 5", "reee1", "reee2", "reee3", "reee4", 1],
             6:["Question 6", "reeee1", "reeee2", "reeee3", "reeee4", 4] }

games = open("games.pickle","wb")
pickle.dump(Questions, games)
games.close

