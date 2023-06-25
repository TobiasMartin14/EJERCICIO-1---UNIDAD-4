from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana = None
    __vCant  = None
    __vPAB = None
    __vPAA =  None
    __aCant = None
    __aPAB = None
    __aPAA = None
    __eCant = None
    __ePAB = None
    __ePAA =  None
    __porcentaje = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x250')
        self.__ventana.title('Calculadora IPC')
        mainframe = ttk.Frame(self.__ventana, padding = "3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__vCant = StringVar()
        self.__vPAB = StringVar()
        self.__vPAA = StringVar()
        self.__aCant = StringVar()
        self.__aPAB = StringVar()
        self.__aPAA = StringVar()
        self.__eCant = StringVar()
        self.__ePAB = StringVar()
        self.__ePAA = StringVar()
        self.__porcentaje = StringVar()

        ttk.Label(mainframe, text="Item").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text="Cantidad").grid(column=2, row=1, sticky=W)
        ttk.Label(mainframe, text="Precio año base").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="Precio Año Actual").grid(column=4, row=1, sticky=W)
        ttk.Label(mainframe, text="Vestimenta").grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text="Alimentos").grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text="Educación").grid(column=1, row=4, sticky=W)
        self.vCantEntry = ttk.Entry(mainframe, width=7, textvariable=self.__vCant)
        self.vCantEntry.grid(column=2, row=2, sticky=(W, E))
        self.vPABEntry = ttk.Entry(mainframe, width=7, textvariable=self.__vPAB)
        self.vPABEntry.grid(column=3, row=2, sticky=(W, E))
        self.vPAAEntry = ttk.Entry(mainframe, width=7, textvariable=self.__vPAA)
        self.vPAAEntry.grid(column=4, row=2, sticky=(W, E))
        self.aCantEntry = ttk.Entry(mainframe, width=7, textvariable=self.__aCant)
        self.aCantEntry.grid(column=2, row=3, sticky=(W, E))
        self.aPABEntry = ttk.Entry(mainframe, width=7, textvariable=self.__aPAB)
        self.aPABEntry.grid(column=3, row=3, sticky=(W, E))
        self.aPAAEntry = ttk.Entry(mainframe, width=7, textvariable=self.__aPAA)
        self.aPAAEntry.grid(column=4, row=3, sticky=(W, E))
        self.eCantEntry = ttk.Entry(mainframe, width=7, textvariable=self.__eCant)
        self.eCantEntry.grid(column=2, row=4, sticky=(W, E))
        self.ePABEntry = ttk.Entry(mainframe, width=7, textvariable=self.__ePAB)
        self.ePABEntry.grid(column=3, row=4, sticky=(W, E))
        self.ePAAEntry = ttk.Entry(mainframe, width=7, textvariable=self.__ePAA)
        self.ePAAEntry.grid(column=4, row=4, sticky=(W,E))

        ttk.Label(mainframe, textvariable=str(self.__porcentaje)).grid(column=2, row=6, sticky=(W, E))
        ttk.Button(mainframe, text="Calcular IPC", command=self.calcular).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=4, row=5, sticky=W)
        ttk.Label(mainframe, text="IPC %").grid(column=1, row=6, sticky=W)
        ttk.Label(mainframe, text="%").grid(column=3, row=6, sticky=W)


        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.vCantEntry.focus()
        self.__ventana.mainloop()
    
    def calcular(self):
        try:
            cantV = int(self.vCantEntry.get())
            cantA = int(self.aCantEntry.get())
            cantE = int(self.eCantEntry.get())
            baseV = int(self.vPABEntry.get())
            baseA = int(self.aPABEntry.get())
            baseE = int(self.ePABEntry.get())
            actualV = int(self.vPAAEntry.get())
            actualA = int(self.aPAAEntry.get())
            actualE = int(self.ePAAEntry.get())
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        
        costo_base = (cantA * baseA) + (cantV * baseV) + (cantE * baseE)
        costo_actual = (cantA * actualA) + (cantV * actualV) + (cantE * actualE)

        ipc = (costo_actual / costo_base)
        ipc = ipc - int(ipc)
        ipc = ipc * 100
        self.__porcentaje.set(round(ipc, 2))

def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()
