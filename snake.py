from turtle import Turtle, Screen
from time import sleep
from random import randint

# creo un istanza per la classe Screen e la setto 600px x 600px
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)                                                      # "spegnere" l'animazione se passo 0 come parametro


posizioni = [(0,0), (-20,0), (-40,0)]                                 # mi sposto di 20 a sinistra considerando che di default la posizione iniziale è 0

snake = []

for pos in posizioni:
    s = Turtle("square")                                 # creo una istanza s della classe Turtle di forma quadrata (square) con 20px per lato di default
    s.penup()
    s.goto(pos)
    snake.append(s)




start = True                                            # essendo while un ciclo infito, partiamo con una condizione True che al verificarsi della condizione False presente all'interno di while, farà sì che il ciclo finisca                                  
while start:
    screen.update()                                     # si muovono tutti i quadrati all'unisolo
    sleep(0.1)                                      # sleep permetterà al cursore di muoversi secondo la velocità inserita come parametro espressa in secondi
    # per far sì che tutti i componenti del serpente si muovano nella stessa direzione, ogni elemento dovrà spostarsi nelle coordinate dell'elemento che lo precede:
    for num in range(len(snake), -1,0, -1):                 # così crescerà man mano che mangia                               
        x = snake[num-1].xcor()
        y = snake[num-1].ycor()

        snake[num].goto(x,y)     
    snake[0].forward(20)
    snake[0].left(20)  















screen.exitonclick()