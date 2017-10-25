#         _\|/_
#         (O-O)             A ver, que tenemos por aqui....
# -----oOO-(_)-OOo----------------------------------------------------

#######################################################################
# ******************************************************************* #
# *                 Juego 4 en Raya para dos jugadores              * #
# *                                                                 * #
# *                    Autor: Eulogio López Cayuela                 * #
# *                                                                 * #
# *                  Versión 2.0    Fecha: 21/07/2015               * #
# *                                                                 * #
# ******************************************************************* #
#######################################################################


# Importa las funcionalidades matematicas y en entorno gráfico Tkinter


from tkinter import *
import time



# ******************************************************************* #
# *                 definicion de algunas constantes                * #
# ******************************************************************* #

ancho_canvas = 900  # Ancho del area de dibujo
alto_canvas = 600   # Altop del area de dibujo
tamaño = 60
origen = (350,500)  # coordendas de la primera casilla (inferior izquierda)
turno = 0     # controla el turno del jugador y el color de la ficha
colores = ['red','yellow','red']
color_resaltado = 'lime'
ganador = None

xbotonera = 350     # offset eje Y para situar el origen de coordenadas
ybotonera = 75     # longitud del eje X


def reinicio():
    global tablero, columnas, ganador
    ganador = None
    columnas = [0,0,0,0,0,0,0]
    tablero = [] # lista de listas, conteniendo las filas con las fichas graficas

    for i in range (6):
        fila = [] # lista conteniendo las fichas de cada fila
        for j in range (7):
            fila.append(Casilla ('light gray',origen[0]+j*tamaño,origen[1]-i*tamaño))
        tablero.append(fila)
    regenerar_pantalla ()
    return ()


def jugada(c):
    global columnas,turno, colores, ganador
    valor_ficha =["B","A"]
    if columnas [c-1] < 6:
        turno +=1
        turno=turno%2
        tablero[columnas [c-1]][c-1].ficha = colores[turno]
        tablero[columnas [c-1]][c-1].centro = colores[turno]
        tablero[columnas [c-1]][c-1].jugador = valor_ficha[turno]        
        columnas [c-1] +=1
        comprobar_ganador('A')
        comprobar_ganador('B')
        regenerar_pantalla ()

        if ganador == 'A' or ganador == 'B':
            columnas = [9,9,9,9,9,9,9]
 
    return ()


def comprobar_ganador(x):
    '''comprobar si existen 4 elementos del mismo color en alguna
    fila, columna o diagonal'''
    global ganador
    
    '''comprobar filas'''
    for i in range (6):
        for j in range (4):        
            if tablero[i][j].jugador == x and tablero[i][j+1].jugador == x \
               and tablero[i][j+2].jugador == x and tablero[i][j+3].jugador == x:
                tablero[i][j].centro = color_resaltado
                tablero[i][j+1].centro = color_resaltado
                tablero[i][j+2].centro = color_resaltado
                tablero[i][j+3].centro = color_resaltado
                ganador = x

    '''comprobar columnas'''
    for j in range (7):
        for i in range (3):        
            if tablero[i][j].jugador == x and tablero[i+1][j].jugador == x \
               and tablero[i+2][j].jugador == x and tablero[i+3][j].jugador == x:
                tablero[i][j].centro = color_resaltado
                tablero[i+1][j].centro = color_resaltado
                tablero[i+2][j].centro = color_resaltado
                tablero[i+3][j].centro = color_resaltado
                ganador = x
        
    '''comprobar diagonales derecha'''
    for i in range (3):
        for j in range (4):
            if tablero[i][j].jugador == x and tablero[i+1][j+1].jugador == x \
               and tablero[i+2][j+2].jugador == x and tablero[i+3][j+3].jugador == x:
                tablero[i][j].centro = color_resaltado
                tablero[i+1][j+1].centro = color_resaltado
                tablero[i+2][j+2].centro = color_resaltado
                tablero[i+3][j+3].centro = color_resaltado
                ganador = x

    '''comprobar diagonales Izquierda'''
    for i in range (3):
        for j in range (3,7):
            if tablero[i][j].jugador == x and tablero[i+1][j-1].jugador == x \
               and tablero[i+2][j-2].jugador == x and tablero[i+3][j-3].jugador == x:
                tablero[i][j].centro = color_resaltado
                tablero[i+1][j-1].centro = color_resaltado
                tablero[i+2][j-2].centro = color_resaltado
                tablero[i+3][j-3].centro = color_resaltado
                ganador = x
    return()


def regenerar_pantalla ():
    '''Borra la pantalla y redibuja todas las casillas'''
    canvas.delete("all") # Borrar la pantalla
    canvas.create_text(190, 90, text="TURNO PARA", fill='Black',
                        activefill='White', font=('verdana', 10,'bold','italic'))
    canvas.create_polygon(150,150,230,150,230,100,150,100,fill=colores[turno+1]) # indicador de turno
    for i in range (6):
        for j in range (7):
            tablero[i][j].crearCasilla()
    return()


   

## ------------------------------------------------------------------------------------
##  DEFINICION DE LA CLASE << CASILLA >>
##  a la que pertenecen los segmentos que forman el robot y los objetos    
## ------------------------------------------------------------------------------------

