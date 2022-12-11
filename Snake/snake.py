import time
import random as rd
import tkinter as tk
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

class Inicio:
    def __init__(self,root):
        # ------------- Configuracion de la ventana tkinter
        self.root=root                      # creo la ventana
        self.root.title("SNAKE")            # titulo
        self.root.geometry("600x600")       # dimensiones
        self.root.config(bg = "#1C1C1C")    # fondo
        #self.root.resizable(0,0)            # bloquea el tamanio
        self.root.iconbitmap("C:/Users/antoo/Downloads/Snake/serpiente.ico") # coloco un icono personalizado
        
        Label (self.root, text=" S N A K E ",bg="green",foreground="white",font=("Helvetica", 40, "normal")).place(x=160,y=150) 

        Label (self.root, text="¿COMENZAR A JUGAR?",bg="#1C1C1C",foreground="white",font=("Helvetica", 15, "normal")).place(x=180,y=300)
        self.redireccion()
        
    def gameover(self):
        self.canvas = Label(self.root)  
        self.canvas.config(width="650", height="600",borderwidth = "0",bg="#1C1C1C")
        self.canvas.place(x=0, y=0)

        Label (self.root, text="  G A M E   O V E R  ",bg="red",foreground="white",font=("Helvetica", 30, "normal")).place(x=120,y=150) 

        Label (self.root, text="¿CONTINUAR JUGANDO?",bg="#1C1C1C",foreground="white",font=("Helvetica", 15, "normal")).place(x=180,y=300)
        self.redireccion()
        
    def redireccion(self):
        gameSnake = Game()
        Button(self.root, text=" SI ",bg="#1C1C1C",foreground="white",font=("Helvetica", 15, "normal"),borderwidth = "0",activebackground="#1C1C1C",activeforeground="#FFEC00",cursor="hand2",command=lambda:gameSnake.ventanaJuego(self.root)).place(x= 250, y=350)
        Button(self.root, text=" NO ",bg="#1C1C1C",foreground="white",font=("Helvetica", 15, "normal"),borderwidth = "0",activebackground="#1C1C1C",activeforeground="red",cursor="hand2",command=lambda:self.root.destroy()).place(x= 300, y=350)   

