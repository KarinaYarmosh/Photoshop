# przez okno po nacisnieciu przycisku "Start" zaladowac plik z komputera, zparsowac go i wyswietlic w oknie, zmieniajac liczby na pikseli

import aspose.words as aw
import numpy as np
from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
import cv2

from image_window import App
from point_operations.brightness import brightness
from point_operations.contrast import contrast
from point_operations.desaturation import desaturation
from point_operations.multiplication import image_mul
from point_operations.negative import neg
from point_operations.saturation import saturation
from point_operations.substract import image_sub
from point_operations.sum import image_sum
from pnm.pbm import PBMImage
from pnm.pgm import PGMImage
from pnm.ppm import PPMImage


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.line = None
        self.format = None
        self.szerokosc = None
        self.wysokosc = None
        self.master = master
        self.filename = None
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)
        # przycisk start, po nacisnieciu otwiera okno z wyborem pliku
        startButton = Button(self, text="Start", command=self.client_start)
        startButton.place(x=0, y=30)

        desaturacjaButton = Button(self, text="Desaturacja", command=lambda: self.desaturacja())
        desaturacjaButton.place(x=0, y=60)

        negatywButton = Button(self, text="Negatyw", command=lambda: self.negatyw())
        negatywButton.place(x=0, y=90)

        kontrastButton = Button(self, text="Kontrast", command=lambda: self.kontrast())
        kontrastButton.place(x=0, y=120)

        jasnoscButton = Button(self, text="Jasność", command=lambda: self.jasnosc())
        jasnoscButton.place(x=0, y=150)

        nasycenieButton = Button(self, text="Nasycenie", command=lambda: self.nasycenie())
        nasycenieButton.place(x=0, y=180)

        sumaButton = Button(self, text="Suma", command=lambda: self.suma())
        sumaButton.place(x=0, y=210)

        roznicaButton = Button(self, text="Różnica", command=lambda: self.roznica())
        roznicaButton.place(x=0, y=240)

        iloczynButton = Button(self, text="Iloczyn", command=lambda: self.iloczyn())
        iloczynButton.place(x=0, y=270)

        ogolneButton = Button(self, text="Ogólne", command=lambda: self.ogolne())
        ogolneButton.place(x=0, y=300)

        jpegButton = Button(self, text="JPEG", command=lambda: self.jpeg())
        jpegButton.place(x=0, y=330)

        obrazLabel = Label(self, text="Obraz nie jest zaladowany")
        obrazLabel.place(y = 30, x = 50)


        self.kontrastEntry = Entry(self)
        self.kontrastEntry.place(y = 120, x = 100)
        kontrastLabel = Label(self, text="Podaj wartosc kontrastu")
        kontrastLabel.place(y = 120, x = 200)
        self.jasnoscEntry = Entry(self)
        self.jasnoscEntry.place(y = 150, x = 100)
        jasnoscLabel = Label(self, text="Podaj wartosc jasnosci")
        jasnoscLabel.place(y = 150, x = 200)
        self.nasycenieEntry = Entry(self)
        self.nasycenieEntry.place(y = 180, x = 100)
        nasycenieLabel = Label(self, text="Podaj wartosc nasycenia")
        nasycenieLabel.place(y = 180, x = 200)


    def client_start(self):
        # otwiera okno z wyborem pliku
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("pbm files", "*.pbm"),
                                                              ("pgm files", "*.pgm"),
                                                              ("ppm files", "*.ppm"),
                                                              ("all files", "*.*")))

        self.zaladowany_obraz(self.filename)

        if self.filename.split(".")[-1] == "pbm":
            self.file = PBMImage(self.filename)
        elif self.filename.split(".")[-1] == "pgm":
            self.file = PGMImage(self.filename)
        elif self.filename.split(".")[-1] == "ppm":
            self.file = PPMImage(self.filename)
        #self.open_image_in_new_window(self.filename)

    def zaladowany_obraz(self, filename):
        if filename != None:
            obrazLabel = Label(self, text="Obraz jest zaladowany")
            obrazLabel.place(y=30, x=50)
        else:
            obrazLabel = Label(self, text="Obraz nie jest zaladowany")
            obrazLabel.place(y=30, x=50)

    def open_image_in_new_window(self, filename):
        window = App(filename)
        window.grab_set()

    def desaturacja(self):
        self.zaladowany_obraz(self.filename)
        image = desaturation(self.file)
        image.save("desaturacja.pgm")
        self.open_image_in_new_window("desaturacja.pgm")

    def negatyw(self):
        self.zaladowany_obraz(self.filename)
        image = neg(self.file)
        image.save("negatyw" + "." + self.filename.split(".")[-1])
        self.open_image_in_new_window("negatyw" + "." + self.filename.split(".")[-1])

    def kontrast(self):
        self.zaladowany_obraz(self.filename)
        if self.kontrastEntry.get().isdigit():
            image = contrast(self.file, float(self.kontrastEntry.get()))
            image.save("kontrast" + "." + self.filename.split(".")[-1])
            self.open_image_in_new_window("kontrast" + "." + self.filename.split(".")[-1])

    def jasnosc(self):
        self.zaladowany_obraz(self.filename)
        if self.jasnoscEntry.get().isdigit():
            image = brightness(self.file, float(self.jasnoscEntry.get()))
            image.save("jasnosc" + "." + self.filename.split(".")[-1])
            self.open_image_in_new_window("jasnosc" + "." + self.filename.split(".")[-1])

    def nasycenie(self):
        self.zaladowany_obraz(self.filename)
        if self.nasycenieEntry.get().isdigit():
            image = saturation(self.file, float(self.nasycenieEntry.get()))
            image.save("nasycenie" + "." + self.filename.split(".")[-1])
            self.open_image_in_new_window("nasycenie" + "." + self.filename.split(".")[-1])

    def suma(self):
        self.zaladowany_obraz(self.filename)
        image = image_sum(self.file, self.file)
        image.save("suma" + "." + self.filename.split(".")[-1])
        self.open_image_in_new_window("suma" + "." + self.filename.split(".")[-1])

    def roznica(self):
        self.zaladowany_obraz(self.filename)
        image = image_sub(self.file, self.file)
        image.save("roznica" + "." + self.filename.split(".")[-1])
        self.open_image_in_new_window("roznica" + "." + self.filename.split(".")[-1])

    def iloczyn(self):
        self.zaladowany_obraz(self.filename)
        image = image_mul(self.file, self.file)
        image.save("iloczyn" + "." + self.filename.split(".")[-1])
        self.open_image_in_new_window("iloczyn" + "." + self.filename.split(".")[-1])

    def jpeg(self):
        print("jpeg")
        #nazwa - "jpg-vs-jpeg.jpg"
        girl = cv2.imread("jpg-vs-jpeg.jpg")
        cv2.imshow("girl", girl)
        plt.hist(girl.revel, 256, [0,255])



    def histogram(self):
        print("histogram")

    def ogolne(self):
        print("Ogólne")

    def client_exit(self):
        self.zaladowany_obraz(self.filename)
        exit()


root = Tk()
root.geometry("500x500")
app = Window(root)
root.mainloop()
