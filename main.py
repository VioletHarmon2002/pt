import math
a = int(input("Kuinka monta kg? "))
b = int(input("Kuinka monta naulaa? "))
c = int(input("Kuinka monta luotia? "))
aa = a * 20
bc = (b * 32 / 13.3)+ (c * 13.3)

while(bc > 450):
    bc-=450
    aa+=1
print("kg yhteensä",aa, "yhteensä grammoja",math.ceil(bc))













a = int(input("enter a value "))
b = int(input("enter b value "))
c = int(input("enter c value "))

print(a+b+c)
print(a*b*c)
print((a+b+c)/3)


import math

säde = float(input('Anna ympyrän säde: '))
pintaAla = math.pi * säde * säde

print(pintaAla)

print("Hei,Liza!")
user = input('Anna nimesi: ')
print("Terve," + user + "!")









