import random
import turtle
turtle.reset()
turtle.speed(15)
turtle.pensize(3)
turtle.up()
turtle.goto(-100,-100)
turtle.down()


def couleur_aléatoire():
    Couleur=['red','blue','green','violet','yellow','orange','magenta','steelblue','lime','gray','gold','silver']
    C=random.choice(Couleur)
    turtle.fillcolor(C)
    

def rectangle():
    couleur_aléatoire()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(140)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()
    
        
def fenetre():
    turtle.fillcolor('white')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(30)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.end_fill()
    

def balcon():
    turtle.fillcolor('white')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    for i in range (4):
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
    turtle.penup()
    turtle.forward(-35)
    turtle.pendown()
    
    
    
        
def porte():
    couleur_aléatoire()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    
    
        
def porte_arrondie():
    couleur_aléatoire()
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(40)
    turtle.circle(15,180)
    turtle.forward(40)
    turtle.left(90)
    turtle.end_fill()
    
    
    
def toit_triangle():
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(150)
    turtle.left(150)
    turtle.forward(92)
    turtle.left(60)
    turtle.forward(92)
    turtle.left(150)
    turtle.forward(10)
    turtle.end_fill()
    
    
def toit_plat():
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(145)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(5)
    turtle.end_fill()

def aleatoire():
    E=random.randint(1,2)
    if E==1:
        turtle.penup()
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.pendown()
        fenetre()
    else:
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()
        balcon()


def immeuble():
    rectangle()
    compteur=0
    E=random.randint(1,3)
    if E==1:
        turtle.penup()
        turtle.forward(15)
        turtle.pendown()
        porte()
        compteur+=1
    elif E==2:
        turtle.penup()
        turtle.forward(15)
        turtle.pendown()
        porte_arrondie()
        compteur+=1
    elif E==3:
        turtle.penup()
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.pendown()
        fenetre()
        compteur+=0
    if compteur==1:
        turtle.penup()
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.pendown()
        fenetre()
    else:
        E=random.randint(1,3)
        if E==1:
            turtle.penup()
            turtle.forward(40)
            turtle.pendown()
            porte()
            compteur+=1
        elif E==2:
            turtle.penup()
            turtle.forward(40)
            turtle.pendown()
            porte_arrondie()
            compteur+=1
        elif E==3:
            turtle.penup()
            turtle.forward(40)
            turtle.left(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.pendown()
            fenetre()
            compteur+=0
    if compteur==1:
        turtle.penup()
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.pendown()
        fenetre()
    elif compteur==0:
        E=random.randint(1,2)
        if E==1:
            turtle.penup()
            turtle.forward(40)
            turtle.pendown()
            porte()
            compteur+=1
        elif E==2:
            turtle.penup()
            turtle.forward(40)
            turtle.pendown()
            porte_arrondie()
            compteur+=1
    turtle.penup()
    turtle.forward(-95)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.pendown()
    for i in range(random.randint(0,4)):
        rectangle()
        E=random.randint(1,2)
        if E==1:
            turtle.penup()
            turtle.forward(15)
            turtle.left(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.pendown()
            fenetre()
        else:
            turtle.penup()
            turtle.forward(15)
            turtle.pendown()
            balcon()
        for i in range(2):
            aleatoire()
        turtle.penup()
        turtle.forward(-95)
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()
    E=random.randint(1,2)
    if E==1:
        toit_triangle()
    else:
        toit_plat()
        
    
    
turtle.forward(40)        
immeuble()
turtle.up()
turtle.goto(40,-100)
turtle.down()
turtle.forward(80)
immeuble()
turtle.up()
turtle.goto(220,-100)
turtle.down()
turtle.forward(80)
immeuble()
turtle.up()
turtle.goto(400,-100)
turtle.down()
turtle.forward(80)
immeuble()
turtle.up()
turtle.goto(580,-100)
turtle.down()
turtle.forward(80)



    
    
        
        
    

    
