import time
import os
import random

fil = "terningdat.txt"
terningdb = []

gui = True

def terning1():
    print("+-------+")
    print("|       |")
    print("|   O   |")
    print("|       |")
    print("+-------+")

def terning2():
    print("+-------+")
    print("| O     |")
    print("|       |")
    print("|     O |")
    print("+-------+")

def terning3():
    print("+-------+")
    print("| O     |")
    print("|   O   |")
    print("|     O |")
    print("+-------+")

def terning4():
    print("+-------+")
    print("| O   O |")
    print("|       |")
    print("| O   O |")
    print("+-------+")

def terning5():
    print("+-------+")
    print("| O   O |")
    print("|   O   |")
    print("| O   O |")
    print("+-------+")

def terning6():
    print("+-------+")
    print("| O   O |")
    print("| O   O |")
    print("| O   O |")
    print("+-------+")

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def skriv_til_fil(filnavn):
    with open(filnavn, "w") as txt_file:
        for line in terningdb:
            txt_file.write("".join(line) + "\n")

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
for i in range(antall_terninger):
    var = random.randint(1, 6)
    if gui == True:
        if var == 1:
            terning1()
        elif var == 2:
            terning2()
        elif var == 3:
            terning3()
        elif var == 4:
            terning4()
        elif var == 5:
            terning5()
        elif var == 6:
            terning6()
    elif gui == False:
        print("Terning", i+1, ":", var)
    entry_string = "Terning " + str(i+1) + ":"
    entry = [entry_string, var]
    #this is a really bad way of doing this, will optimize
    terningdb.append(str(entry))

    #different speeds for UX
    if antall_terninger < 10:
        time.sleep(0.5)
    elif antall_terninger < 25:
        time.sleep(0.1)
    elif antall_terninger < 50:
        time.sleep(0.05)

    #<25 hyperspeed

skriv_til_fil(fil)

var = 0
for item in terningdb:
    number = int(item.split(',')[1].strip().strip("]"))
    var += number
    
avg = var/len(terningdb)
print("Gjennomsnittskast:", avg)

