
import turtle

reglesDeTransformations = {}  # Génère les règles du L_system

mesCouleurs = {"1": "purple", "2": "blue", "3": "green", "4" : "yellow", "5" : "red", "6": "pink",'7': "darkgreen", "8": "lightgreen", "9":"brown" }
iterations =6
longeurSegment = 3
orientationOrigine = 90
angle = 25

#reglesDeTransformations["L"] = "3L[+L+R]8L[-L-R]6L"
#axiome="L"

#reglesDeTransformations["L"] = "3L[+L-R]8L[-L+R]6L"                             # fait línverse du programme dorigine
#axiome="L"


#reglesDeTransformations["L"] = "L[7-LR-L]R"                                     #permet de faire une plante fractale plus complexe, colorée en 3 teintes de vert
#reglesDeTransformations["R"] = "R[3+RL+L]L"
#reglesDeTransformations["3"] = "8"
#reglesDeTransformations["7"] = "3"
#axiome = "7L"

reglesDeTransformations["L"] = "9L[7-LR-L]R"                                   #" vert clair, vert et marron
reglesDeTransformations["R"] = "9R[3+RL+R]L"
reglesDeTransformations["3"] = "8"
reglesDeTransformations["7"] = "3"
axiome = "9L"


#reglesDeTransformations["L"] = "L[6-LR-L]R"                                    #"rose et rouge
#reglesDeTransformations["R"] = "R[5+RL+L]L"
#reglesDeTransformations["5"] = "6"
#reglesDeTransformations["6"] = "5"
#axiome="5L"




def calcul_iterations(_axiome, _iteration):
    derivee = [_axiome]
    for _ in range(_iteration):
        sequenceSuivante = derivee[-1]
        axiomeSuivant = [appliquer_transfo(char) for char in sequenceSuivante]
        derivee.append(''.join(axiomeSuivant))
    return derivee[-1]                                                          # renvoi de la derniere iteration (dernier element de la liste)


def appliquer_transfo(sequence):
    if sequence in reglesDeTransformations:
        return reglesDeTransformations[sequence]
    else:
        return sequence


def dessiner_l_system(turtle, sequenceDeCommandes, _longeurSegment, _angle):
    maPile = []

    for command in sequenceDeCommandes:
        turtle.pd()
        if command in [ "R", "L"]:
            turtle.forward(_longeurSegment)
        elif command == "+":
            turtle.right(_angle)
        elif command == "-":
            turtle.left(_angle)
        elif command == "[":                                                    # enregistrement de la position,de l'orientation et de la couleur
            maPile.append((turtle.position(), turtle.heading(), turtle.color()))
        elif command == "]":                                                    # retourne à la dernière position, orientation et couleur enregistrées
            turtle.pu()                                                         # pen up - la tortue ne dessine pas
            position, heading, color = maPile.pop(-1)
            turtle.goto(position)
            turtle.setheading(heading)
        elif command in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            turtle.color(mesCouleurs[command])


def set_turtle(orientationOrigine):
    r_turtle = turtle.Turtle()                # création de l'objet tortue
    r_turtle.screen.title("Plante fractale")
    r_turtle.speed(0)                         #la vitesse peut être ajustée, 0 étant le plus rapide
    r_turtle.setheading(orientationOrigine)   # orientation dórigine de la tortue
    return r_turtle


model = calcul_iterations(axiome, iterations)                # application du calcul des itérations préalablement défini
print(model)                                                 # mettre en place la tortue et dessiner L_system
r_turtle = set_turtle(orientationOrigine)                    # création de lóbjet tortue
turtle_screen = turtle.Screen()
turtle_screen.tracer(750,0)                             # création dúne fenêtre graphique
turtle_screen.screensize(1500, 1500)                         # détermination de la taille de la fenêtre graphique
dessiner_l_system(r_turtle, model, longeurSegment, angle)    # dessiner le L_system
r_turtle.hideturtle()                                        #cacher la tortue quand le l_system est dessiné
turtle_screen.title("cliquer pour terminer le programme")
turtle_screen.exitonclick()


