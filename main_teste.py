import pyautogui, cv2

while True:
    if pyautogui.locateOnScreen('assets/Abelha.png', confidence=0.4) != None:
        print("abelha")

    if pyautogui.locateOnScreen('assets/formiga.png', confidence=0.4) != None:
        print("formiga")

    if pyautogui.locateOnScreen('assets/mosca.png', confidence=0.4) != None:
        print("mosca")

    if pyautogui.locateOnScreen('assets/joaninha.png', confidence=0.4) != None:
        print("joaninha")


