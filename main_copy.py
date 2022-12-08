import pyautogui, cv2
import pyscreenshot as pys
from time import sleep
import os

pyautogui.hotkey('win','r')
sleep(2)
pyautogui.write('chrome')
pyautogui.hotkey('enter')
sleep(2)

# neobux
pyautogui.write('neobux.com')
pyautogui.hotkey('enter')
sleep(4)
pyautogui.click(pyautogui.locateCenterOnScreen('ver.png'),interval=1.0)
pyautogui.scroll(-200)
sleep(3)

while pyautogui.locateOnScreen('estrela.png') != None:
    x2, y2 = pyautogui.locateCenterOnScreen('estrela.png')
    pyautogui.click(x2, y2, interval=1.0)
    sleep(0.5)
    img = pys.grab(bbox=(x2-300,y2-200,x2+50,y2))
    img.save('scr.png')
    img = cv2.imread('scr.png')
    img_cinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(img_cinza, (1,1), 2)
    circulo = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 300, param1=100, param2=30, minRadius=5, maxRadius=10)
    [[[x, y, z]]] = circulo
    pyautogui.click((x2-300+x), (y2-200+y), interval=1.0)
    sleep(2)
    flag = True
    while flag:
        sinal = pyautogui.locateOnScreen('sinal.png')
        if sinal != None:
            sleep(1)
            pyautogui.hotkey('ctrl','F4')
            flag = False

    os.remove('scr.png')

flag2 = True
x, y = pyautogui.locateCenterOnScreen('ad.png')
pyautogui.click(x, y+40, interval=1.0)
while flag2:
    while pyautogui.locateOnScreen('prox.png') == None:
        ...
    sleep(0.7)
    pyautogui.click(pyautogui.locateCenterOnScreen('prox.png'), interval=1.0)


pyautogui.hotkey('ctrl', 'F4')