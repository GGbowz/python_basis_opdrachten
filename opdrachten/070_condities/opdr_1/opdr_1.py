# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
numbers = []
greater_than_four = []

for i in range(1, 11):
    numbers.append(i)

    if i > 4:
        greater_than_four.append(i)

print(greater_than_four)