from tkinter import *
from PIL import ImageTk, Image
from time import sleep
import tkinter as tk
from threading import *

root = Tk()#tk root değişkenine atandı
root.title("HalAt")#Frame(Ana pencere)'nin ismi verildi
root.geometry("800x600")#Frame(Ana pencere)'nin boyutu verildi

width = 600#ip ve diğer karakterler için genişlik değişkeni verildi
height = 400#ip ve diğer karakterler için uzunluk değişkeni verildi

global sleepValue#Uyku süresi için tanımlanan değişken
sleepValue=0.1# otomatik seviye düzeyi zor ile başlar


canvas1 = Canvas(root, width=width, height=height, bg="white")#Canvas oluşturuldu
img = ImageTk.PhotoImage(Image.open("arkaplan.jpeg"))#Arka plan resmi img değişkenine atıldı
solAdam = tk.PhotoImage(file="solAdam.png")#Soldaki karakter solAdam değişkenine atandı
sagKadin = tk.PhotoImage(file="sagKadin.png")#Sagdaki karakter sagkadin değişkenine atandı
canvas1.create_image(0, 0, anchor=NW, image=img)#arkaplan canvasa tanımlandı
halat_x1 = width - 400#Halatın x değeri
halat_x2 = width - 200#halatın y değeri
halat = canvas1.create_line(halat_x1, height / 1.7, halat_x2, height / 1.7, fill="black")#halat olusturuldu

solSinir = canvas1.create_line(20, height / 2, 20, height / 1.5, fill="red")#Sağ bitiş çizgisi oluşturuldu
sagSinir = canvas1.create_line(580, height / 2, 580, height / 1.5, fill="red")#Sol bitiş çizgisi oluşturuldu

adam = canvas1.create_image(halat_x1 - 40, height / 2, anchor=NW, image=solAdam)#Soldaki karakter canvasta tanımlandı
kadin = canvas1.create_image(halat_x2 - 20, height / 2, anchor=NW, image=sagKadin)#Sağdaki karakter canvasta tanımlandı

loginCanvas = Canvas(root, width=width, height=height)#Giriş ekranı canvas'ı tanımlandı
bilgi= ImageTk.PhotoImage(Image.open("bilgi.jpg"))#Nasıl oynanır resmi bilgi adlı değişkene aktarıldı
loginCanvas.create_image(75, 0, anchor=NW, image=bilgi)#Resim canvasa bağlanır

multiButton = Button(None, text='Arkadaşına karşı')#Arkadaşa karşı butonu tanımlandı
computerButton = Button(None, text='Bilgisayara karşı')#Bilgisayara karşı butonu tanımlandı
multiTamam = Button(None, text='Hazırsanız başlayalım ?!?!?')#Arkadaşa karşı hazırsanız başlayalım butonu tanımlandı
basla = Button(None, text='Hazırsanız başlayalım ?!?!?')#Bilgisayara karşı hazırsanız başlayalım butonu tanımlandı
bilgisayarImg = PhotoImage(file="bilgisayara.png") # bilgisayara karşı olan görseli ekliyor
computerButton.config(image=bilgisayarImg) #görseli butona bağlıyor
arkadasImg=PhotoImage(file="arkadasa.png") #arkadaşa olan görseli ekliyor
multiButton.config(image=arkadasImg) #görseli butona bağlıyor
computerButton.pack()#Bilgisayara karşı butonu gösterildi
multiButton.pack()#Arkadaşa karşı butonu gösterildi
loginCanvas.pack()#Giriş ekranı canvası gösterildi.




kazananCanvas = Canvas(root, width=width, height=height, bg="white")#Kazandıktan sonra çıkacak olan canvas tanımlandı
img2 = ImageTk.PhotoImage(Image.open("lastWin.jpg"))#Kazandıktan sonra ortaya çıkacak resim img2 değişkenine eklendi
kazananCanvas.create_image(0, 0, anchor=NW, image=img2)#Resim canvasa bağlanır.
var = StringVar()#
kazanan = Label(root, textvariable=var, relief=RAISED)#kazanın yazıldığı label

kolay=Button(None, text='Kolay')#Kolay butonu tanımlandı
kolayImg = PhotoImage(file="kolay.png") #kolay seviyesindeki görseli ekliyor
kolay.config(image=kolayImg) #görseli butona bağlıyor

orta=Button(None, text='Orta')#Orta butonu tanımlandı
ortaImg = PhotoImage(file="orta.png") # orta seviyesindeki görseli ekliyor
orta.config(image=ortaImg) #görseli butona bağlıyor

zor=Button(None, text='Zor')#Zor butonu tanımlandı
zorImg = PhotoImage(file="zor.png") # zor seviyesindeki görseli ekliyor
zor.config(image=zorImg) # görseli butona bağlıyor


def Kolay(event):#Kolay seviye butonu fonksiyonu
    global sleepValue
    sleepValue = 0.6
    orta.destroy()
    zor.destroy()
    canvas1.pack()
    basla.pack()



