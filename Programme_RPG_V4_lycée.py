#KELLER Guillaume 28/11/15 Premier_essai_RPG_V8.py
# ____________________________________________________
#
#Date de modification : 28/11/15 -> Rédaction
# ____________________________________________________
#
#Date de modification : 01/12/15 -> Mise au clair du code, remplacement des valeurs par variables
#                                                   largeur,hauteur,taille_carrée
# ____________________________________________________
#
#Date de modification : 05/12/15 -> Ajout seconde carte, code des fonctions servant à changer de 
#                                                   carte, "zones interdites" sur carte 2
# ____________________________________________________
#
#Date de modification : 05/12/15 -> Hitbox de la carte 2 éclaircies / définition de celles-ci en fonction
# ____________________________________________________
#
#Date de modification : 06/12/15 -> Ajout d'une troisième carte : Carte1_10
#                                                   +Hitbox
# ____________________________________________________
#
#Date de modification : 07-12/12/15 ->Définition de l'interface combat
# ____________________________________________________
#
#Date de modification : 15-16/12/15 ->Association du programme avec les cartes et celui de l'interface de combat
# ____________________________________________________
#
#Date de modification : 16/12/15 ->Ajustement des fonctions de page d'accueil / carte / combat
# ____________________________________________________

from tkinter import  *
from random import *
from time import time, sleep
fen=Tk()
fen.configure(bg="White")
fen.title="Premier essai RPG"


taille_carrée=int(32)
nbr_carré_x=42
nbr_carré_y=16
largeur=nbr_carré_x*taille_carrée
hauteur=nbr_carré_y*taille_carrée
#coords=(0*taille_carrée,16*taille_carrée)
coords=(22*taille_carrée,11*taille_carrée)
Choix="Draco"
#coordscarte=(0,0)
coordscarte=(1,0)
droite=StringVar()
gauche=StringVar()
bas=StringVar()
haut=StringVar()
compteur_mouvement=0
compteur_mouvement2=0
#date=randint(20,100)
date=3
print("date =",date)
Event=False

init=0
compteur_attaque_me=-1
compteur_attaque_vs=-1
Progression_Dégat_me=('Dégat_', 0)
Progression_Dégat_vs=('Dégat_', 0)
Choix_attaque_me=0
init_evenement=0
init_Dégat=0


DracoVue_dos=PhotoImage(file="DracoVue_dos.gif")
DracoVue_dos2=PhotoImage(file="DracoVue_dos2.gif")
DracoVue_face=PhotoImage(file="DracoVue_face.gif")
DracoVue_face2=PhotoImage(file="DracoVue_face2.gif")
DracoVue_droite=PhotoImage(file="DracoVue_droite.gif")
DracoVue_droite2=PhotoImage(file="DracoVue_droite2.gif")
DracoVue_gauche=PhotoImage(file="DracoVue_gauche.gif")
DracoVue_gauche2=PhotoImage(file="DracoVue_gauche2.gif")

CaninosVue_dos=PhotoImage(file="CaninosVue_dos.gif")
CaninosVue_dos2=PhotoImage(file="CaninosVue_dos2.gif")
CaninosVue_face=PhotoImage(file="CaninosVue_face.gif")
CaninosVue_face2=PhotoImage(file="CaninosVue_face2.gif")
CaninosVue_droite=PhotoImage(file="CaninosVue_droite.gif")
CaninosVue_droite2=PhotoImage(file="CaninosVue_droite2.gif")
CaninosVue_gauche=PhotoImage(file="CaninosVue_gauche.gif")
CaninosVue_gauche2=PhotoImage(file="CaninosVue_gauche2.gif")

PikachuVue_dos=PhotoImage(file="PikachuVue_dos.gif")
PikachuVue_dos2=PhotoImage(file="PikachuVue_dos2.gif")
PikachuVue_face=PhotoImage(file="PikachuVue_face.gif")
PikachuVue_face2=PhotoImage(file="PikachuVue_face2.gif")
PikachuVue_droite=PhotoImage(file="PikachuVue_droite.gif")
PikachuVue_droite2=PhotoImage(file="PikachuVue_droite2.gif")
PikachuVue_gauche=PhotoImage(file="PikachuVue_gauche.gif")
PikachuVue_gauche2=PhotoImage(file="PikachuVue_gauche2.gif")

BulbizarreVue_dos=PhotoImage(file="BulbizarreVue_dos.gif")
BulbizarreVue_dos2=PhotoImage(file="BulbizarreVue_dos2.gif")
BulbizarreVue_face=PhotoImage(file="BulbizarreVue_face.gif")
BulbizarreVue_face2=PhotoImage(file="BulbizarreVue_face2.gif")
BulbizarreVue_droite=PhotoImage(file="BulbizarreVue_droite.gif")
BulbizarreVue_droite2=PhotoImage(file="BulbizarreVue_droite2.gif")
BulbizarreVue_gauche=PhotoImage(file="BulbizarreVue_gauche.gif")
BulbizarreVue_gauche2=PhotoImage(file="BulbizarreVue_gauche2.gif")

Boutton_Draco=PhotoImage(file="Boutton_Draco.gif")
Boutton_Caninos=PhotoImage(file="Boutton_Caninos.gif")
Boutton_Pikachu=PhotoImage(file="Boutton_Pikachu.gif")
Boutton_Bulbizarre=PhotoImage(file="Boutton_Bulbizarre.gif")

Carte0_0=PhotoImage(file="Carte0_0.gif")
Carte1_0=PhotoImage(file="Carte1_0.gif")
Carte1_10=PhotoImage(file="Carte1_10.gif")

Bulbizarre_dos=PhotoImage(file="Bulbizarre_dos.gif")
Rattata_face=PhotoImage(file="Rattata_face.gif")
Bulbizarre_dos=PhotoImage(file="Bulbizarre_dos.gif")
Draco_dos=PhotoImage(file="Draco_dos.gif")
Pikachu_dos=PhotoImage(file="Pikachu_dos.gif")
Caninos_dos=PhotoImage(file="Caninos_dos.gif")

Dégat_0=PhotoImage(file="Dégat_0.gif")
Dégat_1=PhotoImage(file="Dégat_1.gif")
Dégat_2=PhotoImage(file="Dégat_2.gif")
Dégat_3=PhotoImage(file="Dégat_3.gif")
Dégat_4=PhotoImage(file="Dégat_4.gif")
Dégat_5=PhotoImage(file="Dégat_5.gif")
Dégat_6=PhotoImage(file="Dégat_6.gif")
Carte_Combat=PhotoImage(file="Carte_Combat.gif")

