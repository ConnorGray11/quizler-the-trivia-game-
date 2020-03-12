import pickle

Questions = {1:["What is the highest note on a baseline piano?", "B7", "C8", "G2", "A1", 2],
             2:["When was Daft Punks first album released?", "2000", "1999", "1995", "1997", 4], 
             3:["What Depeche Mode song was inspired by Priscilla Presley's book Elvis and Me?", "Strangelove", "World in my eyes", "Personal Jesus", "sweetest Perfection", 3],
             4:["What instrument do you play without touching it?", "Sitar", "Harp", "synthesizer", "theremin", 4],
             5:["How much pressure do all the strings combined within a grand piano exert on the frame?", "30 tons","300 tons",  "3 tons", "300 lbs", 1],
             6:["What is the oldest surviving musical instrument?", "Drum", "didgeridoo", "Lyre", "Flute", 4], 
             7:["Which jazz musician was known for playing a bent trumpet?", "Chet Baker","Dizzy Gillespie",  "Miles Davis", "Louis Armstrong", 2],
             8:["What note is the lowest string on a bass guitar most commonly tuned to?", "G3","F4",  "E2", "B2", 3], 
             9:[" How many different instruments did Prince play on his debut album?", "27","17",  "31", "26", 1],
             10:["What 1985 charity single sold more than 20 million copies?", "Candle in the wind","we are the world",  "Thats what friends are for", "Do they know its christmas", 2],
             11:["Who was The Number one Jazz Musican", "Billie Holiday","Nat King Cole",  "Lena Horne", "Louis Armstrong", 4],
             12:["How many tonnes of bells are in the world's largest Carillon?", "123","78",  "91", "212", 3],}

music = open("music.pickle","wb")
pickle.dump(Questions, music)
music.close
