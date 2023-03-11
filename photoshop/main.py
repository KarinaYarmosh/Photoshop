import tkinter as tk
from pnm.pbm import PBMImage
from pnm.pgm import PGMImage
from pnm.ppm import PPMImage

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        #self.create_widgets() przekazanie argumentu filename z main_window.py do create_widgets
        self.create_widgets("test_raw.pbm")

    def create_widgets(self, filename):
        # Create a canvas widget
        self.canvas = tk.Canvas(self, width=500, height=500)
        #add to center
        self.canvas.pack()

        # Load the image file
        #filename = "test_raw.pbm"
        #filename = "test_raw.pbm"
        image = None
        if filename.endswith(".pbm"):
        #if filename.endswith(".txt"):
            image = PBMImage(filename)
        elif filename.endswith(".pgm"):
            image = PGMImage(filename)
        elif filename.endswith(".ppm"):
            image = PPMImage(filename)

        # Draw the image on the canvas
        image.get_pixel(0, 0)
        #print(image.data)
        for i in range(image.height):
            for j in range(image.width):
                print(int(image.get_pixel(j, i)))
                if image.get_pixel(j, i):
                    self.canvas.create_rectangle(
                        j, i, j, i, fill="black", outline=""
                    )
                else:
                    self.canvas.create_rectangle(
                        j, i, j, i, fill="white", outline=""
                    )

root = tk.Tk()
app = App(master=root)
app.mainloop()