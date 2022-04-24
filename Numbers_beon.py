"""
SOLUTION 

A given has the following lead sequence:
POST A
PLEASE B
PLEASE C
DELETE 1
ADD ON D
CHANGE B
POST E
SHIFT B
After completing the first questions you will have ABC, then AB, ABD,
ABB, ABB last instruction, first B to C, then finally replace
inscription to ACBE.

"""

def zadanie_4_1(wejscie):
    wynik = 0
    for item in wejscie:
        krok = item.split()[0]
        if krok == 'PLEASE':
            wynik+=1
        if krok == 'DELETE':
            wynik-=1
        if krok == 'CHANGE':
            pass
        if krok == 'PLEASE':
            pass
    return wynik
