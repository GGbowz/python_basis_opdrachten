# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
gasten = ["Yerke", "Paul", "Kees", "Marie", "Hilda"]

gasten.remove("Marie")
print(gasten)

index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, "George")
print(gasten)