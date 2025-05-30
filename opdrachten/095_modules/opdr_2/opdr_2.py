# Opdracht 1 functies
# Naam student:
# Groep:

# my_modules/csv_mod.py

# opdr_1.py

from my_modules import csv  # importeer je eigen module

# Lees de CSV-data in
personen = csv.lees_csv("C:/Users/yerke/Documents/Deltion/Python_opdrachten/python_basis_opdrachten/opdrachten/095_modules/opdr_2/data.csv")

# Filter op voornaam die begint met "ja"
print("Filter: voornaam begint met 'ja'")
resultaat = csv.filter(personen, "voornaam", "ja")
for p in resultaat:
    print(f"{p['voornaam']} {p['tussenvoegsel']} {p['achternaam']}".strip())

# Filter op voornaam die begint met "Pie"
print("\nFilter: voornaam begint met 'Pie'")
resultaat = csv.filter(personen, "voornaam", "Pie")
for p in resultaat:
    print(f"{p['voornaam']} {p['tussenvoegsel']} {p['achternaam']}".strip())

# Filter op plaats die begint met "d"
print("\nFilter: plaats begint met 'd'")
resultaat = csv.filter(personen, "plaats", "d")
for p in resultaat:
    print(f"{p['voornaam']} {p['tussenvoegsel']} {p['achternaam']}".strip())