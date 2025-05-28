# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

verschuiving = 5

def versleutel_tekst(tekst, verschuiving):
    resultaat = ""
    for teken in tekst:
        if teken.isalpha():
            basis = ord('A') if teken.isupper() else ord('a')
            nieuw_teken = chr((ord(teken) - basis + verschuiving) % 26 + basis)
            resultaat += nieuw_teken
        else:
            resultaat += teken
    return resultaat

originele_tekst = input("Geef de tekst die je wilt encrypten:\n")
versleuteld = versleutel_tekst(originele_tekst, verschuiving)

print("\nVersleutelde tekst:")
print(versleuteld)

with open("versleutelde_tekst.txt", "w") as bestand:
    bestand.write(versleuteld)