coordsfleche=(24*taille_carrée,13*taille_carrée)

Page_Accueil=True
fonte="Walkway Oblique SemiBold"

Bulbizarre_face=PhotoImage(file="Bulbizarre_face.gif")
Pikachu_face=PhotoImage(file="Pikachu_face.gif")
Caninos_face=PhotoImage(file="Caninos_face.gif")
Draco_face=PhotoImage(file="Draco_face.gif")
Accueil=PhotoImage(file="Page_accueil.gif")
init_Accueil=0

coordsfleche=(3*taille_carrée,7*taille_carrée)


def changement_carte(coordonnéescarte):
    chaine=str(coordonnéescarte)
    liste=[]
    for i in range (len(chaine)):
        liste.insert(i,chaine[i])
    liste.remove("(")
    liste.remove(")")
    liste.remove(",")
    chaine=""
    for i in range (len(liste)):
        if liste[i]==" ":
            liste[i]="_"
    for i in range (len(liste)):
        chaine+=liste[i]
    return chaine

def limite_carte0_0():
    if ((coords[0]>27*taille_carrée) and (coords[1]<3*taille_carrée)) or \
       ((coords[0]>17*taille_carrée and coords[0]<24*taille_carrée) and (coords[1]>3*taille_carrée and coords[1]<6*taille_carrée)) or \
       (coords[1]<1*taille_carrée) or \
       (coords[1]>16*taille_carrée) or \
       (coords[0]<0*taille_carrée) or \
       ((coords[0]>32*taille_carrée) and (coords[1]>4*taille_carrée and coords[1]<7*taille_carrée)):
        return True
    else:
        return False

def limite_carte1_0():
    if ((coords[0]<1*taille_carrée) and (coords[1]>4*taille_carrée and coords[1]<7*taille_carrée)) or \
       ((coords[0]<1*taille_carrée) and (coords[1]<3*taille_carrée)) or \
       ((coords[0]>0*taille_carrée and coords[0]<2*taille_carrée) and (coords[1]<7*taille_carrée)) or \
       ((coords[0]>6*taille_carrée and coords[0]<12*taille_carrée) and (coords[1]>2*taille_carrée and coords[1]<6*taille_carrée)) or \
       ((coords[0]>6*taille_carrée and coords[0]<8*taille_carrée) and (coords[1]<3*taille_carrée)) or \
       ((coords[0]>2*taille_carrée and coords[0]<7*taille_carrée) and (coords[1]>12*taille_carrée and coords[1]<15*taille_carrée)) or \
       ((coords[0]>9*taille_carrée and coords[0]<11*taille_carrée) and (coords[1]>7*taille_carrée and coords[1]<9*taille_carrée)) or \
       ((coords[0]>12*taille_carrée and coords[0]<18*taille_carrée) and (coords[1]>2*taille_carrée and coords[1]<6*taille_carrée)) or \
       ((coords[0]>17*taille_carrée and coords[0]<22*taille_carrée) and (coords[1]>5*taille_carrée and coords[1]<9*taille_carrée)) or \
       ((coords[0]>21*taille_carrée and coords[0]<23*taille_carrée) and (coords[1]>5*taille_carrée and coords[1]<7*taille_carrée)) or \
       ((coords[0]>22*taille_carrée and coords[0]<25*taille_carrée) and (coords[1]>5*taille_carrée and coords[1]<9*taille_carrée)) or \
       ((coords[0]>27*taille_carrée and coords[0]<35*taille_carrée) and (coords[1]>5*taille_carrée and coords[1]<9*taille_carrée)) or \
       ((coords[0]>27*taille_carrée and coords[0]<29*taille_carrée) and (coords[1]<2*taille_carrée)) or \
       ((coords[0]>23*taille_carrée and coords[0]<25*taille_carrée) and (coords[1]<2*taille_carrée)) or \
       ((coords[0]>27*taille_carrée and coords[0]<29*taille_carrée) and (coords[1]>3*taille_carrée and coords[1]<6*taille_carrée)) or \
       ((coords[0]>23*taille_carrée and coords[0]<25*taille_carrée) and (coords[1]>3*taille_carrée and coords[1]<6*taille_carrée)) or \
       ((coords[0]>17*taille_carrée and coords[0]<22*taille_carrée) and (coords[1]>8*taille_carrée and coords[1]<10*taille_carrée)) or \
       (coords[1]<1*taille_carrée) or \
       (coords[1]>16*taille_carrée) or \
       (coords[0]>41*taille_carrée) or \
       ((coords[0]>33*taille_carrée) and (coords[1]>2*taille_carrée and coords[1]<6*taille_carrée)):
        return True
    else:
        return False


def limite_Carte1_10():
    if ((coords[0]<2*taille_carrée) and (coords[1]>3*taille_carrée and coords[1]<6*taille_carrée)) or \
       ((coords[0]>1*taille_carrée and coords[0]<3*taille_carrée) and (coords[1]>5*taille_carrée and coords[1]<7*taille_carrée)) or \
       ((coords[0]>1*taille_carrée and coords[0]<8*taille_carrée) and (coords[1]>4*taille_carrée and coords[1]<6*taille_carrée)) or \
       ((coords[0]>5*taille_carrée and coords[0]<7*taille_carrée) and (coords[1]>5*taille_carrée and coords[1]<7*taille_carrée)) or \
       ((coords[0]>7*taille_carrée and coords[0]<11*taille_carrée) and (coords[1]>5*taille_carrée and coords[1]<7*taille_carrée)) or \
       ((coords[0]>9*taille_carrée and coords[0]<22*taille_carrée) and (coords[1]>6*taille_carrée and coords[1]<8*taille_carrée)) or \
       ((coords[0]>20*taille_carrée and coords[0]<23*taille_carrée) and (coords[1]>7*taille_carrée and coords[1]<9*taille_carrée)) or \
       ((coords[0]>21*taille_carrée and coords[0]<24*taille_carrée) and (coords[1]>8*taille_carrée and coords[1]<10*taille_carrée)) or \
       ((coords[0]>22*taille_carrée and coords[0]<25*taille_carrée) and (coords[1]>9*taille_carrée and coords[1]<11*taille_carrée)) or \
       ((coords[0]>24*taille_carrée and coords[0]<26*taille_carrée) and (coords[1]>9*taille_carrée)) or \
       ((coords[0]<6*taille_carrée) and (coords[1]>8*taille_carrée and coords[1]<10*taille_carrée)) or \
       ((coords[0]>4*taille_carrée and coords[0]<7*taille_carrée) and (coords[1]>9*taille_carrée and coords[1]<11*taille_carrée)) or \
       ((coords[0]>6*taille_carrée and coords[0]<8*taille_carrée) and (coords[1]>10*taille_carrée)) or \
       ((coords[0]>12*taille_carrée and coords[0]<14*taille_carrée) and (coords[1]>7*taille_carrée and coords[1]<9*taille_carrée)) or \
       (coords[0]<0*taille_carrée) or \
       ((coords[0]>0*taille_carrée and coords[0]<22*taille_carrée) and (coords[1]>16*taille_carrée)) or \
       ((coords[0]>22*taille_carrée) and (coords[1]>16*taille_carrée)):
        return True
    else:
        return False

