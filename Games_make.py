import pickle

Questions = {1:["What is the main character of Halo?", "Private Pile", "Master Chief", "Frost", "Soap", 2],
             2:["Which pokemon has no type disadvantage?", "Dugtrio", "Shuckle", "Tepig", "Eelectros", 4], 
             3:["What are the professions of Mario and his brother Luigi?", "Teachers", "Exterminators", "Plumbers", "Zookeepers", 3],
             4:["In which of these countries did the Nintendo Wii NOT come bundled with a copy of Wii Sports?", "South Korea", "Russia", "Canada", "Japan", 4],
             5:["What Board game helped POW's escape during WW2", "Monopoly","Chutes and Latters",  "Battleship", "Candy land", 1],
             6:["What country is tetris from", "North Korea", "Kenya", "Ireland", "Russia", 4], 
             7:["In which game can you find dog meat in cake of broken dreams", "Star wars:KOTOR","Fallout 2",  "Final Fantasy", "EarthBound", 2],
             8:["What does Atari mean", "Winner","Best",  "Success", "Revolution", 3], 
             9:["When was minecraft released", "2009","1998",  "2006", "2016", 1],
             10:["Who was the enemy in Homefront", "The U.S Govt","The Korean army",  "Space Nazis", "Aliens", 2],
             11:["What game is the character master hands portayed in", "Halo","Call of duty",  "Street Fighter", "Smash", 4],
             12:["In the metal gear series who is Liquid snakes brother", "Snakeus Wakeus","Ho Chi Minh",  "Solid Snake", "Zoidberg", 3],}

games = open("games.pickle","wb")
pickle.dump(Questions, games)
games.close

