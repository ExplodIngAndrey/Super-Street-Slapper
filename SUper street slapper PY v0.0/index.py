from tkinter import *
import time
import json
import sys
gamerunning = True
tk = Tk()
tk.title('SUper street slapper v0.0')
window = Canvas(tk, width=500, height = 250/1.7)
window.pack()
img = PhotoImage(file='load.gif')
player = PhotoImage(file='player.gif')
enemy = PhotoImage(file='enemy.gif')
def image():
        window.create_image(0,0,image=img, anchor='nw')
        print('image called')
    
def text(ttr):
    window.create_text(80,10,text= ttr, font=('courier',20))
    print('text called')
    
image()
text('Loading...')
def clear():
    window.delete('all')
    print('clear called')
    
def __init__():
    global img
    img = PhotoImage(file="game.gif")
    clear()
    image()
    button = Button(tk,text='Play!',command=initgame)
    button.pack()
    print('init called')
tk.after(5000, __init__) 
def renderAll(playerX, enemyX):
        window.create_image(playerX,0,image=player, anchor='nw')
        window.create_image(enemyX,0,image=enemy, anchor='nw')
def loop():
        img = PhotoImage(file="game.gif")
        clear()
        image()
        renderAll(x, enemyx)
        tk.after(10,loop)
        print('loop called')

def initgame():
        #eat
        global x
        global enemyx
        x=0
        enemyx = 100
        loop()
        print('initgame run')
def moveleft(event):
        global x
        x-=10
def moveright(event):
        global x
        x+=10
window.bind_all('<KeyPress-Left>',moveleft)
window.bind_all('<KeyPress-Right>',moveright)
tk.mainloop()        
