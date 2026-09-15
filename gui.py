from tkinter import *
import operator
operations = {"+": operator.add, "-": operator.sub, "÷": operator.truediv, "×": operator.mul, "^":operator.pow}

light_blue = "#0078D7"
grey = "#808080"
black = "#000000"
white = "#FFFFFF"
red = "#FF0000"
charcoal_grey = "#36454F"
orange = "#FFA500"

window = Tk()
window.title("Calculator")
window.geometry("360x600")
window.configure(background=black)
# dosen't allow the window to be resized manually
window.resizable(height=False, width=False)

def calculate(o,num1,num2,operations):
    return operations[o](num1,num2)

class entry:
    def __init__(self):
        self.entry = Entry(
              window, 
              font=("Arial", 40), 
              bg=black, 
              fg=white,
              disabledbackground=black,
              disabledforeground=white,
              width=16,
              state=DISABLED
               )
        self.entry.place(x=0,y=0)
        self.ans = Entry(
              window, 
              font=("Arial", 40), 
              bg=black, 
              fg=white,
              disabledbackground=black,
              disabledforeground=white,
              width=16,
              state=DISABLED
               )
        self.ans.place(x=0,y=110)
    def add(self,i):
        self.entry.configure(state=NORMAL)
        self.entry.insert(END,i)
        self.entry.configure(state=DISABLED)

    def delete(self):
        self.entry.configure(state=NORMAL)
        self.entry.delete(len(self.entry.get()) - 1, END)
        self.entry.configure(state=DISABLED)

    def calc(self):
        i = (self.entry.get()).split(" ")
        c = calculate(i[1],float(i[0].strip()),float(i[2].strip()),operations)
        c = round(c,6)

        self.ans.configure(state=NORMAL)
        self.ans.insert(END,c)
        self.ans.configure(state=DISABLED)

    def clear(self):
        self.entry.configure(state=NORMAL)
        self.entry.delete(0,END)
        self.entry.configure(state=DISABLED)

        self.ans.configure(state=NORMAL)
        self.ans.delete(0,END)
        self.ans.configure(state=DISABLED)


def button(text,size,x,y,command,width=None,height=None,colour=None):
    b = Button(
                window,
                text=text,
                font=("Arial", size),
                activebackground=black,
                bg=black,
                fg=white,
                width=width,
                command=command,
                activeforeground=white,
                )
    if width is not None:
            b.config(width=width)
    if height is not None:
            b.config(height=height)
    if colour is not None:
           b.config(activebackground=colour,bg=colour)
           
    b.place(x=x, y=y)
   


e = entry()                
            

#first column

bb = button("←",20,0,175,lambda:e.delete(),5,2,grey)
b1 = button("1",20,0,260,lambda:e.add("1"),5,2)
b4 = button("4",20,0,345,lambda:e.add("4"),5,2)
b7 = button("7",20,0,430,lambda:e.add("7"),5,2)
bpower = button("^",20,0,515,lambda:e.add(" ^ "),5,2)

#second column

ba = button("AC",20,90,175,lambda:e.clear(),5,2,grey)
b2 = button("2",20,90,260,lambda:e.add("2"),5,2)
b5 = button("5",20,90,345,lambda:e.add("5"),5,2)
b8 = button("8",20,90,430,lambda:e.add("8"),5,2)
b0 = button("0",20,90,515,lambda:e.add("0"),5,2)

#third column

bp = button("%",20,180,175,None,5,2,grey)
b3 = button("3",20,180,260,lambda:e.add("3"),5,2)
b6 = button("6",20,180,345,lambda:e.add("6"),5,2)
b9 = button("9",20,180,430,lambda:e.add("9"),5,2)
bdot = button(".",20,180,515,lambda:e.add("."),5,2)

#fourth column

bdivide = button("÷",20,270,175,lambda:e.add(" ÷ "),5,2,orange)
bplus = button("×",20,270,260,lambda:e.add(" × "),5,2,orange)
bminus = button("-",20,270,345,lambda:e.add(" - "),5,2,orange)
badd = button("+",20,270,430,lambda:e.add(" + "),5,2,orange)
be = button("=",20,270,515,lambda:e.calc(),5,2,orange)



window.mainloop()



