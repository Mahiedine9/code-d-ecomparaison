# -*- coding: utf-8 -*-

"""
TP AP1

Analyse des algorithmes de recherche

"""

def compare(a, b):
    """
    :param a: (any) un element
    :param b: (any) un element
    :return: (bool) * 1 si a est plus grand que b
                    * 0 si a est egal Ã  b
                    * -1 si a est plus petit que b
    :CU: a et b sont comparables
    :Exemples:
    
    >>> compare(1, 2)
    -1
    >>> compare('z', 'a')
    1
    >>> compare(0, 0)
    0
    """
    if a > b:
        res = 1
    elif a < b:
        res = -1
    else:
        res = 0
    return res

def est_trie(l, cmp = compare):
    """
    :param l: (list) une liste
    :param cmp: (function) une fonction de comparaison
    :return: (bool) True si la liste est triÃ©e, False sinon
    :CU: les Ã©lÃ©ments de l sont comparables avec cmp
    :Exemples:

    >>> est_trie([])
    True
    >>> est_trie( [1, 2, 3] )
    True
    >>> est_trie( list(range(10, 0, -1)))
    False
    """
    if len(l)==0:
        return True
    a=l[0]
    i=1
    trouve=True
    
    while i<len(l) and trouve==True:
        if cmp(l[i],a)==-1:
            trouve=False
        a=l[i]
        i+=1
    return trouve
r=est_trie([])        
    
def recherche_sequentielle(x, l, cmp = compare):
    """
    :param x: (any) un element 
    :param l: (list) une liste
    :return: (bool) True si x appartient a  l, False sinon
    :CU: x doit etre comparable aux elements  de l
    :Exemples:

    >>> recherche_sequentielle(1, [])
    False
    >>> l = list(range(10))
    >>> recherche_sequentielle(5, l)
    True
    >>> recherche_sequentielle(5.5, l)
    False
    """
    trouve=False
    i=0
    while i<len(l) and trouve==False :
        if cmp(l[i],x)==0:
            trouve=True
        i+=1
        
    return trouve


def recherche_sequentielle_triee(x, l, cmp = compare):
    """
    :param x: (any) un Ã©lÃ©ment 
    :param l: (list) une liste
    :return: (bool) True si x appartient Ã  l, False sinon
    :CU: x doit Ãªtre comparable aux Ã©lÃ©ments de l,
         l est triÃ©e
    :Exemples:

    >>> recherche_sequentielle_triee(1, [])
    False
    >>> l = list(range(10))
    >>> recherche_sequentielle_triee(5, l)
    True
    >>> recherche_sequentielle_triee(5.5, l)
    False
    """
    fini=False
    trouve=False
    i=0
    while i<len(l) and trouve==False and fini==False:
        if cmp(l[i],x)==0:
            trouve=True
        if cmp(l[i],x)>0:
            fini=True
        i+=1
            
    return trouve


def recherche_dichotomique(x, l, cmp = compare):
    """
    :param x: (any) un element 
    :param l: (list) une liste
    :return: (bool) True si x appartient a  l, False sinon
    :CU: x doit etre comparable aux elements de l,
         l est triee
    :Exemples:

    >>> recherche_dichotomique(1, [])
    False
    >>> l = list(range(10))
    >>> recherche_dichotomique(5, l)
    True
    >>> recherche_dichotomique(5.5, l)
    False
    """
    if len(l)==0:
        return False
    d=0
    f=len(l)-1
    while d<f:
        m=(d+f)//2
        if cmp(l[m],x)<0:
            d=m+1
        else:
            f=m
    if x==l[d]:
        return True
    else:
        return False
   

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)


