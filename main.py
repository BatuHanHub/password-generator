# Kütüphaneler
from tkinter import *
from tkinter import messagebox
import random
    
# Şifre için kullanılacak elemanlar

buyukHarf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kucukHarf = "abcdefghijklmnopqrstuvwxyz"
sayilar = "1234567890"
ozelKarakter = "?@!#%+-*"

karakterler = buyukHarf+kucukHarf+sayilar+ozelKarakter
###

def sifreOlustur():
    sifre = "".join(random.sample(karakterler, uzunluk.get()))
    sifreAlani.configure(state='normal')
    sifreAlani.delete(0, END)
    sifreAlani.insert(0, sifre)
    sifreAlani.configure(state='readonly')

def kaydet():
    soru = messagebox.askyesno('Kaydet','Şifrenizi kaydetmek istediğinizden emin misiniz?')
    if soru == True:
        print()
        with open('Şifrem.txt','a',encoding='utf8') as dosya:
            dosya.write(f'{isimAlani.get()} - {sifreAlani.get()}')
            messagebox.showinfo('İşlem Başarılı','İşleminiz başarıyla gerçekleştirildi.')
    else:
        pass
    
pencere = Tk()
pencere.geometry('850x400')
pencere.title('Şifre Oluşturucu')
pencere.resizable(height=False, width= False)
pencere.configure(bg='#212121')

# Uygulama isim alanı {
isimFrame = Frame(bg='#212121')
isimYaziLabel = Label(isimFrame,text='İsim:', bg='#212121', fg='white', font=('arial 35 bold'))
isimAlani =  Entry(isimFrame, font=('arial 30 bold'), state='normal', width=28)

isimFrame.place(relx=0.1 ,rely=0.2 , relwidth=1, relheight=0.2)
isimYaziLabel.pack(side='left')
isimAlani.pack(side='left')
# }

# Şifre alanı {
sifreFrame = Frame(bg='#212121')
yaziLabel = Label(sifreFrame,text='Şifreniz:', bg='#212121', fg='white', font=('arial 35 bold'))
sifreAlani =  Entry(sifreFrame, font=('arial 30 bold'), state='readonly')

uzunluk = IntVar(sifreFrame)
uzunluk.set(8) # Program çalıştığında ilk çıkacak sayıyı 8 yaptım

uzunlukOptMenu = OptionMenu(sifreFrame, uzunluk, 8,9,10,11,12,13,14)
uzunlukOptMenu.configure(height=2, width=5, borderwidth=0, font=('arial 13 bold'))

sifreFrame.place(relx=0.1 ,rely=0.4 , relwidth=1, relheight=0.2)
yaziLabel.pack(side='left')
sifreAlani.pack(side='left')
uzunlukOptMenu.pack(side='left')
# }

# Buttonlar {
buttonFrame = Frame(bg='#212121')

olusturButton = Button(buttonFrame, text='Oluştur', font=('arial 30 bold'), command=sifreOlustur)
kaydetButton = Button(buttonFrame, text='Kaydet', font=('arial 30 bold'), command=kaydet)

buttonFrame.place(relx=0.2 ,rely=0.7 , relwidth=0.7, relheight=0.2)
olusturButton.pack(side=LEFT)
kaydetButton.pack(side=RIGHT)
# }

pencere.mainloop()
