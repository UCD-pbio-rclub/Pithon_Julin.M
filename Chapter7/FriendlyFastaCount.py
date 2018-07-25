from tkinter import *
import tkinter.filedialog as fd
from Chapter6.countSeqFuns import countFasta


class App:

    def __init__(self, master):
        self.file = StringVar()
        self.count = IntVar()
        frame = Frame(master)
        frame.pack()
        Button(frame,
               text="Choose File",
               command=self.get_file).grid(row=0, column=0)
        Label(frame, textvariable=self.file).grid(row=0, column=1)
        Button(frame, 
               text="Count Sequences",
               command=self.get_count).grid(row=1, column=0)
        Label(frame, textvariable=self.count).grid(row=1, column=1)

    def get_file(self):
        self.file.set(fd.askopenfilename())

    def get_count(self):
        self.count.set(countFasta(self.file.get()))

root = Tk()
app = App(root)
root.mainloop()

