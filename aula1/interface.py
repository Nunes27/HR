import tkinter as tk
import random

root = tk.Tk()
root.geometry('200x200')

def houver(event):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    nao.place(x=x, y=y)

def mensagem():
    message = tk.Label(root, text='Love u S2')
    message.place(x=7, y=120, relx=0, rely=0)

pergunta = tk.Label(root, text='quer viver um romace boiola comigo?')
pergunta.pack(anchor='n', padx=20)

nao = tk.Button(root, text='Não')
nao.place(x=140, y=80)
nao.bind('<Enter>', houver)

sim= tk.Button(root, text='Sim', command=mensagem)
sim.place(x=25,y=80, relx=0, rely=0)

root.mainloop()