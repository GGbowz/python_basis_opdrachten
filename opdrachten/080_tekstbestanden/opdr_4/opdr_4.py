# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

antwoorden = {}
labels = ["voornaam", "achternaam", "drank", "eten"]

for i, vraag in enumerate(vragen):
    antwoord = input(f"{i + 1}. {vraag}\n")
    antwoorden[labels[i]] = antwoord

print("\nBedankt voor het invullen!")
print("See you at the party.\n")

with open("party_enquete.txt", "a") as bestand:
    bestand.write("----\n")
    for sleutel, waarde in antwoorden.items():
        bestand.write(f"{sleutel}: {waarde}\n")
    bestand.write("\n")