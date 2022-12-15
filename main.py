import tkinter as tk
from grab import start_grab, grab
from detection import clipboardThread, stop_thread_fn

x1 = 0
y1 = 0
x2 = 0
y2 = 0

def set_capture_area():
    global x1, y1, x2, y2
    print("Clique uma vez no canto superior esquerdo e outra no inferior direito da área a ser monitorada")
    x1, y1, x2, y2 = start_grab()
    print("X1: " + str(x1) + " Y1: " + str(y1) + "\nX2: " + str(x2) + " Y2: " + str(y2) + "\n")

    inputX1.delete('1.0', "end")
    inputY1.delete('1.0', "end")
    inputX2.delete('1.0', "end")
    inputY2.delete('1.0', "end")

    inputX1.insert('1.0', str(x1))
    inputY1.insert('1.0', str(y1))
    inputX2.insert('1.0', str(x2))
    inputY2.insert('1.0', str(y2))


def init_inspector():
    global x1, y1, x2, y2

    clipboardThread.daemon=True
    thread = clipboardThread(args=(x1, y1, x2, y2))
    thread.start()

    init_btn["text"] = "EXECUTANDO..."
    init_btn["state"] = "disabled"


def stop_inspect():
    print("parando")

    stop_thread_fn()

    init_btn["text"] = "INSPECIONAR"
    init_btn["state"] = "normal"

def set_inputed_points():
    global x1, y1, x2, y2

    print(x1, y1, x2, y2)

    x1 = int(inputX1.get("1.0","end-1c"))
    y1 = int(inputY1.get("1.0","end-1c"))
    x2 = int(inputX2.get("1.0","end-1c"))
    y2 = int(inputY2.get("1.0","end-1c"))

    print(x1, y1, x2, y2)


root = tk.Tk(baseName="root")

root.geometry("400x400")
root.title("Inspetor de insetos")
root.configure(background='#262626')

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)

cap_select_btn = tk.Button(root, text="SELECIONAR ÁREA DE CAPTURA", command=set_capture_area, width=40, height=2, bg="#4F4D8C", activebackground="#8F8EBF", fg="white")
cap_select_btn.grid(columnspan = 3, sticky = tk.W+tk.E, pady=10, padx=10)

lbX1 = tk.Label(root, text = "X1: ", background='#262626', foreground="white")
lbX1.grid(column=0, row=1)
inputX1 = tk.Text(root, height = 1, width = 5)
inputX1.grid(column=0, row=2)

lbY1 = tk.Label(root, text = "Y1: ", background='#262626', foreground="white")
lbY1.grid(column=2, row=1)
inputY1 = tk.Text(root, height = 1, width = 5)
inputY1.grid(column=2, row=2)

points_input_btn = tk.Button(root, text="SALVAR PONTOS", command=set_inputed_points, width=-10, bg="#4F4D8C", activebackground="#8F8EBF", fg="white")
points_input_btn.grid(column=1, pady=10, padx=10)

lbX2 = tk.Label(root, text = "X2: ", background='#262626', foreground="white")
lbX2.grid(column=0, row=4)
inputX2 = tk.Text(root, height = 1, width = 5)
inputX2.grid(column=0, row=5)

lbY2 = tk.Label(root, text = "Y2: ", background='#262626', foreground="white")
lbY2.grid(column=2, row=4)
inputY2 = tk.Text(root, height = 1, width = 5)
inputY2.grid(column=2, row=5)

init_btn = tk.Button(root, text="INSPECIONAR", command=init_inspector, width=40, height=2, bg="#2E4159", activebackground="#8F8EBF", disabledforeground="yellow", fg="white")
init_btn.grid(columnspan = 3, sticky = tk.W+tk.E, pady=15, padx=10)

stop_btn = tk.Button(root, text="PARAR", command=stop_inspect, width=40, height=2, bg="#6C0E23", activebackground="#ED6A5A", fg="white")
stop_btn.grid(columnspan = 3, sticky = tk.W+tk.E, pady=10, padx=10)
 
root.mainloop()