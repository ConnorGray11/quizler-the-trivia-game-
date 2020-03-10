import pickle

games = {1:['FPS','Halo 3','Bungie','Microsoft','Xbox','2007','10','either','30.00','yes','1/15/2008','good game yee'],
2:['RTS','Halo Wars','Bungie','Microsoft','Xbox','2009','10','either','20.00','yes','6/20/2009','loved the art style']}

data_file = open("game_lib.pickle","wb")
pickle.dump(games, data_file)
data_file.close

