from tkinter import*
from weltSetting import*
import haupt

losingtext = "DU HAST VERLOREN. \n MÖCHTEST DU ERNEUT SPIELEN?"
class EndGame():
    def __init__(self):
        self.tk = Tk()
        self.tk.title('')
        self.tk.geometry('500x500')

        self.frame1 = Frame(self.tk, bg='red')
        self.frame1.place(x=0,y=0,width=500,height=500)
        self.l_text = Label(self.frame1, text=losingtext, bg='red', fg='white')
        self.l_text.grid(column=0, row=0, ipadx=40, ipady=10, padx=20, pady=20)
        self.b_newstart = Button(self.frame1, text='NEUSTART', command=self.newstart)
        self.b_newstart.grid(column=0, row=1, ipadx=40, ipady=10, padx=20, pady=20)
        self.b_leave = Button(self.frame1,text='VERLASSEN', command=self.leave)
        self.b_leave.grid(column=0, row=2, ipadx=40, ipady=10, padx=20, pady=20)
        self.frame2 = Frame(self.tk, bg='orange')
        self.frame2.place(x=280,y=25,width=190,height=400)

        

        self.tk.mainloop()

    def newstart(self):
        self.tk.destroy()
        haupt.run_game()
    def leave(self):
        self.tk.destroy()
        haupt.pygame.display.quit()
        haupt.pygame.quit()
        
