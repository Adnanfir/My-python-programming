import random
from random import choice
Questions={"question Ist":"WHy isn't the sky blue",'Question second':"What is 2+2","Question Third":"What is the Colour of the sun"}
Question=choice(Questions)
Answer = input(Question).strip().capitalize()
while Answer!="Just Because":
    Answer=input("Why").strip().capitalize()
print("Ohh... okay")
    