import time
import random
import os
import sys

from time import sleep

jhonny_name = "a"
jhonny_level = 1
jhonny_hp = 10
jhonny_dmg = 1
jhonny_xp = 0
jhonny_ase = 0 #muutos
jhonny_heit=0 #muutos
jhonny_taik=0 #muutos
level = 1
hp = 5
dmg = 1
xp = 10


def croac(lv,lama,kokemus):
    jhonny_level = lv
    jhonny_dmg = lama
    jhonny_xp = kokemus

def croac_elama(elama,hups):
    jhonny_hp = elama - hups

    if jhonny_hp <= 0:
        print("Olit kuvottava sammakon niljake ilman tulevaisuutta etkä oikea Johnnyn perillinen")


def genericEnemy(elama,lama,xp):
    hp = elama
    dmg = lama
    xp = xp

def piirra(nimi):
    
    kuva = open(os.path.join(sys.path[0], nimi), "r", encoding="utf-8")
    for x in kuva:
        print(x.rstrip())
    kuva.close()

def fight(JDMG,EDMG,JHP,EHP,RNG):

    taistelutilanne = 1
    while taistelutilanne == 1:
        status = 1
        while status == 1:
            print("Paina 1 hyökätäksesi, 2 paetaksesi")
            x = input()
            if x == "1":
                print("Kohdistat vihasi agressiivisiin ajatuksiin")
                break
            if x=="2":
                print("Pakenit")
                return JHP
                
            else:
                print("Syötä 1 tai 2, älä vittuile")

       # if status == 2:   #mahdollistaa pakenemisen
         #   break     

        taistelu = 1
        while taistelu == 1:
            print(" 1. Lyö \n 2. heitä esineellä \n 3. vuorovaikuta")
            x = input()
            if x == "1":
                print("Löit mörköä")
                EHP=EHP-JDMG    #Johnnyn lyönti ja hpmuutos
                JHP=JHP-EDMG    #Vihun lyönti ja hpmuuots
                if EHP<1 and JHP>1:
                    print ("Kalman vihreät kätesi ovat löytäneet uuden uhrinsa")
                    taistelutilanne = 2
                    taistelu = 2
                    return JHP
                    
                    
                if EHP>1 and JHP<1:
                    print ("Nöyrryt vahvempasi edessä\n")
                    print ("Olit vain pieni sammakon paska vailla tulevaisuutta")
                    taistelutilanne = 2
                    taistelu = 2
                    return JHP
                break
                    

            if x=="2":
                print("Heität esineellä TODO")
                EHP=EHP-RNG
                if EHP<1:
                    print("Heitetty tavarasi on kohtalokas vastustajalle")
                    taistelutilanne = 2
                    taistelu = 2
                break
                    

            if x=="3":
                print("Vuorovaikutat")
                taistelu = 2
            
            elif x!="1" or x!="2" or x!="3":
                print("Syötä numero, älä vittuile")

def happitilanne(nykynen,alkuperainen):
    prosentti=nykynen/alkuperainen
    if prosentti<0.10 and prosentti>0:
        print("Olet kuoleman partaalla\n")
        print("Kuoleman portit kutsuvat huumaavasti")
    if prosentti<0.40 and prosentti>0.11:
        print("Olet verinen ja haiset")
    if prosentti<0.80 and prosentti>0.41:
        print("Olet lähes havoittumaton")
    if prosentti<100 and prosentti>0.81:
        print("Ilman maitoa")
    
    
