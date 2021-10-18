time = int(input("Hány óra van most?: "))


if (time >= 8  and time <16):
    print('A bolt nyitva van')
    print('Enyni órád van még oda érni: ',(16 - time))
    
else:
    print('A bolt zárva tart!')

    if time > 16:
        print('Enyni idő van még a nyitásig: ',(32 - time))

    else:
        print('Ennyi idő van még a nyitásig' ,(8 - time))