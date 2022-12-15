import pyscreenshot as ImageGrab
from pynput.mouse import Listener
import sys

click1 = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
 
def grab(x, y, w, h, filename):
    try:
        im = ImageGrab.grab(bbox=(x, y, w, h))
        im.save(filename)

    except Exception as e:
        print("Error: ", e)


def on_click(x, y, button, pressed):
    global click1, x1, y1, x2, y2, listener
    
    if pressed:
        if click1 == 0:
            x1 = x
            y1 = y
            click1 = 1
            return
        else:
            x2 = x
            y2 = y

            if x2 <= x1 or y2 <= y1:
                print('Erro: x2 <= x1 ou y2 <= y1')
                x1, y1, x2, y2 = [0, 0, 0, 0]

            listener.stop()
            click1 = 0
            sys.exit()

def start_grab():
    global listener

    with Listener(on_click=on_click) as listener:
        listener.join()

    return [x1, y1, x2, y2]