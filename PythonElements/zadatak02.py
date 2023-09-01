### Zadatak 2. Napiši program tako da izračunava i ispisuje tabelu stepeni Celzijusa i Farenhajta
### za svakih 10 stepeni od 0 C do 100 C.

print("Stepeni C | Stepeni F")
print("---------------------")

for celzijus in range(0, 101, 10):
    farenhajt = celzijus * 9 / 5 + 32
    print("{:>5}     | {:>5}".format(celzijus, round(farenhajt, 2)))