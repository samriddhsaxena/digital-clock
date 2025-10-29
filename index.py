import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.resizable(False, False)

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root,font=('calibri',50,'bold'),background='black',foreground='white')
label.pack(anchor='center')
time()

root.mainloop()