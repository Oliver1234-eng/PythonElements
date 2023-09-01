### Zadatak 3. Napiši program za konverziju iz Farenhajta u Celzijuse.

farenhajt = float(input("Unesite temperaturu u Farenhajtima: "))

celzijus = (farenhajt - 32) * 5 / 9

print("{:.2f} stepeni Farenhajta = {:.2f} stepeni Celzijusa".format(farenhajt, celzijus))