def Affichage_perso(coté):
    global Choix,perso
        
    if Choix=="Draco":
        if coté==haut:
            coté=DracoVue_dos
            coté2=DracoVue_dos2
        elif coté==bas:
            coté=DracoVue_face
            coté2=DracoVue_face2
        elif coté==gauche:
            coté=DracoVue_gauche
            coté2=DracoVue_gauche2
        elif coté==droite:
            coté=DracoVue_droite
            coté2=DracoVue_droite2

        Canevas.delete(perso)
        
        if (coords[0]%4==0 or coords[0]%4==1) and (coté==DracoVue_droite or coté==DracoVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[0]%4==2 or coords[0]%4==3) and (coté==DracoVue_droite or coté==DracoVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)
        if (coords[1]%4==0 or coords[1]%4==1) and (coté==DracoVue_face or coté==DracoVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[1]%4==2 or coords[1]%4==3) and (coté==DracoVue_face or coté==DracoVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)

#        sleep(0.01)
        

            
    elif Choix=="Caninos":
        if coté==haut:
            coté=CaninosVue_dos
            coté2=CaninosVue_dos2
        elif coté==bas:
            coté=CaninosVue_face
            coté2=CaninosVue_face2
        elif coté==gauche:
            coté=CaninosVue_gauche
            coté2=CaninosVue_gauche2
        elif coté==droite:
            coté=CaninosVue_droite
            coté2=CaninosVue_droite2

        Canevas.delete(perso)
        
        if (coords[0]%4==0 or coords[0]%4==1) and (coté==CaninosVue_droite or coté==CaninosVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[0]%4==2 or coords[0]%4==3) and (coté==CaninosVue_droite or coté==CaninosVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)
        if (coords[1]%4==0 or coords[1]%4==1) and (coté==CaninosVue_face or coté==CaninosVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[1]%4==2 or coords[1]%4==3) and (coté==CaninosVue_face or coté==CaninosVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)
            
#        sleep(0.01)


            
    elif Choix=="Pikachu":
        if coté==haut:
            coté=PikachuVue_dos
            coté2=PikachuVue_dos2
        elif coté==bas:
            coté=PikachuVue_face
            coté2=PikachuVue_face2
        elif coté==gauche:
            coté=PikachuVue_gauche
            coté2=PikachuVue_gauche2
        elif coté==droite:
            coté=PikachuVue_droite
            coté2=PikachuVue_droite2

        Canevas.delete(perso)
        
        if (coords[0]%4==0 or coords[0]%4==1) and (coté==PikachuVue_droite or coté==PikachuVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[0]%4==2 or coords[0]%4==3) and (coté==PikachuVue_droite or coté==PikachuVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)
        if (coords[1]%4==0 or coords[1]%4==1) and (coté==PikachuVue_face or coté==PikachuVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[1]%4==2 or coords[1]%4==3) and (coté==PikachuVue_face or coté==PikachuVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)
            
#        sleep(0.01)



    elif Choix=="Bulbizarre":
        if coté==haut:
            coté=BulbizarreVue_dos
            coté2=BulbizarreVue_dos2
        elif coté==bas:
            coté=BulbizarreVue_face
            coté2=BulbizarreVue_face2
        elif coté==gauche:
            coté=BulbizarreVue_gauche
            coté2=BulbizarreVue_gauche2
        elif coté==droite:
            coté=BulbizarreVue_droite
            coté2=BulbizarreVue_droite2

        Canevas.delete(perso)
        
        if (coords[0]%4==0 or coords[0]%4==1) and (coté==BulbizarreVue_droite or coté==BulbizarreVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[0]%4==2 or coords[0]%4==3) and (coté==BulbizarreVue_droite or coté==BulbizarreVue_gauche):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)
        if (coords[1]%4==0 or coords[1]%4==1) and (coté==BulbizarreVue_face or coté==BulbizarreVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté)
        elif (coords[1]%4==2 or coords[1]%4==3) and (coté==BulbizarreVue_face or coté==BulbizarreVue_dos):
            perso=Canevas.create_image(coords,anchor=SW,image=coté2)
            
    sleep(0.01)

def Anim_bas():
    global coords,perso,taille_carrée,Choix,coordscarte,FondCarte,FondCarte2,compteur_mouvement
    if Page_Accueil==False:
        compteur_mouvement+=1
        coords=(coords[0],coords[1]+(taille_carrée/taille_carrée))
        Canevas.delete(perso)
        Affichage_perso(bas)
#        sleep(0.01)

        if FondCarte=="Carte0_0":
            if limite_carte0_0()==True:
                coords=(coords[0],coords[1]-(taille_carrée/taille_carrée))

        if FondCarte=="Carte1_0":
            if limite_carte1_0()==True:
                coords=(coords[0],coords[1]-(taille_carrée/taille_carrée))

        if FondCarte=="Carte1_10":
            if limite_Carte1_10()==True:
                coords=(coords[0],coords[1]-(taille_carrée/taille_carrée))
            if (coords[0]>21*taille_carrée and coords[0]<23*taille_carrée) and (coords[1]>17*taille_carrée):
                coords=(coords[0],9*taille_carrée)
                coordscarte=(coordscarte[0],coordscarte[1]-10)
                FondCarte=("Carte"+str(changement_carte(coordscarte)))
                if FondCarte=="Carte1_0":
                    FondCarte2=Carte1_0
                    item = Canevas.create_image(0,0,anchor=NW, image=FondCarte2)
                    Affichage_perso(bas)


