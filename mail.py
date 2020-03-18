from tkinter import *
import time
import random
def color_mixer():
    g_int = random.randint(1, 255)
    b_int = random.randint(1, 255)
    r_int = random.randint(1, 255)
    
    g_rate = random.randint(1, 10)
    b_rate = random.randint(1, 10)
    r_rate = random.randint(1, 10)
    
    g_dir = random.choice([1, -1])
    b_dir = random.choice([1, -1])
    r_dir = random.choice([1, -1])
    
    while True: 
        if (g_int + g_rate) * g_dir > 255 or g_int + (g_rate * g_dir) < 0:
            g_dir = g_dir * -1
        if (b_int + b_rate) * b_dir > 255 or b_int + (b_rate * b_dir) < 0:
            b_dir = b_dir * -1
        if (r_int + r_rate) * r_dir > 255 or r_int + (r_rate * r_dir) < 0:
            r_dir = r_dir * -1

        g_int += g_dir * g_rate
        b_int += b_dir * b_rate
        r_int += r_dir * r_rate

        yield g_int, b_int, r_int




class alien(object):
     def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=512, height = 512)
        self.canvas.pack()
        self.bg = self.canvas.create_rectangle(0, 0, 512, 512, fill='black')

        self.hello = self.canvas.create_oval(128, 128, 512 - 128, 512 - 128, outline='white',         fill='blue')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

     def change_circle_size(self, radius):
         self.canvas.coords(self.hello, 256 - radius, 256 - radius, 256 + radius, 256 + radius)
         self.canvas.update()
     def animation(self):
        colors = ["red", "orange", "yellow", "green", "blue", "violet"]
        palate = color_mixer()
        self.canvas.update()






        while True:
            print(palate.__next__())

            for x in range(random.randint(1, 100)):

                time.sleep(0.0125)
                self.canvas.itemconfig(self.bg, fill='#%02x%02x%02x' % palate.__next__())
                self.change_circle_size(x)
            for x in range(random.randint(1, 100)):
                time.sleep(0.0125)
                self.canvas.itemconfig(self.bg, fill='#%02x%02x%02x' % palate.__next__())

                self.change_circle_size(100 - x)
            self.canvas.itemconfig(self.hello, fill=random.choice(colors))
alien()