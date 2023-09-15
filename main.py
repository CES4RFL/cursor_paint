from tkinter import *

class main:
    def __init__(self,master):
        #Inicializa variables dentro del scope del contexto de la clase
        #Inicializa el wrapper que contendra todos los elementos de tkinter
        self.master = master
        #Inicializa variables que contienen el color del canvas y de las lineas
        self.color_fg = 'blue'
        self.color_bg = 'white'
        #Declara las variables que contendran los valores anteriores del cursor
        #Son necesarios para obtener las cordenas de inicio de la linea
        self.old_x = None
        self.old_y = None
        #Inicializa variable que contiene el grosor de la linea que se marca en el canvas
        self.penwidth = 3
        #Llamada al metodo que crea el canvas
        self.createCanvas()
        #Bindigs de eventos dentro del canvas
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)
        #Bindings de eventos dentro del wrapper de tkinter
        self.master.bind('<space>',self.clear)

    def paint(self,e):
        #Valida si ambas variables estan declaradas e incializadas
        if self.old_x and self.old_y:
            #Lammada al metodo create_line del canvas este nos ayudara a pintar la linea dentro del canvas
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

        #Finalmente obtiene del evento las cordenadas y y x del cursor dentro del canvas
        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):
        #Una ves que suelta el boton de click derecho, se reinicia el valor de las variables para recibir en el proximo
        #vento los nuevos valores del cursos e identificar de que cordenada partir
        self.old_x = None
        self.old_y = None        

    def clear(self,e):
        #Funcion del canvas borra todos los elementos creados
        #Fue utilizado para borrar las lineas
        self.c.delete('all')

    def createCanvas(self):
        #Crea el canvas
        self.c = Canvas(self.master,width=500,height=500,bg=self.color_bg)
        self.c.pack(fill=BOTH,expand=True)

        #Inicializa la variable con las instrucciones de borrado
        self.label=Label(self.master, text="Presiona la barra espaciadora para limpiar la pantalla")
        self.label.pack()
        

if __name__ == '__main__':
    #Codigo principal para el inicio del programa
    root = Tk()
    main(root)
    root.title('Aplicacion para dibujar en un canvas con el cursor')
    root.mainloop()
