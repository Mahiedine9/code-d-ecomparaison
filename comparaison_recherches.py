#construction de liste1

l=list(range(0, 100))

o=str(l)

#le module timeit

from timeit import timeit

#Q1

timeit(stmt='(1+sqrt(5))/2',

           setup='from math import sqrt',

           number=10000000)

#comparaison des temps d'éxecution

 

LONGUEURS_LISTES = list(range(1,101))

NOMBRE_EVAL = 100

 

#Q2

def entiers_aleatoires(x):

    from random import randint

    li=[]

    for i2 in range(0,x-1):
        li.append(randint(0,i2+1))   

    return li

 

LISTE_ENTIERS=entiers_aleatoires(100)

#Q3

temps1=[]

for k in range(1, 100):

    o=LISTE_ENTIERS[k-1]

    p=list(range(0,k+1))

    t=timeit(stmt='recherche_sequentielle(o,p)',

        setup='from algo_recherches import recherche_sequentielle;from  __main__ import p,o',

        number=1)

    temps1.append(t)

print(temps1)

#Q3B

temps2=[]

for g in range(1, 100):

    o=LISTE_ENTIERS[g-1]

    p=list(range(0,g+1))

    t=timeit(stmt='recherche_sequentielle_triee(o,p)',

        setup='from algo_recherches import recherche_sequentielle_triee; from __main__ import p,o',

        number=1)

    temps2.append(t)

print(temps2)

       

#Q3C

temps3=[]

for n in range(1, 100):

    o=LISTE_ENTIERS[n-1]

    p=list(range(0,n+1))

    t=timeit(stmt='recherche_dichotomique(o,p)',

        setup='from algo_recherches import recherche_dichotomique;from __main__ import p,o',

        number=1)

    temps3.append(t)

print(temps3)

 

import matplotlib.pyplot as plt

#a

ordo=temps1

absi=list(range(1,100))

plt.plot(absi,ordo,color='blue')

plt.show()

#b

 

ordo2=temps2

absi2=list(range(1,100))

plt.plot(absi2 ,ordo2, color='green')

plt.show()

#c

 

ordo3=temps3

absi3=list(range(1,100))

plt.plot(absi3 ,ordo3, color='red')

plt.show()

#2 tracer les droit courbes

ordo11=temps1

absi11=list(range(1,100))

plt.plot(absi11 ,ordo11, color='blue', label='sequentielle fructueuse')

ordo22=temps2

absi22=list(range(1,100))

plt.plot(absi22 ,ordo22, color='green', label='sequentielle triee fructueuse')

ordo33=temps3

absi33=list(range(1,100))

plt.plot(absi33 ,ordo33, color='red', label='dichotomique fructueuse')
plt.legend()
plt.show()

#recherche infructueuse###############

for i in LISTE_ENTIERS:
    a=LISTE_ENTIERS.index(i)
    LISTE_ENTIERS[a] =i+0.5
##construire la liste temps1b pour la recherche sequentielle infructueuse##

temps1b=[]
for k2 in range(1, 100):

    o1=LISTE_ENTIERS[k2-1]

    p1=list(range(0,k2+1))

    t1=timeit(stmt='recherche_sequentielle(o1,p1)',

        setup='from algo_recherches import recherche_sequentielle;from  __main__ import p1,o1',

        number=1)

    temps1b.append(t)

###construire la liste temps1b pour la recherche sequentielle triee infructueuse
temps2b=[]
for g2 in range(1, 100):

    o2=LISTE_ENTIERS[g2-1]

    p2=list(range(0,g2+1))

    t2=timeit(stmt='recherche_sequentielle_triee(o2,p2)',

        setup='from algo_recherches import recherche_sequentielle_triee; from __main__ import p2,o2',

        number=1)

    temps2b.append(t2)


#####construire la liste temps1b pour la recherche dichotomique infructueuse

temps3b=[]    
for n2 in range(1, 100):

    o3=LISTE_ENTIERS[n2-1]

    p3=list(range(1,n2+1))

    t3=timeit(stmt='recherche_dichotomique(o3,p3)',

        setup='from algo_recherches import recherche_dichotomique;from __main__ import p3,o3',

        number=1)
    temps3b.append(t3)
    
    
#construire les trois courbes sur un meme graphique
ordo12=temps1b

absi12=list(range(1,100))

plt.plot(absi12 ,ordo12, color='blue', label='sequentielle infructueuse')

ordo23=temps2b

absi23=list(range(1,100))

plt.plot(absi23 ,ordo23, color='green', label='sequentielle triee infructueuse')

ordo34=temps3b

absi34=list(range(1,100))

plt.plot(absi34 ,ordo34, color='red', label = 'dichotomique infructueuse')
plt.title("graphique avec les trois courbes de recherches pour des recherches infructueuses")
plt.legend()
plt.show()



#commentaire

##on voit sur le graphe que la fonction de recherche sequentielle prend les plus grande valeures comparée

##au deux autres car l'algorithme n'est pas optimiser et le nombre de comparaison est plus grand dans celle-ci,

##l'algorithme de recherche dichotomique est le plus optimiser et prend les valeures les plus petites dans ce graphe,

##on voit que dans la fonction dichotomique les valeures sont plus stable par rapport au deux autres fonction.
