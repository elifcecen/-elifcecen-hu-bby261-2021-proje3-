from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.geometry("490x600")

kapaklar = ["otel_1.png","otel_2.png", "otel_3.png"]

kapak = 0

def goster():
    gorsel = ImageTk.PhotoImage(Image.open(kapaklar[kapak]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=3, padx= 10, pady=10)

goster()

def ileri():
    global kapak
    if kapak < len(kapaklar)-1:
        kapak +=1
    else:
        kapak = 0
    print(kapak)

    goster()

buton = Button(text="Sonraki", command=ileri)
buton.grid(row=2, column=2, padx= 10, pady=10)
buton.config(font=("Arial", 20))

def geri():
    global kapak
    if kapak < len (kapaklar)+3:
        kapak -=1
    else:
        kapak =0
    print(kapak)

    goster()

buton = Button(text="Önceki", command=geri)
buton.grid(row=2, column=1, padx= 10, pady=10)
buton.config(font=("Arial", 20))



baslik = Label(pencere, text="Ev Fotoğrafları")
baslik.grid(row= 0, column= 0, padx= 10, pady=10)
baslik.config(font=("Arial", 30))

cikiş = Button (text="Çıkış", command= pencere.quit)
cikiş.grid(row=2, column=8, padx= 10, pady=10)
cikiş.config(font=("Arial", 20))




mainloop()

