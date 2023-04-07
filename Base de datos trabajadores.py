from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser as colorchooser 

root=Tk()
root.title("ventana de horarios de trabajo")
root.geometry("500x300")
root.config(bg="teal")

boton=Button(root,text="ventana de horarios de trabajo",width=30,height=5)

root.mainloop()

# Creamos una clase 
class App():
    #Metodo es constructor
    def __init__(self):
        #creamos el objeto de tipo Tkinter 
        ventanas=Tk()
        ventanas.title("Ventana principal")
        ventanas.geometry("400x400")
        

        #widgets
        self.Iabel1=Label(ventanas, text="nombre") 
        self.Iabel1.place(x=40,y=30)
        self.text1=Entry(ventanas,)
        self.text1.place(x=100,y=30)

        #Boton
        self.bt1=Button(ventanas, text="Aceptar", command=self.mensaje)
        self.bt1.place(x=60, y=80)


        

        ventanas.mainloop()
    def mensaje(self):
            #print("su horarios son los siguientes")
            messagebox.showinfo(message="estos son su horarios"+ self.text1.get(), title="Ejemplo")


# programa principal 
objet_ventanas =App()
        