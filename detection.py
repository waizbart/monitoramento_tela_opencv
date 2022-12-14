import pyautogui, cv2
import numpy as np
from grab import grab
import threading
from time import sleep
from decision_ia import insect_choice

stop_thread = False

class clipboardThread(threading.Thread):
    def __init__(self, args):
        threading.Thread.__init__(self)
        self.args = args

        return
    def run(self):
        print("Iniciando monitoramento")
        x1, y1, x2, y2 = self.args
        inspect_insects(x1, y1, x2, y2)


def inspect_insects(x1, y1, x2, y2):
    global stop_thread

    stop_thread = False

    while True:
        try:
            print("Monitorando: ", not stop_thread)

            if stop_thread:
                stop_thread = False
                break

            insetos=[]

            centerAbelha = pyautogui.locateCenterOnScreen("assets/insetos/abelha.png", confidence=0.8, region=(x1, y1, x2, y2))

            if centerAbelha != None:
                insetos.append({"insect": "abelha", "center": centerAbelha})
                
            centerMosca = pyautogui.locateCenterOnScreen("assets/insetos/mosca.png", confidence=0.8, region=(x1, y1, x2, y2))

            if centerMosca != None:
                insetos.append({"insect": "mosca", "center": centerMosca})
                
            centerFormiga = pyautogui.locateCenterOnScreen("assets/insetos/formiga.png", confidence=0.8, region=(x1, y1, x2, y2))

            if centerFormiga != None:
                insetos.append({"insect": "formiga", "center": centerFormiga})
                
            print(insetos)

            if insetos != []:
                decision = insect_choice(insetos)
                print(decision, "decide")
                pyautogui.moveTo(pyautogui.locateCenterOnScreen("assets/botoes/" + decision + "_btn.png", confidence=0.8))
                pyautogui.click()
                sleep(1.2)

        except Exception as e:
            print("Erro no monitoramento", e)
            stop_thread = False
            break
            

def stop_thread_fn():
    global stop_thread
    stop_thread = True

def process_image(filename, x1, y1, x2, y2): 
    found = False 
    while not found:
        if pyautogui.locateOnScreen(filename, confidence=0.8, region=(x1, y1, x2, y2)) != None:
            print("Imagem ", filename, " na tela")
            found = True


def match_image(filename, x1, y1, x2, y2):
    grab(x1, y1, x2, y2, 'screenshot.png')
    
    image = cv2.imread('screenshot.png')
    template = cv2.imread(filename)
    heat_map = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    print(heat_map)
    y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)

    print(x, y)