import pickle

scores = (0)

data_file = open("score.pickle","wb")
pickle.dump(scores,data_file )
data_file.close