class Game(Inicio):
    def __init__(self):
        self.score = 1
        archivo=open("record.txt","r")
        record=archivo.read()
        archivo.close()
        self.highScore = int(record)

    def ventanaJuego(self,root):
        # ------------- Configuracion de la ventana tkinter
        self.root=root                      # creo la ventana
        self.root.title("SNAKE")            # titulo
        self.root.geometry("600x600")       # dimensiones
        self.root.config(bg = "#1C1C1C")    # fondo
        self.root.resizable(0,0)            # bloquea el tamanio
        self.root.iconbitmap("C:/Users/antoo/Downloads/Snake/serpiente.ico") # coloco un icono personalizado

        self.canvas = ScrolledCanvas(self.root)  
        self.canvas.config(width="550", height="500",borderwidth = "1",highlightcolor="white")
        self.canvas.place(x=21, y=20)
        
        # ------------- Configuracion de la ventana turtle
        self.wn = TurtleScreen(self.canvas)                                 # creo la ventana
        self.wn.screensize(canvwidth = 10, canvheight = 10, bg = "#1C1C1C") # fondo
        self.wn.tracer(0)                                                   # mejora animaciones

        # ------------- Llamo funciones principales
        self.confComida()
        self.confSnake()
        self.confTeclado()
        self.confMarcador()
        self.comenzar()
        
    #  ------------- Funciones del juego
    def confSnake(self):   
        # ------------- Snake // Cabeza
        self.cabeza = RawTurtle(self.wn)         # crea un elemento turtle
        self.cabeza.speed(0)                     # ubica el elemento en la pantalla
        self.cabeza.shape("square")              # le da forma de cuadrdo
        self.cabeza.color("#FFEC00")             # color de la cabeza
        self.cabeza.penup()                      # quita el rastro al moverse
        self.cabeza.goto(0,0)                    # posision al empezar 
        self.cabeza.direction = "stop"           # declara el movimiento
        
        # ------------- Snake // Cuerpo 
        self.cuerpo=[]
    
    def confComida(self):
        # ------------- Comida
        self.comida = RawTurtle(self.wn)        # crea un elemento turtle
        self.comida.speed(0)                    # ubica el elemento en la pantalla
        self.comida.shape("circle")             # le da forma de cuadrdo
        self.comida.color("red")                # color de la cabeza
        self.comida.penup()                     # quita el rastro al moverse
        self.comida.goto(0,100)                 # posision al empezar 
        self.comida.direction = "stop"          # declara el movimiento

    def confMarcador(self):
        self.texto="Score: {}                                            High Score: {}".format(self.score,self.highScore)
        Label(self.root, text=self.texto,
            width=50,
            bg="#1C1C1C",
            foreground="white",
            anchor="center",
            font=("Helvetica", 15, "normal")).place(x="21", y="540")

    def confTeclado(self):
        # ------------- teclado
        self.wn.listen()                          # toma las teclas presionadas del teclado
        self.wn.onkeypress(self.arriba,"Up")      # declara la tecla y su funcion
        self.wn.onkeypress(self.abajo,"Down")     # declara la tecla y su funcion
        self.wn.onkeypress(self.izquierda,"Left") # declara la tecla y su funcion
        self.wn.onkeypress(self.derecha,"Right")  # declara la tecla y su funcion

    # ------------- Funciones de movimiento
    def arriba(self):
        self.cabeza.direction = "up"    # declara la direccion hacia arriba
    
    def abajo(self):
        self.cabeza.direction = "down"  # declara la direccion hacia abajo
    
    def izquierda(self):
        self.cabeza.direction = "left"  # declara la direccion hacia la izquierda
    
    def derecha(self):
        self.cabeza.direction = "right" # declara la direccion hacia la derecha

    def mover(self): 
        if self.cabeza.direction == "up":    # lo mueve hacia arriba
            y = self.cabeza.ycor()
            self.cabeza.sety(y + 20)
        if self.cabeza.direction == "down":  # lo mueve hacia abajo
            y = self.cabeza.ycor()
            self.cabeza.sety(y - 20)
        if self.cabeza.direction == "left":  # lo mueve hacia la izquierda
            x = self.cabeza.xcor()
            self.cabeza.setx(x - 20)
        if self.cabeza.direction == "right": # lo mueve hacia la derecha
            x = self.cabeza.xcor()
            self.cabeza.setx(x + 20)

    def morir(self):
        time.sleep(0.2)                 # tiempo de espera para volver a empezar
        if self.highScore <= int(self.score):
            score=str(self.score)
            print(score)
            archivo=open("record.txt","w")
            archivo.write(score)
            archivo.close()

        self.score = 0                  # reinicia el contador
        self.confMarcador()
        self.cabeza.goto(0,0)           # lo envia al centro
        self.cabeza.direction = "stop"  # lo mantiene quieto
        self.gameover()

        # ------------- esconder cuerpo
        for i in self.cuerpo:
            i.goto(10000,10000)      # los envia a una parte de la pantalla donde no se vean    
        self.cuerpo.clear()          # elimina los egmentos de la lista

    # ------------- bucle principal del juego
    def comenzar(self):
        while True:
            self.wn.update() # actualizar
            # ------------- cambiar de lugar la manzana
            if self.cabeza.distance(self.comida) < 20:  # si la distancia es menor a 20 cambia de lugar la manzana
                x = rd.randint(-230,215)                # define zonas donde va a aparecer
                y = rd.randint(-150,155)                # se deja un margen para evitar errores
                self.comida.goto(x,y)                   # actualiza la posicion

                # ------------- agrega un cuadradito a la serpiente
                addBody = RawTurtle(self.wn)        # crea un elemento turtle
                addBody.speed(0)                    # ubica el elemento en la pantalla
                addBody.shape("square")             # le da forma de cuadrdo
                addBody.color("#BFB300")            # color de la cabeza
                addBody.penup()                     # quita el rastro al moverse
                self.cuerpo.append(addBody)         # lo agrega a la lista cuerpo
                self.score+=1
                
                # ------------- actualziar marcador
                if self.score > self.highScore:
                    self.highScore = self.score

                self.confMarcador()

            # ------------- mover cuerpo
            totalCuerpo = len(self.cuerpo)   # cuenta cantidad de cuadrados

            for i in range(totalCuerpo-1,0,-1): 
                x = self.cuerpo [i - 1].xcor()
                y = self.cuerpo [i - 1].ycor()
                self.cuerpo[i].goto(x,y)
            
            if totalCuerpo > 0:
                x = self.cabeza.xcor()
                y = self.cabeza.ycor()
                self.cuerpo[0].goto(x,y)

            # ------------- limite del mapa
            if self.cabeza.xcor() > 260 or self.cabeza.xcor() < -260 or self.cabeza.ycor() > 220 or self.cabeza.ycor() < -220:
                self.morir()

            self.mover()

            # ------------- tocar cuerpo
            for i in self.cuerpo:
                if i.distance(self.cabeza) < 20:
                    self.morir()

            time.sleep(0.1)

if __name__ == '__main__':
    root = tk.Tk()
    game = Inicio(root)
    root.mainloop()
