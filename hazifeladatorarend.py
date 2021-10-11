mondayList = ["Töri", "Ikt", "Ikt", "Magyar", "Angol", "Matek"]
tuesdayList = ["Fizika", "Ofő", "Angol", "Töri", "Magyar", "Magyar"]
wednesdayList = ["asd"]
thirsdayList = ["dsa"]
fridayList = ["sda"]

inputLetter = str(input("Kerem a napot: "))

if(inputLetter[0].lower() == 'h'):
    print("Hetfoi program:")
    print(*mondayList, sep=", ")
elif(inputLetter[0].lower() == 'k'):
    print("Keddi program:")
    print(*tuesdayList, sep=", ")
elif(inputLetter[0].lower() == 's'):
    print("Szerdai program:")
    print(*wednesdayList, sep=", ")
elif(inputLetter[0].lower() == 'c'):
    print("Csütörtöki program:")
    print(*thirsdayList, sep=", ")
elif(inputLetter[0].lower() == 'p'):
    print("Pénteki program:")
    print(*fridayList, sep=", ")
else:
    print("Hibas bemenet")