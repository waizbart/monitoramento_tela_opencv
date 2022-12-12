import pyautogui, cv2

def process_image(filename, x1, y1, x2, y2): 
    found = False 
    while not found:
        if pyautogui.locateOnScreen(filename, confidence=0.8, region=(x1, y1, x2, y2)) != None:
            print("Imagem ", filename, " na tela")
            found = True


