#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).


print("Sijoita oikein käyttäjätunnus ja salasana ")

kertaa = 0
tunnus = ""
passw = ""

while kertaa < 5:
    tunnus = input("Sijoita tunnus: ")
    passw = input("Sijoita salasana: ")
    if passw == "rules" and tunnus == "python":
        print("Tervetuloa")
        break
    else:
        print("Tunnus tai salasana on väärin. Yrittää uudellen. ")
        kertaa += 1

while kertaa == 5:
    print("Pääsy on evätty")
    break




Write a program that asks the user for a username and password.
If either or both are incorrect, the ID and password will be asked again.
This will continue until the login details are correct or
the incorrect information has been entered five times.
In the former case print welcome and in the latter Access Denied.
(The correct username is python and password rules).

username = 'python'
password = 'rules'
user = ''
pwd = ''
times = 0
notlogin = True
while (notlogin and times <5):
    user = input('username: ')
    pwd = input('password: ')
    times = times + 1
    if(username ==user and password ==pwd)
        notloin = False

if notlogin:
    print('Access denied')
else:
    print('Access granted')
