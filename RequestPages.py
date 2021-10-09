import tkinter as tk
from tkinter import StringVar, messagebox, ttk
from Request import *

WIDTH = 500
HEIGHT = 350
HEIGHT2 = 500

class Request_Page(tk.Toplevel):
    def __init__(self, master, customerid) -> None:
        super().__init__()
        self.master = master
        self.customerid = customerid
        self.title("Request Page")
        
        wid_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        x = (wid_screen/2) - (WIDTH/2)
        y = (height_screen/2) - (HEIGHT/2)
        self.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

        self.itemid = tk.StringVar()
        tk.Label(self, text="ID of item to submit request").pack()
        self.itemidentry = tk.Entry(self, textvariable=self.itemid)
        self.itemidentry.pack()

        tk.Button(self, text="Submit", font=("Arial", 12), width=12, height=1, command=self.submit).pack()
        tk.Button(self, text="Track my requests", font=("Arial", 12), width=12, height=1, command=self.track).pack()

    def submit(self):
        itemid = self.itemid.get()
        result = Request().submit_request(self.customerid, itemid)#ifwarranty need to be changed
        if result[0] == 0 or 1:
            messagebox.showinfo("showinfo", result[1])
            self.itemidentry.delete(0, tk.END)
        else:
            return result[1]

    def track(self):
        pass


Request_Page(tk.Tk(), '1').mainloop()