def Orta(event):#Orta seviye butonu fonksiyonu
    global sleepValue
    sleepValue = 0.35
    kolay.destroy()
    zor.destroy()
    canvas1.pack()
    basla.pack()



def Zor(event):#Zor seviye butonu fonksiyonu
    global sleepValue
    sleepValue = 0.08
    orta.destroy()
    kolay.destroy()
    canvas1.pack()
    basla.pack()



def multi(event):#Arkadaşla oyna butonu fonksiyonu
    loginCanvas.destroy()
    computerButton.destroy()
    canvas1.pack()
    multiTamam.pack()



def multiBasla(event):#Arkadaşa karşı kısmında Hazırsanız başlayalım butonu fonksiyonu
    loginCanvas.destroy()
    canvas1.pack()
    root.bind('<a>', left)
    root.bind('<i>', right)



def computer(event):#Bilgisayara karşı kısmında Hazırsanız başlayalım butonu fonksiyonu
    loginCanvas.destroy()
    multiButton.destroy()
    kolay.pack()
    orta.pack()
    zor.pack()



def left(event):#Sol tarafa hareket etme fonksiyonu
    yeri = int(canvas1.coords(halat)[0])#Kazananı belirlemek için halatın konumunu bize veren değişken
    if yeri != 35:#ifin içinde ise oyun devam eder
        x = -5
        y = 0
        canvas1.move(halat, x, y)
        canvas1.move(adam, x, y)
        canvas1.move(kadin, x, y)
    else:#Oyun sonlanmış, sol taraf kazanmıştır
        canvas1.destroy()
        root.unbind('<KeyPress-a>')  # oyun sonuçlandığı zaman harflerin bağlantısı sonlanıyor
        root.unbind('<KeyPress-i>')
        multiTamam.destroy()
        kazananCanvas.pack()
        kazanan.pack()
        kolay.destroy()
        orta.destroy()
        zor.destroy()
        basla.destroy()
        multiButton.destroy()
        computerButton.destroy()
        var.set("Sol kazandı")



def right(event):#Sağ tarafa hareket ettirme fonksiyonu
    yeri = int(canvas1.coords(halat)[0])#Kazananı belirlemek için halatın konumunu bize veren değişken
    if yeri != 360:#ifin içinde ise oyun devam eder
        x = 5
        y = 0
        canvas1.move(halat, x, y)
        canvas1.move(adam, x, y)
        canvas1.move(kadin, x, y)
    else:
        canvas1.destroy()
        root.unbind('<KeyPress-a>')  # oyun sonuçlandığı zaman harflerin bağlantısı sonlanıyor
        root.unbind('<KeyPress-i>')
        multiTamam.destroy()
        kazananCanvas.pack()
        kolay.destroy()
        orta.destroy()
        zor.destroy()
        basla.destroy()
        multiButton.destroy()
        basla.destroy()
        computerButton.destroy()
        var.set("Sağ kazandı")
        kazanan.pack()



def oto(event):#Bilgisayara karşı modunda çalışan fonksiyon

    def oyuncu(event):#Oyuncunun oynadığı fonksiyon
        root.bind(event, right)

    def pc():#Bilgisayarı kontrol ettiğimiz fonksiyon
        while (True):
            yeri = int(canvas1.coords(halat)[0])#Kazananı belirlemek için halatın konumunu bize veren değişken
            sleep(sleepValue)#Zorluk seviyesi burada belli oluyor
            if yeri > 35:#ifin içinde kaldığı sürede oyun devam eder
                x = -5
                y = 0
                canvas1.move(halat, x, y)
                canvas1.move(adam, x, y)
                canvas1.move(kadin, x, y)
            else:#Oyun bitmiştir. Kazananı söyleme burada yapılır
                canvas1.destroy()
                root.unbind('<KeyPress-a>')  # oyun sonuçlandığı zaman harflerin bağlantısı sonlanıyor
                root.unbind('<KeyPress-i>')
                multiTamam.destroy()
                kolay.destroy()
                orta.destroy()
                zor.destroy()
                computerButton.destroy()
                basla.destroy()
                kazananCanvas.pack()
                var.set("Sol kazandı")
                kazanan.pack()
                break
    t1 = Thread(target=pc)#Bilgisayarla oyuncuyu aynı anda oynatabilmek için thread kullanılmıştır.
    t2 = Thread(target=oyuncu('<i>'))
    t1.start()
    t2.start()

#Butonlarla fonksiyonlar bağlanmıştır
multiButton.bind('<Button-1>', multi)
basla.bind('<Button-1>', oto)
computerButton.bind('<Button-1>', computer)
multiTamam.bind('<Button-1>', multiBasla)

kolay.bind('<Button-1>', Kolay)
orta.bind('<Button-1>', Orta)
zor.bind('<Button-1>', Zor)

root.mainloop()