from tkinter import *
import random
import string

def rand():
    n = leng.get()

    if n < 8:
        output.set("Length must be ≥ 8")
        return

    small = string.ascii_lowercase
    capital = string.ascii_uppercase
    num = string.digits
    special = "@#&_%-*"

    password = [
        random.choice(capital),
        random.choice(small),
        random.choice(num),
        random.choice(special)
    ]

    all_chars = small + capital + num + special
    for _ in range(n - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    output.set("".join(password))


root = Tk()
root.geometry("415x525")
root.title("Pardhu Password Generator")

output = StringVar()

Label(root, text='Length of Required Password', font='arial 12 bold').pack(pady=10)

leng = IntVar(value=8)
Spinbox(root, from_=8, to_=32, textvariable=leng, width=24, font='arial 16').pack()

Button(
    root,
    text="Generate Strong Password",
    command=rand,
    font="Arial 10",
    bg='lightblue',
    fg='black',
    activebackground="teal",
    padx=5,
    pady=5
).pack(pady=20)

Label(root, text='Generated Password', font='arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=output, width=24, font='arial 16').pack()

root.mainloop()
