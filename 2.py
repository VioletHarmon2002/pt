print("Hei,Liza!")
user = input('Anna nimesi: ')
print("Terve," + user + "!")

# kerrat = int(input("Montako kertaa tervehditään: "))


kerrat = 24
tehdyt = 0
while tehdyt<kerrat:
    print("Hyvää huomenta")
    tehdyt = tehdyt + 1



#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
#niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = float(input('Anna tummat: '))

while tuumat >= 0:
    print(f'{tuumat} tuuma on {2.54 * tuumat} senttiä ')
    tuumat = float(input('Anna tummat: '))