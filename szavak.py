elso_szo = input('Adj megy egy szót: ')
masodik_szo = input('Adj meg egy másik szót: ')

szo1_hossza = len(elso_szo)
szo2_hossza = len(masodik_szo)

if ( szo1_hossza > szo2_hossza):
    print('A hosszabb szó: ' + elso_szo)

elif(szo1_hossza < szo2_hossza):
    print('A hosszabb szó: ' + masodik_szo)

else:
    print('A két szó egyen hosszú.')