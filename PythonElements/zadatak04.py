### Zadatak 4. Napiši program tako da izračunava realnu dobit, uzimajući u obzir i inflaciju.
### Godišnji stepen inflacije se takođe unosi sa tastature. Formula koja uključuje uticaj inflacije je sledeća:
### principal = principal / (1 + inflation)

principal = float(input("Unesite osnovni kapital: "))
inflation = float(input("Unesite godisnju inflaciju (u procentima): "))

# Pretvaranje inflacije u decimalni format
inflation /= 100

# Računanje realne dobiti
realna_dobit = principal / (1 + inflation) - principal

# Ispis rezultata
print("Realna dobit je: ", round(realna_dobit, 2))
print("Ukupan iznos ce biti: ", round(principal + realna_dobit, 2))