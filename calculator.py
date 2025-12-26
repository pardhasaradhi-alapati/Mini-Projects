from tkinter import *

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(scvalue.get())
            scvalue.set(result)
        except:
            scvalue.set("Error")

    elif text == "C":
        scvalue.set("")

    else:
        scvalue.set(scvalue.get() + text)


root = Tk()
root.geometry("415x525")
root.title("Calculator By Pardhu")

scvalue = StringVar()
scvalue.set("")

screen = Entry(
    root,
    textvar=scvalue,
    font="lucida 40 bold",
    justify=RIGHT
)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


f = Frame(root, bg="grey")
for txt in ("9", "8", "7", "/"):
    b = Button(f, text=txt, font="lucida 35 bold")
    b.pack(side=LEFT, padx=12.5, pady=5)
    b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
for txt in ("6", "5", "4", "*"):
    b = Button(f, text=txt, font="lucida 35 bold")
    b.pack(side=LEFT, padx=12, pady=5)
    b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
for txt in ("3", "2", "1", "-"):
    b = Button(f, text=txt, font="lucida 35 bold")
    b.pack(side=LEFT, padx=13, pady=5)
    b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
for txt in ("C", "0", "=", "+"):
    b = Button(f, text=txt, font="lucida 35 bold")
    b.pack(side=LEFT, padx=10, pady=8)
    b.bind("<Button-1>", click)
f.pack()

root.mainloop()
