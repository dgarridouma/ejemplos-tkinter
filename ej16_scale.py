import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="[Valor escala]")
        self.label1.grid(column=0, row=0, padx=10, pady=10)

        self.scale = tk.Scale(self.ventana1, from_=0, to=99, orient=tk.HORIZONTAL, command=self.update_label)
        self.scale.grid(column=0, row=1, sticky='we')

        self.ventana1.mainloop()


    def update_label(self,event):
        self.label1.configure(text = str(self.scale.get()))

aplicacion1=Aplicacion() 