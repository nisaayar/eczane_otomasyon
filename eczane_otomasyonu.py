import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import sqlite3
from numpy import random
import re

bgColour = "#8b8386"

def clear_widgets(frame):

    for widget in frame.winfo_children():
        widget.destroy()

def create_connection(dp_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Bağlantı başarılı: SQLite " + sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn

    """
    curs.execute('''CREATE TABLE Reports (
                report_ID INTEGER PRIMARY KEY,
                purchase_ID INTEGER,
                sales_ID INTEGER,
                cust_ID INTEGER,
                date DATE)''')
    curs.execute('''CREATE TABLE Medicines (
                med_ID INTEGER PRIMARY KEY,
                med_category VARCHAR(30),
                name VARCHAR(30),
                description VARCHAR(30),
                price VARCHAR(30))''')
    curs.execute('''CREATE TABLE Ilaclar (
                ilac_ID INTEGER PRIMARY KEY,
                ilac_adi VARCHAR(255),
                ilac_turu VARCHAR(255),
                uretici_firma VARCHAR(255),
                ilac_kodu VARCHAR(50),
                uretim_yeri VARCHAR(255),
                son_kullanma_tarihi DATE,
                uretim_tarihi DATE,
                stok_durumu VARCHAR(50)
                )''')
    curs.execute ( CREATE TABLE Ilaclar (
        ilac_ID INTEGER PRIMARY KEY,
        ilac_adi VARCHAR(255),
        ilac_turu VARCHAR(255),
        uretici_firma VARCHAR(255),
        ilac_kodu VARCHAR(50),
        uretim_yeri VARCHAR(255),
        son_kullanma_tarihi DATE,
        uretim_tarihi DATE,
        stok_durumu VARCHAR(50)
    ) 
'''
    """
    conn.commit()
    conn.close()
    

def Insert(ilacAdi, ilacTuru, firmaAdi, stokDurumu, kodu, uretimTarihi, sonKullanmaTarihi, uretimYeri,
           entry_ilacAdi=None):

    connection = sqlite3.connect("data/eczane_otomasyonu.db")
    cursor = connection.cursor()

    sql = 'INSERT INTO Ilac(ilacAdi, ilacTuru, firmaAdi, stokDurumu, kodu, uretimTarihi, sonKullanmaTarihi, uretimYeri) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'
    values = (ilacAdi, ilacTuru, firmaAdi, stokDurumu, kodu, uretimTarihi, sonKullanmaTarihi, uretimYeri)
    cursor.execute(sql, values)

    connection.commit()
    connection.close()
    print("EKLEME İŞLEMİ BAŞARILI!")


    Insert(entry_ilacAdi.get(), entry_ilacTuru.get(), entry_firmaAdi.get(), entry_stokDurumu.get(), entry_kodu.get(),
           entry_uretimTarihi.get(), entry_sonKullanmaTarihi.get(), entry_uretimYeri.get())


def Update(id, entry_ilacAdi, entry_ilacTuru, entry_firmaAdi, entry_stokDurumu, entry_kodu):
    connection = sqlite3.connect("data/eczane_otomasyonu.db")
    cursor = connection.cursor()
    id = id
    ilacAdi = entry_ilacAdi.get()
    ilacTuru = entry_ilacTuru.get()
    firmaAdi = entry_firmaAdi.get()
    stokDurumu = entry_stokDurumu.get()
    kodu = entry_kodu.get()

    sql = 'UPDATE Ilac SET ilacAdi = ?, ilacTuru = ?, firmaAdi = ?, stokDurumu = ? WHERE kodu = ?'
    values = (ilacAdi, ilacTuru, firmaAdi, stokDurumu, kodu)
    cursor.execute(sql, values)

    connection.commit()
    connection.close()

    print("GÜNCELLEME İŞLEMİ BAŞARILI!")

def Delete(kodu):
    connection = sqlite3.connect("data/eczane_otomasyonu.db")
    cursor = connection.cursor()

    sql = 'DELETE FROM Ilac WHERE kodu = ?'
    values = (kodu,)
    cursor.execute(sql, values)

    connection.commit()
    connection.close()

    print("SİLME İŞLEMİ BAŞARILI!")

def Select():
    connection = sqlite3.connect("data/eczane_otomasyonu.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Ilac')
    data = cursor.fetchall()

    connection.commit()
    connection.close()
    return data

def IndexChangedUpdate(event):
    selected_item = event.widget.get()
    print("düzensiz değerler",selected_item)
    selected_item = re.sub('\{(.*?)\}','', selected_item).split()

    print("Dizi Olarak Değerler:", selected_item)

    ilacAdi = tk.Label(frameMain4, text="İlaç Adı:")
    ilacAdi.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    entry_ilacAdi = tk.Entry(frameMain4)
    entry_ilacAdi.insert(0, selected_item[1])
    entry_ilacAdi.grid(row=1, column=1, padx=5, pady=5)


    label_ilacTuru = tk.Label(frameMain4, text="İlaç Türü:")
    label_ilacTuru.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_ilacTuru = tk.Entry(frameMain4)
    entry_ilacTuru.insert(1, selected_item[2])
    entry_ilacTuru.grid(row=2, column=1, padx=5, pady=5)


    label_firmaAdi = tk.Label(frameMain4, text="Firma Adı:")
    label_firmaAdi.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_firmaAdi = tk.Entry(frameMain4)
    entry_firmaAdi.insert(0, selected_item[3])
    entry_firmaAdi.grid(row=3, column=1, padx=5, pady=5)


    label_stokDurumu = tk.Label(frameMain4, text="Stok Durumu:")
    label_stokDurumu.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_stokDurumu = tk.Entry(frameMain4)
    entry_stokDurumu.insert(0, selected_item[4])
    entry_stokDurumu.grid(row=4, column=1, padx=5, pady=5)


    label_kodu = tk.Label(frameMain4, text="Kodu:")
    label_kodu.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    entry_kodu = tk.Entry(frameMain4)
    entry_kodu.insert(0, selected_item[5])
    entry_kodu.grid(row=5, column=1, padx=5, pady=5)


    label_uretimYeri = tk.Label(frameMain4, text="Üretim Yeri:")
    label_uretimYeri.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    entry_uretimYeri = tk.Entry(frameMain4)
    entry_uretimYeri.insert(0, selected_item[6])
    entry_uretimYeri.grid(row=6, column=1, padx=5, pady=5)


    label_sonKullanmaTarihi = tk.Label(frameMain4, text="Son Kullanma Tarihi:")
    label_sonKullanmaTarihi.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
    entry_sonKullanmaTarihi = tk.Entry(frameMain4)
    entry_sonKullanmaTarihi.insert(0, selected_item[7])
    entry_sonKullanmaTarihi.grid(row=7, column=1, padx=5, pady=5)

    label_uretimTarihi = tk.Label(frameMain4, text="Üretim Tarihi:")
    label_uretimTarihi.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
    entry_uretimTarihi = tk.Entry(frameMain4)
    entry_uretimTarihi.insert(0, selected_item[8])
    entry_uretimTarihi.grid(row=8, column=1, padx=5, pady=5)


    tk.Button(
        frameMain4,
        text="İLAÇ DEĞİŞTİR",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: Update(selected_item[0], entry_ilacAdi, entry_ilacTuru, entry_firmaAdi, entry_stokDurumu,
                               entry_kodu, entry_uretimYeri, entry_sonKullanmaTarihi, entry_uretimTarihi)).grid(row=9, column=0, columnspan=2)

def IndexChangedDelete(event):
    selected_item = event.widget.get()
    selected_item = re.sub('\{(.*?)\}', '', selected_item).split()
    kodu = selected_item[0]
    print(kodu)

    # silme butonu
    tk.Button(
        frameMain5,
        text="İLAÇ SİL",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: Delete(kodu)).grid(row=12, column=0, columnspan=2, pady=10)

def LoadFrame1():
    clear_widgets(frameMain2)
    frameMain.tkraise()
    frameMain.pack_propagate(False)
    # logo widget
    imgLogo = ImageTk.PhotoImage(file="assets/eczane.png")
    logoWidget = tk.Label(frameMain, image=imgLogo, bg=bgColour)
    logoWidget.image = imgLogo
    logoWidget.pack()

    tk.Label(
        frameMain,
        text="ECZANE OTOMASYONU",
        bg=bgColour,
        fg="black",
        font=("TkMenuFont", 14)
    ).pack()



    ekle=tk.Button(
        frameMain,
        text="EKLE",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame3()
    ).pack( pady=20)



    duzenle=tk.Button(
        frameMain,
        text="DÜZENLE",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame4()
    ).pack( pady=20)


    sil=tk.Button(
        frameMain,
        text="SİL",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame5()
    ).pack( pady=20)

def LoadFrame2():
    clear_widgets(frameMain2)
    clear_widgets(frameMain)
    frameMain2.tkraise()

    data = EczaneDatabase()


    imgLogo = ImageTk.PhotoImage(file="assets/eczane.png")
    logoWidget = tk.Label(frameMain2, image=imgLogo, bg=bgColour)
    logoWidget.image = imgLogo
    logoWidget.pack(pady=20)

    tk.Label(
        frameMain2,
        text=data[0],
        bg=bgColour,
        fg="white",
        font=("TkHeadingFont", 20)
    ).pack(pady=25)

    data= data[1:]
    for i in data:
        tk.Label(
            frameMain2,
            text=i,
            bg=bgColour,
            fg="white",
            font=("Shanti", 12)
        ).pack(fill="both", padx=25)


    tk.Button(
        frameMain2,
        text="DEĞİŞTİR",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame2()
    ).pack(pady=20)

    tk.Button(
        frameMain2,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:LoadFrame1()
    ).pack(pady=20)
def LoadFrame3():
    clear_widgets(frameMain)
    frameMain3.tkraise()

    ilacAdi = tk.Label(frameMain3, text="İlaç Adı:")
    ilacAdi.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    entry_ilacAdi = tk.Entry(frameMain3)
    entry_ilacAdi.grid(row=0, column=1, padx=5, pady=5)


    label_ilacTuru = tk.Label(frameMain3, text="İlaç Türü:")
    label_ilacTuru.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W) #widget hizalama
    entry_ilacTuru = tk.Entry(frameMain3)
    entry_ilacTuru.grid(row=1, column=1, padx=5, pady=5)


    label_firmaAdi = tk.Label(frameMain3, text="Firma Adı:")
    label_firmaAdi.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_firmaAdi = tk.Entry(frameMain3)
    entry_firmaAdi.grid(row=2, column=1, padx=5, pady=5)


    label_stokDurumu = tk.Label(frameMain3, text="Stok Durumu:")
    label_stokDurumu.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_stokDurumu = tk.Entry(frameMain3)
    entry_stokDurumu.grid(row=3, column=1, padx=5, pady=5)


    label_kodu = tk.Label(frameMain3, text="Kodu:")
    label_kodu.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_kodu = tk.Entry(frameMain3)
    entry_kodu.grid(row=4, column=1, padx=5, pady=5)


    label_uretimTarihi = tk.Label(frameMain3, text="Üretim Tarihi:")
    label_uretimTarihi.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    entry_uretimTarihi = tk.Entry(frameMain3)
    entry_uretimTarihi.grid(row=5, column=1, padx=5, pady=5)


    label_sonKullanmaTarihi = tk.Label(frameMain3, text="Son Kullanma Tarihi:")
    label_sonKullanmaTarihi.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    entry_sonKullanmaTarihi = tk.Entry(frameMain3)
    entry_sonKullanmaTarihi.grid(row=6, column=1, padx=5, pady=5)


    label_uretimYeri = tk.Label(frameMain3, text="Üretim Yeri:")
    label_uretimYeri.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
    entry_uretimYeri = tk.Entry(frameMain3)
    entry_uretimYeri.grid(row=7, column=1, padx=5, pady=5)


    button_ekle = tk.Button(
     frameMain3,
     text="İLAÇ EKLE",
    font=("TkHeadingFont", 16),
    bg="#FF7700",
    fg="black",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:Insert(entry_ilacAdi,entry_ilacTuru,entry_firmaAdi,entry_stokDurumu,entry_kodu,entry_uretimTarihi,entry_sonKullanmaTarihi,entry_uretimYeri))
    button_ekle.grid(row=8, column=0, columnspan=2, pady=10)

    btn_geri=tk.Button(
        frameMain3,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1())
    btn_geri.grid(row=9, column=0, columnspan=2, pady=10)

def LoadFrame4():
    clear_widgets(frameMain)
    frameMain4.tkraise()

    listObjects= Select()


    combo_var = tk.StringVar()

    combo = tk.Label(frameMain4, text="İlaç seç")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    combo = ttk.Combobox(frameMain4, values= listObjects)
    combo.grid(row=0, column=1, padx=5, pady=15)


    combo.bind('<<ComboboxSelected>>', IndexChangedUpdate)


    btn_geri = tk.Button(
        frameMain4,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()).grid(row=13, column=0, columnspan=2, pady=10)

def LoadFrame5():
    clear_widgets(frameMain)
    frameMain5.tkraise()

    listObjects = Select()


    combo_var = tk.StringVar()

    combo = tk.Label(frameMain5, text="İlaç seç")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    combo = ttk.Combobox(frameMain5, values=listObjects)
    combo.grid(row=0, column=1, padx=5, pady=15)


    combo.bind('<<ComboboxSelected>>', IndexChangedDelete)

    btn_geri = tk.Button(
        frameMain5,
        text="GERİ",
        font=("TkHeadingFont", 16),
        bg="#FF7700",
        fg="black",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: LoadFrame1()).grid(row=13, column=0, columnspan=2, pady=10)


root = tk.Tk()
root.title("ECZANE OTOMASYONU")



frameMain = tk.Frame(root, width=1200, height=1300, bg=bgColour)
frameMain2 = tk.Frame(root, bg=bgColour)
frameMain3 = tk.Frame(root, bg=bgColour)
frameMain4 = tk.Frame(root, bg=bgColour)
frameMain5 = tk.Frame(root, bg=bgColour)

for frame in (frameMain,frameMain2,frameMain3,frameMain4,frameMain5):
    frame.grid(row=0, column=0)

LoadFrame1()

root.mainloop()

