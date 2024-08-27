import time
import os
import random

terningdb = ["Terning:", "Resultat:"]

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


console_clear()
antall_terninger = int(input("Hvor mange terninger ønsker du å trille? "))
if antall_terninger != int:
    print("Skriv et heltall")
console_clear()
print("Kaster terninger.")
time.sleep(0.5)
console_clear()
print("Kaster terninger..")
time.sleep(0.5)
console_clear()
print("Kaster terninger...")
time.sleep(0.5)
console_clear()
for i in range(1, antall_terninger):
    var = random.randint(1, 6)
    print("Terning", i, ": ", var)
    entry = [i, var]
    terningdb.append(entry)
    time.sleep(0.1)