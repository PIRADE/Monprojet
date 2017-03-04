#yahtzee.py

import random

#test combinaison

def combinaison(choix,des):
    total=0
    nb_identique = 1
    demax=0
    scoredemax=0

    for x in range(5):
        actuel = x
        compteur = 1
        while compteur != -1:
            if actuel + 1 < 5:
                if des[actuel + 1] == des[x]:
                    actuel = actuel + 1
                    compteur = compteur + 1
                    maxdes=des[x]
                    if compteur >= nb_identique:
                        nb_identique = compteur
                        demax=maxdes
                        scoredemax=demax*nb_identique    
                else:
                    compteur = -1
            else:
                compteur = -1
        if(compteur >= nb_identique):
            print("la somme des", demax, "fait ", scoredemax)
    if (choix >0 and choix <7) :
       for x in range(5):
           if des[x] == choix:
               total=total+des[x]
    if choix == 0 :    
        total=0
        for index in range(5):
            total = total + int(des[index])
        print("la somme des 5 dés fait ",total)
    if choix==12 or choix ==0 :  
        if nb_identique == 5:
            print("vous avez un Yathzee:")
            total=50
    if ((choix>6 and choix<10) or choix ==0) :      
        if nb_identique == 4 or nb_identique == 3:
            total = 0
            for index in range(5):
                total = total + int(des[index])
            if nb_identique == 4:
                print("Vous avez un carré: " + str(total) + " points.")
            else:
                no_duplicates = []
                for index in range(5):
                    if des[index] not in no_duplicates:
                        no_duplicates.append(des[index])
                if len(no_duplicates) == 2:
                    print("Vous avez un Full.")
                    total=25
                else:
                    print("vous avez un brelan: " + str(total) + " points.")
    return total

#test suite

def suite(choix,des):
    suite = 1
    for index in range(len(des)):
        actuel = index
        compteur = 1
        while(actuel != -1):
            if actuel + 1 < len(des):
                if int(des[actuel + 1]) - int(des[actuel]) == 1:
                    actuel = actuel + 1
                    compteur = compteur + 1
                elif int(des[actuel + 1]) == int(des[actuel]):
                    actuel = actuel + 1
                else:
                    actuel = -1
            else:
                actuel = -1
            if compteur > suite:
                suite = compteur
    if (suite == 4 and choix == 10) or (suite == 4 and choix == 0):
        print("Vous avez une petite suite: 30 points.")
        return 30
    elif (suite == 5 and choix == 11) or (suite == 5 and choix == 0):
        print("Vous avez une grande suite: 40 points.")
        return 40
    else:
        return 0

#on regarde les combinaisons que l'on peut avoir

def propose(des):
    total=0
    score=0
    score = combinaison(0,des)
    score = suite(0,des)
    for index in range(5):
        total = total + int(des[index])
    print("la somme des 5 dés fait ",total)


def resultat(choix,des):
    monchoix=choix
    total=0
    score=0
    if monchoix <10 or monchoix==12:
        score = combinaison(monchoix,des)
    elif monchoix == 10 or monchoix == 11 :
        score = suite(monchoix,des)
    elif monchoix==13 :
        for index in range(5):
            total = total + int(des[index])
        print("la somme des 5 dés fait ",total)
        score=total
    return score

def affiche(tour,des):
    desaffiche=des
    x=tour
    print("lancé ",x , end =": ")
    for x in range(len(desaffiche)):
          if x < len(desaffiche) - 1:
              print(desaffiche[x], end =" ")
          else:
              print(desaffiche[x])

def tirage(des):
    des = []
    for x in range(5):
        des.append(random.randint(1,6))
    des.sort()
    for y in range(1,4):
        affiche(y,des)
        desgardes = input("quels dés voulez vous garder 1,2,3,4,5 ? ")
        desgardes = desgardes.split(',')
        for x in range(5):
            if str(x + 1) not in desgardes:
                des[x] = random.randint(1,6)
        des.sort()
        affiche(y+1,des)
        choix=input("on garde cette combinaison 0ui/Non ?")
        if (choix == 'O' or choix == 'o' or choix == 'Oui' or choix == 'OUI') :
            return des
        else :
            print(" on relance")
    return des

def affichescore(tabjoue,tabscore):
    print ("score")
    print ("[1]      total des un ", tabjoue[1]," ",tabscore[1])
    print ("[2]    total des deux ", tabjoue[2]," ",tabscore[2])
    print ("[3]   total des trois ", tabjoue[3]," ",tabscore[3])
    print ("[4]  total des quatre ", tabjoue[4]," ",tabscore[4])
    print ("[5]    total des cinq ", tabjoue[5]," ",tabscore[5])
    print ("[6]     total des six ", tabjoue[6]," ",tabscore[6])
    print ("      Total section 1 ", "   ",tabscore[1]+tabscore[2]+tabscore[3]+tabscore[4]+tabscore[5]+tabscore[6]) 
    if (tabscore[1]+tabscore[2]+tabscore[3]+tabscore[4]+tabscore[5]+tabscore[6] > 63):
        print (">63 + Bonus de 35 points  35")
        Totsection1=tabscore[1]+tabscore[2]+tabscore[3]+tabscore[4]+tabscore[5]+tabscore[6]+35
        print ("total section supérieure  ", Totsection1)
    else :
        print ("63 + Bonus de 35 points    0")
        Totsection1=tabscore[1]+tabscore[2]+tabscore[3]+tabscore[4]+tabscore[5]+tabscore[6]
        print ("total section supérieure  ", Totsection1)
    print("")
    print("[7]            Brelan ", tabjoue[7]," ",tabscore[7])
    print("[8]             Carré ", tabjoue[8]," ",tabscore[8])
    print("[9]              Full ", tabjoue[9]," ",tabscore[9])
    print("[10]     Petite Suite ", tabjoue[10]," ",tabscore[10])
    print("[11]     Grande Suite ", tabjoue[11]," ",tabscore[11])
    print("[12]          Yathzee ", tabjoue[12]," ",tabscore[12])
    print("[13]           Chance ", tabjoue[13]," ",tabscore[13])
    Totsection2 = tabscore[7]+tabscore[8]+tabscore[9]+tabscore[10]+tabscore[11]+tabscore[12]+tabscore[13]
    print("      Total section 2     ", Totsection2)
    print("         Total Général    ", Totsection1+Totsection2)
    
def main():
    tabscore=[]
    tabjoue=[]
    for i in range(14):
          tabscore.append(0)
          tabjoue.append(" ")
    affichescore(tabjoue,tabscore)
    total_score = 0
    score=0
    for x in range(1,14):
        print("Tour " + str(x) + "!")
        des = []
        des = tirage(des)
        confirme=True
        while (confirme):
            combinaison=0
            while(combinaison <1 or combinaison >13):
                propose(des)
                combinaison=int(input("Quelle combinaison retenez vous [1-13] "))

            if(tabjoue[combinaison] == 'X'):
                print("vous ne pouvez pas retenir cette combinaison, elle a déjà été prise")
            else :
                score = resultat(combinaison,des)    

                choix=input("vous confirmez que vous gardez la combinaison ?")
                if (choix == 'O' or choix == 'o' or choix == 'Oui' or choix == 'OUI') :
                    tabjoue[combinaison] = 'X'   
                    print("score=",score)
                    tabscore[combinaison]=score
                    confirme=False
        
        affichescore(tabjoue,tabscore)                
        
        total_score = total_score + score
    affichescore(tabjoue,tabscore)
    print("score: " + str(total_score) + " points.")
main()