def Anim_haut():
    global coords,perso,taille_carrée,Choix,coordscarte,FondCarte,FondCarte2,compteur_mouvement
    if Page_Accueil==False:
        compteur_mouvement+=1
        coords=(coords[0],coords[1]-(taille_carrée/taille_carrée))
        Canevas.delete(perso)
        Affichage_perso(haut)
#    sleep(0.01)

        if FondCarte=="Carte0_0":
            if limite_carte0_0()==True:
                coords=(coords[0],coords[1]+(taille_carrée/taille_carrée))

        if FondCarte=="Carte1_0":
            if limite_carte1_0()==True:
                coords=(coords[0],coords[1]+(taille_carrée/taille_carrée))

            if (coords[0]>21*taille_carrée and coords[0]<23*taille_carrée) and (coords[1]>7*taille_carrée and coords[1]<9*taille_carrée):
                coords=(coords[0],16*taille_carrée)
                coordscarte=(coordscarte[0],coordscarte[1]+10)
                FondCarte=("Carte"+str(changement_carte(coordscarte)))
                if FondCarte=="Carte1_10":
                    FondCarte2=Carte1_10
                    item = Canevas.create_image(0,0,anchor=NW, image=FondCarte2)
                    Affichage_perso(haut)
            

        if FondCarte=="Carte1_10":
            if limite_Carte1_10()==True:
                coords=(coords[0],coords[1]+(taille_carrée/taille_carrée))



def Anim_gauche():
    global coords,perso,taille_carrée,Choix,coordscarte,FondCarte,FondCarte2,compteur_mouvement
    if Page_Accueil==False:
        compteur_mouvement+=1
        coords=(coords[0]-(taille_carrée/taille_carrée),coords[1])
        Canevas.delete(perso)
        Affichage_perso(gauche)
    
        if FondCarte=="Carte0_0":
            if limite_carte0_0()==True:
                coords=(coords[0]+(taille_carrée/taille_carrée),coords[1])

        if FondCarte=="Carte1_0":
            if limite_carte1_0()==True:
                coords=(coords[0]+(taille_carrée/taille_carrée),coords[1])

            if (coords[0]<0*taille_carrée) and ((coords[1]>2*taille_carrée and coords[1]<5*taille_carrée) or (coords[1]>6*taille_carrée)):
                coords=(41*taille_carrée,coords[1])
                coords=(coords[0]+taille_carrée,coords[1])
                coordscarte=(coordscarte[0]-1,coordscarte[1])
                FondCarte=("Carte"+str(changement_carte(coordscarte)))
                if FondCarte=="Carte0_0":
                    FondCarte2=Carte0_0
                    item = Canevas.create_image(0,0,anchor=NW, image=FondCarte2)
                    Affichage_perso(gauche)

        if FondCarte=="Carte1_10":
            if limite_Carte1_10()==True:
                coords=(coords[0]+(taille_carrée/taille_carrée),coords[1])



def Anim_droite():
    global coords,perso,taille_carrée,Choix,coordscarte,FondCarte,FondCarte2,compteur_mouvement
    if Page_Accueil==False:
        
        compteur_mouvement+=1
    
        coords=(coords[0]+(taille_carrée/taille_carrée),coords[1])
        Canevas.delete(perso)
        Affichage_perso(droite)

        if FondCarte=="Carte0_0":
            if limite_carte0_0()==True:
                coords=(coords[0]-(taille_carrée/taille_carrée),coords[1])

            if (coords[0]>41*taille_carrée) and ((coords[1]>2*taille_carrée and coords[1]<5*taille_carrée) or (coords[1]>6*taille_carrée)):
                coords=(0*taille_carrée,coords[1])
                coords=(coords[0]-taille_carrée,coords[1])
                coordscarte=(coordscarte[0]+1,coordscarte[1])
                FondCarte=("Carte"+str(changement_carte(coordscarte)))
                if FondCarte=="Carte1_0":
                    FondCarte2=Carte1_0
                    item = Canevas.create_image(0,0,anchor=NW, image=FondCarte2)
                    Affichage_perso(droite)

        if FondCarte=="Carte1_0":
            if limite_carte1_0()==True:
                coords=(coords[0]-(taille_carrée/taille_carrée),coords[1])

        if FondCarte=="Carte1_10":
            if limite_Carte1_10()==True:
                coords=(coords[0]-(taille_carrée/taille_carrée),coords[1])

def Valider_Draco():
    global Boutton2,Boutton3,Boutton4,Boutton5
    Valider(0)
    Boutton2.configure(state=DISABLED)
    Boutton3.configure(state=ACTIVE)
    Boutton4.configure(state=ACTIVE)
    Boutton5.configure(state=ACTIVE)

def Valider_Caninos():
    global Boutton2,Boutton3,Boutton4,Boutton5
    Valider(1)
    Boutton3.configure(state=DISABLED)
    Boutton2.configure(state=ACTIVE)
    Boutton4.configure(state=ACTIVE)
    Boutton5.configure(state=ACTIVE)

def Valider_Pikachu():
    global Boutton2,Boutton3,Boutton4,Boutton5
    Valider(2)
    Boutton4.configure(state=DISABLED)
    Boutton2.configure(state=ACTIVE)
    Boutton3.configure(state=ACTIVE)
    Boutton5.configure(state=ACTIVE)

def Valider_Bulbizarre():
    global Boutton2,Boutton3,Boutton4,Boutton5
    Valider(3)
    Boutton5.configure(state=DISABLED)
    Boutton2.configure(state=ACTIVE)
    Boutton3.configure(state=ACTIVE)
    Boutton4.configure(state=ACTIVE)



