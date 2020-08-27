# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------#
# Kalkulacka                                                                   #
#------------------------------------------------------------------------------#

from tkinter import * 
from tkinter import font as tkFont
from math import *
#import tkFont

def callback(f, *a):
    """
    Vraci funkci f s nastavenym parametrem a.
    Tato funkce umi osetrit i vice nez jeden parametr.

    Pouziti:
        callback(funkce, arg1, arg2, ..., argn )
    """
    return lambda: f(*a)

class MyApp:

    control = ''
    firstNum = 0.0

    def createButton( self, textButton, rowButton, columnButton, rowspanButton = 2,
     colspanButton = 1 ):

        self._addButton = Button(
            self._numbersFrame, text=textButton, width = 5, height = rowspanButton,
            font=self._font, 
            command=callback(self._insert_key, textButton)
        )
        # -- add to grid
        self._addButton.grid(row=rowButton, column=columnButton, rowspan = rowspanButton,
         columnspan = colspanButton, sticky=W+E+N+S, padx=2, pady=2)

        # self._addButton.config(sticky = NSEW)

    def _big(self):
        print("big")
        self._font.config(size = 12, weight = "bold")
    
    def _normal(self):
        print("normal") 
        self._font.config(size = 10, weight = "normal")

    def _insert_key(self, sign):

        try:
            self._displayLabel.config( text = self._displayLabel.cget("text") + str(int(sign)))
        except ValueError:
            if(sign == "="):
                if(self.control == "+"):
                    self._displayLabel.config(
                         text = str(self.firstNum + int(self._displayLabel.cget("text")))
                    )
                if(self.control == "-"):
                    self._displayLabel.config(
                         text = str(self.firstNum - int(self._displayLabel.cget("text")))
                    )
                if(self.control == "/"):
                    self._displayLabel.config(
                         text = str(self.firstNum + int(self._displayLabel.cget("text")))
                    )
                if(self.control == "*"):
                    self._displayLabel.config(
                         text = str(self.firstNum * int(self._displayLabel.cget("text")))
                    )

                self.firstNum = int(self._displayLabel.cget("text"))
            else:
                self.firstNum = int(self._displayLabel.cget("text"))
                self._displayLabel.config( text = "")
            self.control = sign



        print("insKey"+ sign)
        
    def __init__(self, root):
        self._root = root
        self._mode = StringVar()
        self._root.title("Calculator")
        self._font = tkFont.Font(size=10, weight="normal")
    
        self._displayLabel = Label(
            self._root, text="0", background="#ffffff", 
            anchor=E, relief=SUNKEN, height=2, font=self._font
        )
        self._displayLabel.pack(fill=X, side=TOP, padx=8, pady=5)
    
        self._optionsFrame = Frame(self._root, relief=GROOVE)
        self._optionsFrame.pack()
        
        self._normalRadio = Radiobutton(
            self._optionsFrame, text="Normal", variable=self._mode, value="normal", 
            command=self._normal, font=self._font
        )
        self._normalRadio.pack(side=LEFT)

        self._bigRadio = Radiobutton(
            self._optionsFrame, text="Big", variable=self._mode, value="big", 
            command=self._big, font=self._font
        )
        self._bigRadio.pack(side=LEFT)
        
        self._numbersFrame = Frame(self._root)
        self._numbersFrame.pack(fill=BOTH, expand=1, padx=4, pady=4)
    
        Grid.columnconfigure( self._numbersFrame, [ 1, 2, 3, 4] , weight=1 )

        #First row buttons
        self.createButton( 'Cls',1,1 )
        self.createButton( '/',1,2 )
        self.createButton( '*',1,3 )
        self.createButton( '-',1,4 )
        #Second row buttons
        self.createButton( '7',3,1 )
        self.createButton( '8',3,2 )
        self.createButton( '9',3,3 )
        self.createButton( '+',3,4,4 )
        #Third row buttons
        self.createButton( '4',5,1 )
        self.createButton( '5',5,2 )
        self.createButton( '6',5,3 )
        #Forth row buttons
        self.createButton( '1',7,1 )
        self.createButton( '2',7,2 )
        self.createButton( '3',7,3 )
        self.createButton( '=',7,4,4 )
        #Fifth row buttons
        self.createButton( '0',9,1,2,2 )
        self.createButton( ',',9,3 )

        # available/disable buttons
        # -- self._plusButton.config(state=DISABLED)
        
        self._normalRadio.select()

def main():
    root = Tk()
    app = MyApp(root)
    root.mainloop()
    root.destroy()

main()
    

