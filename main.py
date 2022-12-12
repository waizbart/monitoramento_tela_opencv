import tkinter as tk
from grab import start_grab, grab
from detection import process_image

x1 = 0
y1 = 0
x2 = 0
y2 = 0

def set_capture_area():
    global x1, y1, x2, y2
    print("Clique uma vez no canto superior esquerdo e outra no inferior direito da área a ser monitorada")
    x1, y1, x2, y2 = start_grab()
    print("X1: " + str(x1) + " Y1: " + str(y1) + "\nX2: " + str(x2) + " Y2: " + str(y2) + "\n")

def grab_target_obj():
    x1, y1, x2, y2 = start_grab()
    grab(x1, y1, x2, y2)

def init_inspector():
    global x1, y1, x2, y2
    process_image("target.png", x1, y1, x2, y2)

root = tk.Tk(baseName="root")

root.geometry("400x600")
root.title("Inspetor de insetos")
root.configure(background='#262626')

cap_select_btn = tk.Button(root, text="SELECIONAR ÁREA DE CAPTURA", command=set_capture_area, width=40, height=2, bg="#4F4D8C", activebackground="#8F8EBF", fg="white")
target_select_btn = tk.Button(root, text="SELECIONAR OBJETO ALVO", command=grab_target_obj, width=40, height=2, bg="#4F4D8C", activebackground="#8F8EBF", fg="white")
init_btn = tk.Button(root, text="INSPECIONAR", command=init_inspector, width=40, height=2, bg="#5F5DA6", activebackground="#8F8EBF", fg="white")
#stop_btn = tk.Button(root, text="PARAR", command=print_coords, width=40, height=2, bg="#2E4159", activebackground="#8F8EBF", fg="white")

cap_select_btn.pack(pady=10, padx=10)
target_select_btn.pack(pady=10, padx=10)
init_btn.pack(pady=10, padx=10)
 
root.mainloop()