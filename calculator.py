

from tkinter import *
calculator = Tk()
calculator.title("Simple Calculator")
calculator.resizable(0,0)

class Shuaib(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.makeWidgets()

  
        
    def calculate(self, text):
        self.Operation.config(text=text)
        self.no1=self.No1.get()
        self.no2=self.No2.get()
        if text=='\\':
            text="//"
        if text=='MOD':
            text='%'
        if text=='^':
            text='**'
        
        
        self.result=(self.no1+text+self.no2)
        self.result=eval(self.no1+text+self.no2)
        self.Result.config(text=self.result)
        
        
    

    def clearText(self):
        self.No1.delete(0, 'end')
        self.No2.delete(0, 'end')
        self.Result.config(text='')

    def makeWidgets(self):
        self.no1=Label(self, text="Number 1: ")
        self.no1.grid(row=0, column =0)
        self.No1 = Entry(self)
        self.No1.grid(row=0, column= 1)
        
        self.Operation = Label(self)
        self.Operation.grid(row=1, column=1)
        
        self.no2=Label(self, text="Number 2: ")
        self.no2.grid(row=2, column =0)
        self.No2 = Entry(self)
        self.No2.grid(row=2, column= 1)
        
        
        self.result=Label(self, text="Result: ")
        self.result.grid(row=3, column =0)
        self.Result = Label(self)
        self.Result.grid(row=3, column= 1)
        
        #Button row 1
        self.add= Button(self, text="+", width= 5, command= lambda: self.calculate('+'))
        self.add.grid(row=0, column=2, padx=4)
        
        self.subtract= Button(self, text="-", width= 5, command= lambda: self.calculate('-'))
        self.subtract.grid(row=0, column=3, padx=0)
        
        self.multiply= Button(self, text="*", width= 5, command= lambda: self.calculate('*'))
        self.multiply.grid(row=0, column=4, padx=4)
        
        
        #Button row 2
        self.power= Button(self, text="^", width= 5, command= lambda: self.calculate('^'))
        self.power.grid(row=1, column=2, padx=3, pady=3)
        
        self.division= Button(self, text="/", width= 5, command= lambda: self.calculate('/'))
        self.division.grid(row=1, column=3, padx=0, pady=3)
        
        self.intdivision= Button(self, text="\\", width= 5, command= lambda: self.calculate('\\'))
        self.intdivision.grid(row=1, column=4, padx=3,pady=3)
        
        #Button row 3
        self.division= Button(self, text="MOD", width= 7, command= lambda: self.calculate('MOD'))
        self.division.grid(row=2, column=3, padx=0, pady=3)
        
        #Clear and Exit
        self.division= Button(self, text="Clear", width= 10, command= lambda: self.clearText())
        self.division.grid(row=3, column=3, padx=0, pady=0)
        
        self.division= Button(self, text="Exit", width= 10, command=calculator.destroy)
        self.division.grid(row=4, column=3, padx=0, pady=3)
        
        


mar = Shuaib(calculator).grid()  
calculator.mainloop()