class Casilla:
    '''Definicion de las caracteristicas basicas iniciales del hueso'''
    
    def __init__ (self, color, x,y, color1='blue2',color2='blue4'):

        self.tamaño = tamaño
        self.margen = 7
        self.ventana = self.tamaño - self.margen
        self.c = int(self.ventana/4)

        self.color = color1
        self.color_borde = color2 
        self.jugador = " "
        self.ficha = color
        self.centro = color
        self.x = x
        self.y = y

    ## ------------------------------------------------------------------------------------
    ##  Metodos a llamar para la clase CASILLA     
    ## ------------------------------------------------------------------------------------
    def crearCasilla(self):
        '''Crea una casilla a partir de los valores de entrada'''
        canvas.create_polygon(self.x,self.y, self.x + self.tamaño, self.y,
                              self.x + self.tamaño, self.y - self.tamaño,
                              self.x, self.y - self.tamaño, fill = self.color)
        canvas.create_oval (self.x+self.margen, self.y-self.margen,
                            self.x+self.ventana,self.y-self.ventana, fill=self.ficha)
        canvas.create_oval (self.x+self.margen+self.c, self.y-self.margen-self.c,
                            self.x+self.ventana-self.c,self.y-self.ventana+self.c,
                            outline=self.centro, fill=self.centro)
        
        canvas.create_line (self.x, self.y, self.x,self.y - self.tamaño, width=3,
                            fill=self.color_borde)
        canvas.create_line (self.x + self.tamaño,self.y , self.x + self.tamaño,
                            self.y-self.tamaño, width=3, fill=self.color_borde)



# ******************************************************************* #
# *                       INICIO DEL PROGRAMA                       * #
# ******************************************************************* #



    

#######################################################################
#                                                                     #
#    Crear la ventana 'ROOT' y poner nombre en la barra de titulo     #
#    dibujar elementos iniciales, ejes, brazo, etiquetas...           #
#              Es decir, creacion del entorno grafico                 #
#                                                                     #


# Crear the root window y poner nombre en la barra de titulo
root = Tk()
root.title('Juego "CONECTA 4" - Eulogio López Cayuela 2014')
# root.iconbitmap('minion02.ico')

# Tamaño y posición de la ventana principal
# pasados como parametros al constructor 'geometry'
w = 900
h = 600
px = 100
py = 10

# Ventana principal
# geometry(ancho * alto + desplazamientoX + desplazamientoY)
root.geometry("%dx%d+%d+%d" % (w, h, px, py))

# Creacion del area de dibujo
canvas = Canvas(root, width = ancho_canvas, height=alto_canvas)

# Creacion del tablero vacio de juego mediante la Class 'Casilla'
reinicio()


##########################################################
#    DISEÑO DEL ASPECTO VISUAL DE ETIQUETAS Y BOTONES    #
##########################################################


# MARCO para envolver la zona de la botonera de Colocar Ficha x = 190, y = 470)
marco02 = LabelFrame(root, text = "PULSA PARA PONER FICHA",
                     bd = 2).place(width = 495, height = 65, x = xbotonera-60, y = ybotonera-25)

# BOTONES para colocar fichas

boton_1 = Button(root,text="C1",relief = FLAT,
                 command= lambda: jugada(1))
boton_1.place(bordermode = INSIDE, width = 60, height = 30,  x = xbotonera, y = ybotonera)

boton_2 = Button(root,text = "C2",relief = FLAT,
                 command = lambda: jugada(2))
boton_2.place(bordermode = INSIDE, width = 60, height = 30,  x = xbotonera+tamaño, y = ybotonera)

boton_3 = Button(root, text = "C3",relief = FLAT,
                 command = lambda: jugada(3))
boton_3.place(bordermode = INSIDE, width = 60, height = 30,  x = xbotonera+tamaño*2, y = ybotonera)

boton_4 = Button(root,text = "C4",relief = FLAT,
                 command = lambda: jugada(4))
boton_4.place(bordermode = INSIDE, width = 60, height = 30,  x = xbotonera+tamaño*3, y = ybotonera)

boton_5 = Button(root, text = "C5",relief = FLAT,
                 command = lambda: jugada(5))
boton_5.place(bordermode = INSIDE, width = 60, height = 30,  x = xbotonera+tamaño*4, y = ybotonera)

boton_6 = Button(root, text = "C6",relief = FLAT,
                 command = lambda: jugada(6))
boton_6.place(bordermode = INSIDE, width = 60, height = 30,  x = xbotonera+tamaño*5, y = ybotonera)

boton_7 = Button(root, text = "C7",relief = FLAT,
                 command = lambda: jugada(7))
boton_7.place( width = 60, height = 30,  x = xbotonera+tamaño*6, y = ybotonera)

# REINICIAR, Boton para reiniciar la aplicación
boton_0 = Button(root, text = "ReiniciaR",fg = "white", bg = "orange", command= lambda:reinicio())
boton_0.place(bordermode = INSIDE, width = 120, height = 30,  x= 600, y = 550)


# SALIR, Boton para salir de la aplicación
boton_0 = Button(root, text = "SALIR",fg = "white", bg = "Blue", command=root.destroy)
boton_0.place(bordermode = INSIDE, width = 120, height = 30,  x= 740, y = 550)


    
# Visualizar area de dibujo
canvas.pack()

# ******************************************************************* #
#              FIN de la creacion del entorno grafico                 #
# ******************************************************************* #

# Atender eventos
root.mainloop()

#######################################################################
#                                                                     #
#                           FIN DEL PROGRAMA                          #
#                                                                     #
#######################################################################


