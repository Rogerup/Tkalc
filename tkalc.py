from tkinter import *

def bt_draw(key, col, lin):
    bt = Button(window, text=key, command=lambda: bt_press(key))
    bt.grid(column=col+1, row=lin+1)
    return bt

def bt_press(key):
    if   key == 'C': disp['text'] = ''
    elif key == '<': disp['text'] = disp['text'][:-1]
    elif key == '=': disp['text'] = str(round(eval(disp['text']),6))
    else           : disp['text'] += key

window = Tk()
window.title('Tkalc')

disp = Label(window, text='')
disp.grid(column=0, row=0, columnspan=5)

keys = '()C<789/456*123-.0=+'
bt_list = [bt_draw(keys[n], n%4, n//4) for n in range(20)]

window.mainloop()