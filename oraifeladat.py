inputList = []
inputList += [int(input("Kerek egy szamot: "))]
inputList += [int(input("Kerek meg egy szamot: "))]
inputList += [int(input("Kerek meg egy szamot: "))]
print("A legnagyobb beolvasott szam: "+str(max(inputList)))



inputList = []
inputList += [int(input("Kerek egy szamot: "))]
inputList += [int(input("Kerek meg egy szamot: "))]
inputList += [int(input("Kerek meg egy szamot: "))]
print("A legkisebb beolvasott szam: "+str(min(inputList)))



inputNumber = int(input("Kerem a pontszamot: "))

if(inputNumber < 50):
    print("Erdem jegye: 1")
elif(inputNumber >= 50 and inputNumber <60):
    print("Erdem jegye: 2")
elif(inputNumber >= 60 and inputNumber < 70):
    print("Erdem jegye: 3")
elif(inputNumber >= 70 and inputNumber <85):
    print("Erdem jegye: 4")
elif(inputNumber >= 85 and inputNumber < 100):
    print("Erdem jegye: 5")

