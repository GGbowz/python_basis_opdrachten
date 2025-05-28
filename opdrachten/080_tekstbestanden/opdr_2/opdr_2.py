# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....
# Aantal pogingen bijhouden
aantal_pogingen = 0
geraden = False

while not geraden:
    try:
        gok = int(input(prompt))
        aantal_pogingen += 1

        if gok < geheim_getal:
            print("hoger")
        elif gok > geheim_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden het is {geheim_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer gedaan")
            geraden = True
    except ValueError:
        print("Voer een geldig getal in.")
