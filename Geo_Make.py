import pickle

Questions = {1:["What country has the most natural lakes?", "United States", "Canada", "Brazil", "India", 2],
             2:["What is the driest place on Earth?", "Egypt", "Libya", "Saraha Desert", "Antarctica", 4], 
             3:["Which African nation has the most pyramids?", "Algeria", "Nigeria", "Sudan", "Egypt", 3],
             4:["What is the oldest city in the world?", "Athens", "Jerusalem", "Jericho", "Damascus", 4],
             5:["Which U.S. state has the most active volcanoes?", "Alaska", "California", "Hawaii", "Florida", 1],
             6:["Which country has the most coastline?", "Russia", "Australia", "United States", "Canada", 4], 
             7:["What is the capital of Australia?", "Perth", "Canberra", "Melbourne", "Sydney", 2],
             8:["What U.S. state shares borders with Louisiana, Arkansas, Oklahoma, and New Mexico?", "Missouri", "Wyoming", "Texas", "Colorado", 3], 
             9:["Which continent has land in all four hemispheres?", "Africa", "Asia", "North America", "South America", 1],
             10:["What mountain is closest to the moon?", "Mount Pandim", "Mount CHimborazo", "Mount Rushmore", "Mount Everest", 2],
             11:["What is the largest city in the world based on surface area?", "Mexico City", "Tokyo", "New York City", "Hulunbuir", 4],
             12:["Which Hawaiian island is unhinhabited?", "Coconut Island", "Molokai", "Kaho'olawe", "Niihau", 3],}

geography = open("geo.pickle","wb")
pickle.dump(Questions, geography)
geography.close