import tkinter as tk

def key_handler(event=None):
    if event and event.keysym == 'p':
        print('You pressed the {} key'.format(event.keysym))
    if event and event.keysym == 'm':
        print('You pressed the {} key'.format(event.keysym))


r = tk.Tk()
t = tk.Text()
t.pack()
r.bind('<Key>', key_handler)
r.mainloop()