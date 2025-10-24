import random

print("Random name generator for eveyone in CSE class ")

firstnames = ["Asher", "Nate", "Caspian", "Shaan", "Alexander", "Nayoki", "Seth", "David","Rayan","Colin","Maddox","Dennis", "Evan","Blake"]
lastnames = ["Ader", "Chao", " Farman-Farmaian", "Glazer", "Graves", "Izumi", "leberman", "Lozado", "Mohammadinia", " Poirier","Prata", "Riley","Sherman-Chan", "Slobodsky"]

def generatename():
    first = random.choice(firstnames)
    last = random.choice(lastnames)
    return f"{first} {last}"
#printed code
for i in range(1):
    print(generatename())