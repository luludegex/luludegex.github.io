#etape6:A+B+A+A+B+A+B+A+A+B+A+A+B

from turtle import*

codeGen="AB"
codeTemp=""
etapes= 17 # nous appercevons l'apparition d'une rosace complète à partir de 17 itérations
color("light blue")
tracer(750,0)
for nombre in range(etapes -1):
    codeTemp=""
    for element in  codeGen:
     if element =="A":
        codeTemp=codeTemp+"A+B"
     else :
        codeTemp=codeTemp+"A"
    codeGen=codeTemp



for element in codeGen:
    if element=="A":
        left(10)
    if element=="B":
        forward(10)
    if element=="+":
        right(10)
update()
done()