def Valider(index):
    global Liste,Choix,perso,Canevas,coords
    Canevas.delete(perso)
    print(Choix)
    if index==0:
        Choix="Draco"
        print("Draco")
    elif index==1:
        Choix="Caninos"
        print("Caninos")
    elif index==2:
        Choix="Pikachu"
        print("Pikachu")
    elif index==3:
        Choix="Bulbizarre"
        print("Bulbizarre")

    if Choix=="Draco":
        if Event==False:
            perso=Canevas.create_image(coords,image=DracoVue_face)
            Label1.configure(text="Vas-y Draco !")
        
    elif Choix=="Caninos":
        if Event==False:
            perso=Canevas.create_image(coords,image=CaninosVue_face)
            Label1.configure(text="Vas-y Caninos !")
        
    elif Choix=="Pikachu":
        if Event==False:
            perso=Canevas.create_image(coords,image=PikachuVue_face)
            Label1.configure(text="Vas-y Pikachu !")
        
    elif Choix=="Bulbizarre":
        if Event==False:
            perso=Canevas.create_image(coords,image=BulbizarreVue_face)
            Label1.configure(text="Vas-y Bulbizarre !")
    Canevas.focus_set()


def aléatoire():
    global compteur_mouvement2,date
    if compteur_mouvement2>=date:
        print ("Mouvement 2 =",compteur_mouvement2)
        compteur_mouvement2=0
        evenement()

def evenement():
    global compteur_mouvement2,Event,date,Dégat_0,Dégat_1,Dégat_2,Dégat_3,Dégat_4,Dégat_5,Dégat_6,Carte,coordsfleche,init,Progression_Dégat_vs,Progression_Dégat_me,init_evenement,compteur_attaque_me,compteur_attaque_vs,init_Dégat,        Progression_Dégat_me,Progression_Dégat_vs,Choix_attaque_vs,Choix_attaque_me
    Event=True
#    if Event==True:
    if init_evenement==0:
        Carte=Canevas.create_image(0,512,anchor=SW,image=Carte_Combat)
        init_evenement+=1
#        Progression_Dégat_me=Dégat_0
#        Progression_Dégat_vs=Dégat_0
        Choix_attaque_me=10
        Choix_attaque_vs=10
        
#    Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text="Que voulez-vous faire ? ",font=("Tahoma",20))
#    Attaque1=Canevas.create_text(32*taille_carrée,13*taille_carrée,anchor=SW,text="Charge",font=("Tahoma",20))
#    Attaque2=Canevas.create_text(25*taille_carrée,13*taille_carrée,anchor=SW,text="Griffe",font=("Tahoma",20))
#    Attaque3=Canevas.create_text(32*taille_carrée,15*taille_carrée,anchor=SW,text="Pique",font=("Tahoma",20))
#    Attaque4=Canevas.create_text(25*taille_carrée,15*taille_carrée,anchor=SW,text="Morsure",font=("Tahoma",20))
#    Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=("Tahoma",20))
    Canevas.update()
    Fleche_haut()
    Dégat()


#        Canevas.delete(perso)
#        Canevas.delete(Carte)
#    if compteur_attaque_vs==6 or compteur_attaque_me==6:
#        date=randint(20,100)
#        print(" ")
#        print("date =",date)
#        print(" ")
#        Canevas.delete(Carte)
#        Event=False
#        init=0


def Dégat():
    global Carte,Choix,progression_attaque,Choix_attaque_me,Choix_attaque_vs,compteur_attaque_me,\
           compteur_attaque_vs,Progression_Dégat_vs,Progression_Dégat_me,Texte1,init_Dégat,coté,FondCarte,\
           Carte0_0,Carte1_0,Carte1_10,Event,date,init,init_evenement,FondCarte2

#------------- Texte lié aux attaques -------------

    if init_Dégat!=0:
    
        if Choix_attaque_me==0:
            Canevas.delete(Texte1)
            Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text=Choix+" utilise griffe",font=("Tahoma",20))
        
        if Choix_attaque_me==1:
            Canevas.delete(Texte1)
            Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text=Choix+" utilise charge",font=("Tahoma",20))

        if Choix_attaque_me==2:
            Canevas.delete(Texte1)
            Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text=Choix+" utilise morsure",font=("Tahoma",20))

        if Choix_attaque_me==3:
            Canevas.delete(Texte1)
            Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text=Choix+" utilise pique",font=("Tahoma",20))

#------------- Texte lié aux attaques -------------

    init_Dégat+=1    
    if (Choix_attaque_me==0 or Choix_attaque_me==1 or Choix_attaque_me==2) and (compteur_attaque_vs<6 or compteur_attaque_me<6):
        compteur_attaque_me+=1
        Progression_Dégat_me=('Dégat_',compteur_attaque_me)
        
    if Progression_Dégat_me ==('Dégat_',0):
        Progression_Dégat_me=Dégat_0
        
    elif Progression_Dégat_me ==('Dégat_',1):
        Progression_Dégat_me=Dégat_1
        
    elif Progression_Dégat_me ==('Dégat_',2):
        Progression_Dégat_me=Dégat_2
        
    elif Progression_Dégat_me ==('Dégat_',3):
        Progression_Dégat_me=Dégat_3
        
    elif Progression_Dégat_me ==('Dégat_',4):
        Progression_Dégat_me=Dégat_4
        
    elif Progression_Dégat_me ==('Dégat_',5):
        Progression_Dégat_me=Dégat_5
        
    elif Progression_Dégat_me ==('Dégat_',6):
        Progression_Dégat_me=Dégat_6
        
    Dégat1=Canevas.create_image(160,160,anchor=SW,image=Progression_Dégat_me)
    print("Progression_Dégat_me = ",Progression_Dégat_me)
    print("compteur_attaque_me = ",compteur_attaque_me)

    Canevas.update()
    sleep(0.5)

    Choix_attaque_vs=randint(0,4)
    if (Choix_attaque_vs==0 or Choix_attaque_vs==1 or Choix_attaque_vs==2) and (compteur_attaque_vs<6 or compteur_attaque_me<6) :
        compteur_attaque_vs+=1
        Progression_Dégat_vs=('Dégat_',compteur_attaque_vs)

    if Progression_Dégat_vs ==('Dégat_', 0):
        Progression_Dégat_vs=Dégat_0
        
    elif Progression_Dégat_vs ==('Dégat_',1):
        Progression_Dégat_vs=Dégat_1
        
    elif Progression_Dégat_vs ==('Dégat_',2):
        Progression_Dégat_vs=Dégat_2
        
    elif Progression_Dégat_vs ==('Dégat_',3):
        Progression_Dégat_vs=Dégat_3
        
    elif Progression_Dégat_vs ==('Dégat_',4):
        Progression_Dégat_vs=Dégat_4
        
    elif Progression_Dégat_vs ==('Dégat_',5):
        Progression_Dégat_vs=Dégat_5
        
    elif Progression_Dégat_vs ==('Dégat_',6):
        Progression_Dégat_vs=Dégat_6
        
    Dégat2=Canevas.create_image(896,320,anchor=SW,image=Progression_Dégat_vs)

    
