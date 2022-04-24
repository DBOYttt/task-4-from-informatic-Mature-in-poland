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

from turtle import update


score = 0

while True:

        x = {'PLEASE'}

        if x == {'PLEASE'}:
            score += 1
        if score == 3:
            x.clear()
            x.update({'DELETE'})
print(score)
