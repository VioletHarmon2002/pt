# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random


secret_number = random.randint(1, 10)

print("Tervetuloa peliin! Arvaa numero väliltä 1-10.")


attempts = 0

while True:
    try:

        guess = int(input("Anna arvauksesi: "))
        attempts += 1


        if guess == secret_number:
            print(f"Oikein! Arvasit numeron {secret_number} за {attempts} попыток.")
            break
        elif guess < secret_number:
            print("Liian pieni arvaus.")
        else:
            print("Liian suuri arvaus.")
    except ValueError:
        print("Virheellinen syöte. Введите целое число в диапазоне от 1 до 10.")
