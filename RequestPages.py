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
        result = Request().track(int(self.customerid))
        T = tk.Text(self, height=20, width=50)
        T.pack()
        ans = ""
        l = len(result)
        if l > 0:
            for key in result:
                for i in range(3):
                    ans += str(key[i]) + " "
                ans += "\n"
        else:
            ans = "no"
        T.insert(tk.END, ans)

class See_items_buy(tk.Toplevel):
    def __init__(self, master, customerid) -> None:
        super().__init__()
        self.master = master
        self.customerid = customerid
        self.title("All Items")
        
        wid_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        x = (wid_screen/2) - (WIDTH/2)
        y = (height_screen/2) - (HEIGHT/2)
        self.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

        tk.Button(self, text="See all items purchase", font=("Arial", 12), width=12, height=1, command=self.display).pack()

    def display(self):
        result = Request().all_items(int(self.customerid))
        T = tk.Text(self, height=20, width=50)
        T.pack()
        ans = ""
        l = len(result)
        if l > 0:
            for key in result:
                for i in range(5):
                    ans += str(key[i]) + " "
                ans += "\n"
        else:
            ans = "no"
        T.insert(tk.END, ans)

#Request_Page(tk.Tk(), '1').mainloop()
#See_items_buy(tk.Tk(), '1').mainloop()
