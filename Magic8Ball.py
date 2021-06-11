from tkinter import *
import random
from tkinter import messagebox

answers = {
    1: "It's your lucky day!",
    2: "Certainly.",
    3: "You may rely on it.",
    4: "Without a doubt.",
    5: "Yes - definitely.",
    6: "Most likely.",
    7: "Not today.",
    8: "Try again.",
    9: "Concentrate and ask again.",
    10: "Don't count on it.",
    11: "Very doubtful.",
    12: "Outlook no so good."}

root = Tk()
root.geometry('240x240')
root.title("Magic 8 Ball")
root.iconbitmap("D:\IT\kursy\Python\pycharm projects\Ball.ico")


def answer():
    num = random.randint(1, 13)
    messagebox.showinfo("Answer:", answers[num])


ball = PhotoImage(file=r"D:\IT\kursy\Python\pycharm projects\8Ball\240px-Magic_eight_ball.png")


btn = Button(root, text="Magic8Ball", image=ball, command=answer)
btn.place(x=0, y=0)

root.mainloop()
