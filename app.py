
import tkinter as tk
from tkinter import Entry
from tkinter.constants import SUNKEN

app = tk.Tk()
Label=tk.Label

if __name__ == "__main__":
    app.geometry("300x300")
    languages=["PIFFN","JAWA","CPLUS","PHP","jo WAS"]
    labels =range(5)
    for i in range(5):
        lblLang= Label(app,text=languages[i],
                       fg="white",bg="black")
        lblLang.place(x=10,y=10+i*30,
                      width=120,height=25)
    app.mainloop()
