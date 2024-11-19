import tkinter as tk
import myApp

screen = tk.Tk()

screen.title("Tops musics")

screen.geometry('400x400')

logo_path = r'images/logo.ico'

screen.iconbitmap(logo_path)

# tk.Label(screen, text='Musics System').grid(row=0, column=0)
# tk.Label(screen, text='Musics System').pack(side='left')
# tk.Label(screen, text='Musics System').place(x=10, y=100)

tk.Label(screen, text='Musics System', bg='#77a8a8').pack()

musicList = tk.Listbox(screen, width=100, bg='#dbceb0')

for m in myApp.musics_list:
    musicList.insert(1, m)

musicList.pack()

def playMusic():
    print("Playing music...")
    myApp.randomMusics()

tk.Button(screen, text="Play", fg='#587e76', command=playMusic).pack()

screen.mainloop()