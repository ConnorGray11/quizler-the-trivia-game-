import pickle

Questions = {1:["how long did it take for poland to be annexed at the start of world war two?", "12 days", "35 days", "30 days", "60 days", 2],
             2:["How long did the longest war last?", "154 years", "57 years", "409 years", "335", 4], 
             3:["Who's death caused the first world war?", "Gavrillo Princep", "Otto Von Bismark", "Franz Ferdinand", "Dwight D. Eisenhower", 3],
             4:["What Objest Allowed for us to understand ancient egyptian?", "Rock of gibraltr", "The Blarney stone", "Ayer's Rock", "The Rosetta stone", 4],
             5:["Who was the first democratically elected President of Russia?", "Boris Yeltsin","Joseph Stalin",  "Vladimir Putin", "August Poniatowski", 1],
             6:["Which of the following empires had no written language?", "Roman Empire", "Aztec Empire", "Tang Dynasty", "Incan Empire", 4], 
             7:["When was the first crusade called?", "1765","1095",  "917", "1117", 2],
             8:["Who kiled Julius Caesar?", "Romulus And Remus","Brutus and Cassius",  "Augustus and Antony", "Gaius Octavius and Lepidus", 2], 
             9:["What famous general was once attacked by rabbits", "Hannibal","Julius Caesar",  "Napoleon", "Patton", 3],
             10:["Who was Germany's first woman Chancellor?", "Hanna Reitsch.","Angela Merkel",  "janet Yellen", "Maria Baum", 2],
             11:["During the Summer of Love, where did hippies converge?", "Chicago","St.louis",  "New York", "San Francisco", 4],
             12:["What were the two major powers of the cold war", "China and Canada","Russia and Britain",  "United states and Russia", "United states and Vietnam", 3],}

history = open("history.pickle","wb")
pickle.dump(Questions, history)
history.close