def lootgeneraattori(): #tämä
    print("Tutkailessasi ruumista tarkemmin löydät sieltä....\n")
    x=random.randrange(1,101,1)
    if x>=1 and x<=20:
        print("mahdollisesti ulostetta\n")
        print("kätesi tahriintuvat")
    if x>=21 and x<=30:
        piirra("paska.txt")
        print("mustaa paskaa\n")
        print("jotenkin sitä joutui vielä suuhunkin")
    if x>=31 and x<=35:
        print("tyhjää\n")
    if x>=36 and x>=51:
        print("kiven\n")
        print("Haluatko sen mukaan? K\E")
        v=input("")
        if v=="K" or v=="k":
            jhonny_heit="kivi"
            print("Poimit sen mukaasi")
            return jhonny_heit
        if v=="E" or v=="e":
            print("Hylkäät esineen")
    if x>=52 and x<=65:
        print("kepin\n")
        print("Haluatko sen mukaan? K\E")
        v=input("")
        if v=="K"or v=="k":
            jhonny_ase="keppi"
            print("Poimit sen mukaasi")
            return jhonny_ase
        if v=="E" or v=="e":
            print("Hylkäät esineen")
    if x>=66 and x<=75:
        print("lasin palanen\n")
        print("Haluatko sen mukaan? K\E")
        v=input("")
        if v=="K" or v=="k":
            jhonny_ase="lasin palanen"
            print("Poimit sen mukaasi")
            return jhonny_ase
        if v=="E" or v=="e":
            print("Hylkäät esineen")
    if x>=76 and x<=86:
        print("hiekkaa\n ")
        v=input("")
        if v=="K" or v=="k":
            jhonny_heit="hiekkaa"
            print("Poimit sen mukaasi")
            return jhonny_heit
        if v=="E" or v=="e":
            print("Hylkäät esineen")
    if x>=87 and x<=91:
        print("ruosteisen miekan\n ")
        print("Haluatko sen mukaan? K\E")
        v=input("")
        if v=="K" or v=="k":
            jhonny_ase="ruosteinen miekka"
            print("Poimit sen mukaasi")
            return jhonny_ase
        if v=="E" or v=="e":
            print("Hylkäät esineen")
    if x>=92 and x<=95:
         print("ruosteisen kirveen\n ")
         print("Haluatko sen mukaan? K\E")
         v=input("")
         if v=="K" or v=="k":
            jhonny_ase="ruosteinen_kirves"
            print("Poimit sen mukaasi")
            return jhonny_ase
         if v=="E" or v=="e":
            print("Hylkäät esineen")
    if x>=96 and x<=98:
         print("amuletin \n")
         print("Haluatko sen mukaan? K\E")
         v=input("")
         if v=="K" or v=="k":
            jhonny_taik="amuletti"
            print("Poimit sen mukaasi")
            return jhonny_taik
         if v=="E" or v=="e":
            print("Hylkäät esineen")
        
    if x>=99 and x<=100:
         print("murderhobo maximaattus miekan\n ")
         print("Haluatko sen mukaan? K\E")
         v=input("")
         if v=="K" or v=="k":
            jhonny_ase="murderhobo_maximaattus_miekka"
            print("Poimit sen mukaasi")
            return jhonny_ase
         if v=="E" or v=="e":
            print("Hylkäät esineen")
    

print("\nHuomaat kuinka pyrstösi surkastuu. Et ole enää nuijapää, vaan kehittyvä sammakko vailla tarkoitusta. \n"  )
#sleep(3.5)
print("Kuulet pienen äänen päässäsi \n")
#sleep(3.5)
print(" 'Jos luulet olevasi todellinen Johnny Croacin perillinen on sinun todistettava arvosi' \n")
#sleep(3.5)
print(" 'Etsi minut' \n")
#sleep(5.5)

print("Syötä nimesi")
jhonny_name = input()
print("Nimi: " + jhonny_name + "\n Taso: " + str(jhonny_level) + "\n Elämäpisteet: " + str(jhonny_hp)+ "\n Voimakkuus: " + str(jhonny_dmg) + "\n Kokemuspisteet: " + str(jhonny_xp) )

#sleep(6)
print("\n")
print("░░░░░░░░░░████░░░░░░██████░░░░░░░░░░░░░░")
print("░░░░░░░░░░█░░░███████░░░░██░░░░░░░░░░░░░")
print("░░░░░░░░███░█░░░░░░░░░█░░░░██░░░░░░░░░░░")
print("░░░░░░░██░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░")
print("░░░░░░██░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░")
print("░░░░░░█░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░")
print("░░░░░░█░░██░░░░░░░░░░░█░░░░░░░█░░░░░░░░░")
print("░░░░░░█░░░██░░░░░░░░███░░░░░░██░░░░░░░░░")
print("░░░░░░█░░░░██████████░░░░░░░░█░░░░░░░░░░")
print("░░░░░░█░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░")
print("░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░")
print("░░░░░░░███░░░░░░░░░░░░░░███░░░░░░░░░░░░░")
print("░░░░░░░░░██░░░░░░░░░░░███░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░░███░░░██░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░░████░░░███░░░░░░░░░░░░░░░░░░")
print("░░░░░░░░░░░█████░░░████░░░░░░░░░░░░░░░░░")
print("Olet valmis aloittamaan matkasi")

#sleep(6)

print("\n")
print("Uiskennellessasi huomaat ettet ole yksin\n")
#sleep(3.5)
print("Uhkaava hahmo silmäkulmassasi vaikuttaa vihamieliseltä")
#sleep(3.5)

piirra("kivi.txt")
hp_tilanne = fight(1,1,10,4,0.5)

print(str(hp_tilanne) + " hp jäljellä")
happitilanne(hp_tilanne,jhonny_hp)
lootgeneraattori()

#piirra("kynttila.txt")