#    for i in range (7):
#        Progression_Dégat="Dégat_",i
#        print (Progression_Dégat)
#        if Progression_Dégat ==('Dégat_', 0):
#            Progression_Dégat=Dégat_0
#        if Progression_Dégat ==('Dégat_', 1):
#            Progression_Dégat=Dégat_1
#        if Progression_Dégat ==('Dégat_', 2):
#            Progression_Dégat=Dégat_2
#        if Progression_Dégat ==('Dégat_', 3):
#            Progression_Dégat=Dégat_3
#        if Progression_Dégat ==('Dégat_', 4):
#            Progression_Dégat=Dégat_4
#        if Progression_Dégat ==('Dégat_', 5):
#            Progression_Dégat=Dégat_5
#        if Progression_Dégat ==('Dégat_', 6):
#            Progression_Dégat=Dégat_6
#        Dégat1=Canevas.create_image(160,160,anchor=SW,image=Progression_Dégat)
#        Dégat2=Canevas.create_image(896,320,anchor=SW,image=Progression_Dégat)
    if Choix=="Pikachu":
        Pikachu=Canevas.create_image(288,320,anchor=SW,image=Pikachu_dos)
    if Choix=="Bulbizarre":
        Bulbizarre=Canevas.create_image(288,320,anchor=SW,image=Bulbizarre_dos)
    if Choix=="Caninos":
        Caninos=Canevas.create_image(288,320,anchor=SW,image=Caninos_dos)
    if Choix=="Draco":
        Draco=Canevas.create_image(288,320,anchor=SW,image=Draco_dos)
    Rattata=Canevas.create_image(864,192,anchor=SW,image=Rattata_face)
    Canevas.update()
##    sleep(1)
#        Canevas.delete(Rattata)
#        Canevas.delete(Bulbizarre)
#        Canevas.delete(Dégat1)
#        Canevas.delete(Dégat2)

#        Canevas.delete(Dégat1)
#        Canevas.delete(Dégat2)
#        Canevas.delete(Bulbizarre)
#        Canevas.delete(Rattata)
#        Canevas.delete(Texte1)
#        Canevas.delete(Attaque1)
#        Canevas.delete(Attaque2)
#        Canevas.delete(Attaque3)
#        Canevas.delete(Attaque4)
#        Canevas.delete(Fleche)
    if compteur_attaque_vs==6:
        Canevas.delete(Texte1)
        Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text="Rattata a gagné",font=("Tahoma",20))

    if compteur_attaque_me==6:
        Canevas.delete(Texte1)
        Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text=Choix+" a gagné",font=("Tahoma",20))

    Canevas.update()
    sleep(1)
    
    if compteur_attaque_vs==6 or compteur_attaque_me==6:
        sleep(1)
        Choix_attaque_vs=10
        Choix_attaque_me=10
        Progression_Dégat_me=Dégat_0
        Progression_Dégat_vs=Dégat_0
        compteur_attaque_me=0
        compteur_attaque_vs=0
        Canevas.delete(ALL)
        Carte=Canevas.create_image(0,512,anchor=SW,image=Carte_Combat)
        compteur_attaque_vs=0
        compteur_attaque_me=0
        init_Dégat=0
        sleep(1)
        Canevas.delete(ALL)

        ##########################################
        date=randint(20,100)
#        date=randint(10,12)
        print(" ")
        print("date =",date)
        print(" ")
        Canevas.delete(Carte)
        FondCarte=("Carte"+str(changement_carte(coordscarte)))
        print("FondCarte = ",FondCarte)
        if FondCarte=="Carte1_0":
            FondCarte2=Carte1_0
        if FondCarte=="Carte0_0":
            FondCarte2=Carte0_0
        if FondCarte=="Carte1_10":
            FondCarte2=Carte1_10
        item = Canevas.create_image(0,0,anchor=NW, image=FondCarte2)
        perso=Canevas.create_image(coords,anchor=SW,image=Affichage_perso("haut"))
        Affichage_perso(bas)
        Event=False
        init=0
        init_evenement=0
        ##########################################


def Fleche_droite():
    Selection("droite")

def Fleche_gauche():
    Selection("gauche")

def Fleche_haut():
    Selection("haut")

def Fleche_bas():
    Selection("bas")

def Fleche_entrée():
    Selection("entrée")

def Selection(coté):
    global coordsfleche,init,Texte1,Attaque1,Attaque2,Attaque3,Attaque4,Fleche,Choix_attaque_me,coordsfleche,Texte2,Choix0,Choix1,Choix2,Choix3,Fleche,Choix,init_Accueil,\
           Page_Accueil,FondCarte2,init_Accueil,Page_Accueil,perso,coordscarte,FondCarte,Boutton2,Boutton3,Boutton4,Boutton5
    print("Coté =",coté)

            ######################################
    
    if Page_Accueil==True:
#        if init_Accueil==0:
#            Texte2=Canevas.create_text(6*taille_carrée,4*taille_carrée,anchor=SW,text="Avant de débuter votre quête, veuillez décider quel pokémon vous accompagnera",font=(fonte,20))
#    
#            Choix0=Canevas.create_text(4*taille_carrée,7*taille_carrée,anchor=SW,text="Draco",font=(fonte,20))
#            Choix1=Canevas.create_text(14*taille_carrée,7*taille_carrée,anchor=SW,text="Caninos",font=(fonte,20))
#            Choix2=Canevas.create_text(24*taille_carrée,7*taille_carrée,anchor=SW,text="Pikachu",font=(fonte,20))
#            Choix3=Canevas.create_text(34*taille_carrée,7*taille_carrée,anchor=SW,text="Bulbizarre",font=(fonte,20))
#
#        
#
#            Draco=Canevas.create_image(4*taille_carrée,10*taille_carrée,anchor=SW,image=Draco_face)
#            Caninos=Canevas.create_image(14*taille_carrée,10*taille_carrée,anchor=SW,image=Caninos_face)
#            Pikachu=Canevas.create_image(24*taille_carrée,10*taille_carrée,anchor=SW,image=Pikachu_face)
#            Bulbizarre=Canevas.create_image(34*taille_carrée,10*taille_carrée,anchor=SW,image=Bulbizarre_face)
#            
#            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=(fonte,20))
#            init_Accueil+=1


