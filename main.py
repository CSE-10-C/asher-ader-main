
#in order for me to make this code random i had to import randomness cuz randomness isn't built into computors

import random

#the kind of "title" to the code
print("1 Random name generator for eveyone in our CSE class ")

#the list of first and last names that could randomly be chosen
randomfirst = ["Asher", "Nate", "Caspian", "Shaan", "Alexander", "Naoki", "Seth", "David","Rayan","Colin","Maddox","Dennis", "Evan","Blake"]
randomlast = ["Ader", "Chao", " Farman-Farmaian", "Glazer", "Graves", "Izumi", "leberman", "Lozado", "Mohammadinia", " Poirier","Prata", "Riley","Sherman-Chan", "Slobodsky"]

#making a variable for first and last with and random first and last name from the list
#"random.choice" pics a name from the list 
first = random.choice(randomfirst)
last = random.choice(randomlast)

#printing the random name out
print(first,last)