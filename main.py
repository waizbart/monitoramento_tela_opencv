import pyscreenshot as ImageGrab
import os
from pynput.mouse import Listener
import sys
import tkinter as tk
from PIL import Image
from io import BytesIO
from time import sleep
 
click1 = 0
x1 = 0
y1 = 0
 
def grab(x, y, w, h):
    im = ImageGrab.grab(bbox=(x, y, w, h))
    im.save('im.png')
    image = Image.open("im.png")
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    output.close()


def on_click(x, y, button, pressed):
    global click1, x1, y1, listener
    
    print(x, y, button)
    if pressed:
        if click1 == 0:
            x1 = x
            y1 = y
            click1 = 1
        else:
            grab(x1, y1, x, y)
            listener.stop()
            x1 = 0
            y2 = 0
            click1=0
            sys.exit()

    sleep(0.1)
def start():
    global listener
 
    print("Clique uma vez no canto superior esquerdo e outra no inferior direito")
    with Listener(on_click=on_click) as listener:
        listener.join()
 
root = tk.Tk()
root.geometry("400x600")
but = tk.Button(root, text="GRAB GET IMAGE", command=start, width=20,height=10, bg="gold")
but.pack()
 
root.mainloop()