#--------------------- DROITE---------------------#
        if coté=="droite" and coordsfleche[0]<32*taille_carrée:
            Canevas.delete(Fleche)
            coordsfleche=(coordsfleche[0]+10*taille_carrée,coordsfleche[1])
            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=(fonte,20))
            print("Test D")
#--------------------- DROITE---------------------#



#--------------------- GAUCHE---------------------#
        elif coté=="gauche" and coordsfleche[0]>4*taille_carrée:
            Canevas.delete(Fleche)
            coordsfleche=(coordsfleche[0]-10*taille_carrée,coordsfleche[1])
            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=(fonte,20))
            print("Test G")
#--------------------- GAUCHE---------------------#



#--------------------- ENTREE---------------------#
        elif coté=="entrée":
            if coordsfleche==(3*taille_carrée,7*taille_carrée):
                Choix="Draco"
            elif coordsfleche==(13*taille_carrée,7*taille_carrée):
                Choix="Caninos"
            elif coordsfleche==(23*taille_carrée,7*taille_carrée):
                Choix="Pikachu"
            elif coordsfleche==(33*taille_carrée,7*taille_carrée):
                Choix="Bulbizarre"
            print("Choix = ",Choix)
            print("Test E")
            sleep(1)
            Canevas.delete(ALL)
            coordsfleche=(24*taille_carrée,13*taille_carrée)
            Page_Accueil=False
            init_Accueil=0
            FondCarte=("Carte"+str(changement_carte(coordscarte)))
            print("FondCarte =",FondCarte)
            if FondCarte=="Carte0_0":
                FondCarte2=Carte0_0
            elif FondCarte=="Carte1_0":
                FondCarte2=Carte1_0
            elif FondCarte=="Carte1_10":
                FondCarte2=Carte1_10


            item = Canevas.create_image(0,0,anchor=NW, image=FondCarte2)
            Canevas.grid(row=2,column=0,columnspan=1000)

            Persoactif=Choix+"Vue_face"
            if Persoactif=="DracoVue_face":
                Persoactif=DracoVue_face
            if Persoactif=="CaninosVue_face":
                Persoactif=CaninosVue_face
            if Persoactif=="PikachuVue_face":
                Persoactif=PikachuVue_face
            if Persoactif=="BulbizarreVue_face":
                Persoactif=BulbizarreVue_face

            perso=Canevas.create_image(coords,anchor=SW,image=Persoactif)

            Boutton2=Button(fen,image=Boutton_Draco,command=Valider_Draco,bg="white",relief=GROOVE)
            Boutton2.grid(row=0,column=201)
            Boutton3=Button(fen,image=Boutton_Caninos,command=Valider_Caninos,bg="white",relief=GROOVE)
            Boutton3.grid(row=0,column=202)
            Boutton4=Button(fen,image=Boutton_Pikachu,command=Valider_Pikachu,bg="white",relief=GROOVE)
            Boutton4.grid(row=0,column=203)
            Boutton5=Button(fen,image=Boutton_Bulbizarre,command=Valider_Bulbizarre,bg="white",relief=GROOVE)
            Boutton5.grid(row=0,column=204)
            
            ######################################

    else:
        if init==0:
            Texte1=Canevas.create_text(1*taille_carrée,13*taille_carrée,anchor=SW,text="Que voulez-vous faire ? ",font=("Tahoma",20))
            Attaque1=Canevas.create_text(32*taille_carrée,13*taille_carrée,anchor=SW,text="Charge",font=("Tahoma",20))
            Attaque2=Canevas.create_text(25*taille_carrée,13*taille_carrée,anchor=SW,text="Griffe",font=("Tahoma",20))
            Attaque3=Canevas.create_text(32*taille_carrée,15*taille_carrée,anchor=SW,text="Pique",font=("Tahoma",20))
            Attaque4=Canevas.create_text(25*taille_carrée,15*taille_carrée,anchor=SW,text="Morsure",font=("Tahoma",20))
            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=("Tahoma",20))
            init+=1
#         Canevas.delete(Attaque1)
#         Canevas.delete(Fleche)

#--------------------- DROITE---------------------#
        if coté=="droite" and coordsfleche[0]<25*taille_carrée:
            Canevas.delete(Fleche)
#         Canevas.delete(Dr)
#         Fleche=Canevas.create_text(coordsfleche[0]+7*taille_carrée,coordsfleche[1],anchor=SW,text=">",font=("Tahoma",20))
            coordsfleche=(coordsfleche[0]+7*taille_carrée,coordsfleche[1])
            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=("Tahoma",20))
            print("Test D")
#--------------------- DROITE---------------------#

    

#--------------------- GAUCHE---------------------#
        elif coté=="gauche" and coordsfleche[0]>25*taille_carrée:
            Canevas.delete(Fleche)
#            Fleche=Canevas.create_text(coordsfleche[0]-7*taille_carrée,coordsfleche[1],anchor=SW,text=">",font=("Tahoma",20))
            coordsfleche=(coordsfleche[0]-7*taille_carrée,coordsfleche[1])
            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=("Tahoma",20))
            print("Test G")
#--------------------- GAUCHE---------------------#



#--------------------- HAUT---------------------#
        elif coté=="haut" and coordsfleche[1]>14*taille_carrée:
            Canevas.delete(Fleche)
#            Fleche=Canevas.create_text(coordsfleche[0],coordsfleche[1]-2*taille_carrée,anchor=SW,text=">",font=("Tahoma",20))
            coordsfleche=(coordsfleche[0],coordsfleche[1]-2*taille_carrée)
            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=("Tahoma",20))
            print("Test H")
#--------------------- HAUT---------------------#



#--------------------- BAS---------------------#
        elif coté=="bas" and coordsfleche[1]<14*taille_carrée:
            Canevas.delete(Fleche)
#            Fleche=Canevas.create_text(coordsfleche[0],coordsfleche[1]+2*taille_carrée,anchor=SW,text=">",font=("Tahoma",20))
            coordsfleche=(coordsfleche[0],coordsfleche[1]+2*taille_carrée)
            Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=("Tahoma",20))
            print("Test B")
#--------------------- BAS---------------------#



