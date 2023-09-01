### Zadatak 1. Napiši program tako da izračunava prosek tri ocene.

# Unos ocena
ocena1 = float(input("Unesite prvu ocenu: "))
ocena2 = float(input("Unesite drugu ocenu: "))
ocena3 = float(input("Unesite trecu ocenu: "))

# Računanje proseka
prosek = (ocena1 + ocena2 + ocena3) / 3
prosek = round(prosek, 2)

# Ispis proseka
print("Prosek ocena je:", prosek)