# przez okno po nacisnieciu przycisku "Start" zaladowac plik z komputera, zparsowac go i wyswietlic w oknie, zmieniajac liczby na pikseli
from tkinter import *
from tkinter import filedialog

from main import App


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.line = None
        self.format = None
        self.szerokosc = None
        self.wysokosc = None
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)
        # przycisk start, po nacisnieciu otwiera okno z wyborem pliku
        startButton = Button(self, text="Start", command=self.client_start)
        startButton.place(x=0, y=30)

        desaturacjaButton = Button(self, text="Desaturacja", command=self.desaturacja)
        desaturacjaButton.place(x=0, y=60)

        negatywButton = Button(self, text="Negatyw", command=self.negatyw)
        negatywButton.place(x=0, y=90)

        kontrastButton = Button(self, text="Kontrast")
        kontrastButton.place(x=0, y=120)

        jasnoscButton = Button(self, text="Jasność")
        jasnoscButton.place(x=0, y=150)

        nasycenieButton = Button(self, text="Nasycenie")
        nasycenieButton.place(x=0, y=180)

        sumaButton = Button(self, text="Suma")
        sumaButton.place(x=0, y=210)

        roznicaButton = Button(self, text="Różnica")
        roznicaButton.place(x=0, y=240)

        iloczynButton = Button(self, text="Iloczyn")
        iloczynButton.place(x=0, y=270)

        ogolneButton = Button(self, text="Ogólne")
        ogolneButton.place(x=0, y=300)

    def client_start(self):
        # otwiera okno z wyborem pliku
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("pbm files", "*.pbm"),
                                                              ("pgm files", "*.pgm"),
                                                              ("ppm files", "*.ppm"),
                                                              ("all files", "*.*")))
        #new file end with filename
        if self.filename.endswith(".pbm")  or self.filename.endswith(".pgm") or self.filename.endswith(".ppm"):
            print("OK")
        else:
            print("Error")

    def desaturacja(self):
        print("Desaturacja")

    def negatyw(self):
        print("Negatyw")

    def kontrast(self):
        print("Kontrast")

    def jasnosc(self):
        print("Jasność")

    def nasycenie(self):
        print("Nasycenie")

    def suma(self):
        print("Suma")

    def roznica(self):
        print("Różnica")

    def iloczyn(self):
        print("Iloczyn")

    def ogolne(self):
        print("Ogólne")

    def client_exit(self):
        exit()


root = Tk()
root.geometry("500x500")
app = Window(root)
root.mainloop()