#--------------------- ENTREE---------------------#
        elif coté=="entrée":
            if coordsfleche==(24*taille_carrée,13*taille_carrée):
                Choix_attaque_me=0
            elif coordsfleche==(31*taille_carrée,13*taille_carrée):
                Choix_attaque_me=1
            elif coordsfleche==(24*taille_carrée,15*taille_carrée):
                Choix_attaque_me=2
            elif coordsfleche==(31*taille_carrée,15*taille_carrée):
                Choix_attaque_me=3
            print("Choix_attaque_me = ",Choix_attaque_me)
#            Canevas.delete(Texte1)
#            Canevas.delete(Attaque1)
#            Canevas.delete(Attaque2)
#            Canevas.delete(Attaque3)
#            Canevas.delete(Attaque4)
#            Canevas.delete(Fleche)
##            Canevas.delete(ALL)
##            Carte=Canevas.create_image(0,512,anchor=SW,image=Carte_Combat)

            print("Test E")
            Dégat()
            
        
#--------------------- ENTREE---------------------#

    print(" ")    


def clavier(event):
    global perso,coords,taille_carrée,Choix,compteur_mouvement,compteur_mouvement2,Event,Page_Accueil,perso
    touche=event.keysym
    
    print(touche)
    print("Mouvements = ",compteur_mouvement/taille_carrée)
    print("Mouvements2 = ",compteur_mouvement2)
    
#    Canevas.delete(perso)

    if Page_Accueil==True:
        if touche =="Left":
            Fleche_gauche()

        elif touche =="Right":
            Fleche_droite()

        elif touche =="Return":
            Fleche_entrée()

        if touche=="q":
            fen.destroy()
    
    else:
        if perso!=0:
            Canevas.delete(perso)
        if touche =="Left":
            if Event==False:
                compteur_mouvement2+=1
                for i in range (taille_carrée):
                    compteur_mouvement+=1
                    Anim_gauche()
                    Canevas.update()
            elif Event==True:
                Fleche_gauche()


        elif touche =="Right":
            if Event==False:
                compteur_mouvement2+=1
                for i in range (taille_carrée):
                    Anim_droite()
                    Canevas.update()
            elif Event==True:
                Fleche_droite()


        elif touche =="Down":
            if Event==False:
                compteur_mouvement2+=1
                for i in range (taille_carrée) :
                    Anim_bas()
                    compteur_mouvement+=1
                    Canevas.update()
            elif Event==True:
                Fleche_bas()


        elif touche =="Up":
            if Event==False:
                compteur_mouvement2+=1
                for i in range (taille_carrée):
                    compteur_mouvement+=1
                    Anim_haut()
                    Canevas.update()
            elif Event==True:
                Fleche_haut()

        elif touche =="Return":
            if Event==True:
                Fleche_entrée()

        Canevas.coords(perso,coords[0],coords[1])

        if touche=="q":
            fen.destroy()


        elif touche=="a":           #Relance le compteur
            if Event==False:
                Event=True
            elif Event==True:
                Event=False
        aléatoire()
            

Label1=Label(text="Utilisez les flèches pour que Draco se déplace\nCarte="+str(nbr_carré_x)+"x"+str(nbr_carré_y),font=("Tahoma",15),bg="White")
Label1.grid(row=0,column=0,columnspan=150)

Canevas=Canvas(fen,width=largeur,height=hauteur,relief="raised")
Canevas.grid(row=2,column=0,columnspan=150)
item=Canevas.create_image(0,512,anchor=SW,image=Accueil)

perso=Canevas.create_image(coords,anchor=SW,image=DracoVue_face)
Canevas.delete(perso)

if init_Accueil==0:
    Texte2=Canevas.create_text(6*taille_carrée,4*taille_carrée,anchor=SW,text="Avant de débuter votre quête, veuillez décider quel pokémon vous accompagnera",font=(fonte,20))
    
    Choix0=Canevas.create_text(4*taille_carrée,7*taille_carrée,anchor=SW,text="Draco",font=(fonte,20))
    Choix1=Canevas.create_text(14*taille_carrée,7*taille_carrée,anchor=SW,text="Caninos",font=(fonte,20))
    Choix2=Canevas.create_text(24*taille_carrée,7*taille_carrée,anchor=SW,text="Pikachu",font=(fonte,20))
    Choix3=Canevas.create_text(34*taille_carrée,7*taille_carrée,anchor=SW,text="Bulbizarre",font=(fonte,20))

        

    Draco=Canevas.create_image(4*taille_carrée,10*taille_carrée,anchor=SW,image=Draco_face)
    Caninos=Canevas.create_image(14*taille_carrée,10*taille_carrée,anchor=SW,image=Caninos_face)
    Pikachu=Canevas.create_image(24*taille_carrée,10*taille_carrée,anchor=SW,image=Pikachu_face)
    Bulbizarre=Canevas.create_image(34*taille_carrée,10*taille_carrée,anchor=SW,image=Bulbizarre_face)
    
    Fleche=Canevas.create_text(coordsfleche,anchor=SW,text=">",font=(fonte,20))
    init_Accueil+=1

#FondCarte=("Carte"+str(changement_carte(coordscarte)))
#if FondCarte=="Carte0_0":
#    FondCarte2=Carte0_0
#elif FondCarte=="Carte1_0":
#    FondCarte2=Carte1_0
#elif FondCarte=="Carte1_10":
#    FondCarte2=Carte1_10
#
#
#item = Canevas.create_image(0,0,anchor=NW, image=FondCarte2)
#Canevas.grid(row=2,column=0,columnspan=1000)
#
#perso=Canevas.create_image(coords,anchor=SW,image=DracoVue_face)
#
#Boutton2=Button(fen,image=Boutton_Draco,command=Valider_Draco,bg="white",relief=GROOVE)
#Boutton2.grid(row=0,column=201)
#Boutton3=Button(fen,image=Boutton_Caninos,command=Valider_Caninos,bg="white",relief=GROOVE)
#Boutton3.grid(row=0,column=202)
#Boutton4=Button(fen,image=Boutton_Pikachu,command=Valider_Pikachu,bg="white",relief=GROOVE)
#Boutton4.grid(row=0,column=203)
#Boutton5=Button(fen,image=Boutton_Bulbizarre,command=Valider_Bulbizarre,bg="white",relief=GROOVE)
#Boutton5.grid(row=0,column=204)


Canevas.focus_set()
Canevas.bind("<Key>", clavier)

fen.mainloop()
