from tkinter import*
import haupt
import shelve

class HomeScreen():
    def __init__(self):
        self.text = "Informatikprojekt 2018/2019\nKurs: info,gk,KD, Stufe:13\nEntwickler: Sascha Rudenko\nVersion: alpha\nBei Fragen bitte an den Entwickler wenden"
        self.info1 = """Folgende Dinge müssen als nächstes implementiert werden:
                        - bei Kälte und Hunger muss der Spieler schneller Energie verlieren
                        - wenn der Spieler im Haus ist, soll er Energie und Items bekommen
                        - Er darf im selben Haus nicht mehrmals Items bekommen
                           """
        self.info2 =""" 
Mit der Eingabe wird berechnet, wie viele Tiles (Bäume, Häuser) 
generiert werden sollen. Und bis wohin die Tiles spawnen sollen. 
Es dürfen nur ganze Zahlen eingegeben werden. 
Ich empfehle: 10000x10000. Die Tagesdauer gibt an, wie lang der Tag dauert.
"""
        self.a = Tk()
        self.a.title('')
        self.a.geometry('735x600+120+50')

        image = PhotoImage(file="assets/startgameImg.png")
        self.label = Label(self.a, image = image)
        self.label.place(x=0, y=0)

        self.text = Label(self.a, text=self.text)
        self.text.place(x=30, y=30)
        
        self.b_play = Button(self.a, text='PLAY', command=self.play)
        self.b_play.place(x=40, y=150, width=150, height=50)
        self.b_settings = Button(self.a, text='Settings', command=self.openSettings)
        self.b_settings.place(x=40, y=300, width=150, height=50)

        self.a.mainloop()

    def play(self):
        file = shelve.open('mydata')
        worldsize = {'width': 15000,
                     'height': 15000,
                     'duration': 300}
        file['settings'] = worldsize
        print(file['settings'])
        file.close()
        self.a.destroy()
        haupt.run_game()

    def openSettings(self):
        self.a.iconify()
        b = Toplevel(self.a, bg='orange')
        b.title('Einstellungen')
        b.geometry("735x600+120+50")

        t1 = Label(b, text=self.info1)
        t1.place(x=20, y=20)
        t4 = Label(b, text=self.info2)
        t4.place(x=20, y=450)

        frame1 = Frame(b, bg='white')
        frame1.place(x=20, y=150, width=500, height=280)
        t2 = Label(frame1, text='Weltweite')
        t2.grid(column=0, row=0, padx=20, pady=15)
        t3 = Label(frame1, text='Welthöhe')
        t3.grid(column=0, row=1, padx=20, pady=15)
        t3 = Label(frame1, text='Tagesdauer')
        t3.grid(column=0, row=2, padx=20, pady=15)
        self.e1 = Entry(frame1)
        self.e1.grid(column=1, row =0, padx=20, pady=15)
        self.e2 = Entry(frame1)
        self.e2.grid(column=1, row=1, padx=20, pady=15)
        self.e3 = Entry(frame1)
        self.e3.grid(column=1, row=2, padx=20, pady=15)
        b = Button(frame1, text='Play', command=self.settingplay)
        b.grid(column=1, row=3, ipadx=40, ipady=10, padx=20, pady=20)
        
    def settingplay(self):
        #file = open('/Users/maxmustermann/Documents/Spieleprojekt/alpha_v1/saveddata.txt')
        #r = file.read()
        #r
        #print(r)
        file = shelve.open('mydata')
        worldsize = {'width': int(self.e1.get()),
                     'height': int(self.e2.get()),
                     'duration': int(self.e3.get())}
        file['settings'] = worldsize
        print(file['settings'])
        #type(shelfFile)
        self.a.destroy()
        file.close()
        haupt.run_game()

a = HomeScreen()
