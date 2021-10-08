import tkinter as tk
from tkinter import StringVar, messagebox, ttk
from Customers import *
from Admins import *

WIDTH = 500
HEIGHT = 350
HEIGHT2 = 500

class Login_Cust_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.title("Login the system")
        
        wid_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        x = (wid_screen/2) - (WIDTH/2)
        y = (height_screen/2) - (HEIGHT/2)
        self.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        tk.Label(self, text="Your User ID").pack()
        self.usrentry = tk.Entry(self, textvariable=self.username)
        self.usrentry.pack()
        tk.Label(self, text="password").pack()
        self.passentry = tk.Entry(self, textvariable=self.password)
        self.passentry.pack()

        tk.Button(self, text="Login", font=("Arial", 12), width=12, height=1, command=self.login).pack()

    def login(self):
        userid = self.username.get()
        password = self.password.get()

        result = Customer().login(userid, password)
        if result[1]:
            messagebox.showinfo("showinfo", result[0])
            self.call_search(userid)
        else:
            messagebox.showinfo("showinfo", result[0])
            self.usrentry.delete(0, tk.END)
            self.passentry.delete(0, tk.END)

    def call_search(self, userid):
        self.clear_widgets()
        Search_Cust_Page(self, userid)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

class Register_Cust_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.master.title("Register Page")
        wid_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        x = (wid_screen/2) - (WIDTH/2)
        y = (height_screen/2) - (HEIGHT2/2)
        self.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT2, x, y))

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.name = tk.StringVar()
        self.phone_number = tk.StringVar()
        self.address = tk.StringVar()
        self.email = tk.StringVar()

        tk.Label(self, text="Your User ID").pack()
        self.usrentry = tk.Entry(self, textvariable=self.username)
        self.usrentry.pack()

        tk.Label(self, text="Password").pack()
        self.passentry = tk.Entry(self, textvariable=self.password)
        self.passentry.pack()

        tk.Label(self, text="Name").pack()
        self.namentry = tk.Entry(self, textvariable=self.name)
        self.namentry.pack()

        tk.Label(self, text="Gender").pack()
        self.gender = ttk.Combobox(self, width="10", values=("Female", "Male"))
        self.gender.pack()

        tk.Label(self, text="Phone Number").pack()
        self.phonentry = tk.Entry(self, textvariable=self.phone_number)
        self.phonentry.pack()

        tk.Label(self, text="address").pack()
        self.adressentry = tk.Entry(self, textvariable=self.address)
        self.adressentry.pack()

        tk.Label(self, text="Email").pack()
        self.emailentry = tk.Entry(self, textvariable=self.email)
        self.emailentry.pack()

        tk.Button(self, text="Register", font=("Arial", 12), width=15, height=1, command=self.register_user).pack()
        tk.Button(self, text="Close", font=("Arial", 12), width=15, height=1, command=self.close).pack()

    def close(self):
        self.destroy()

    def register_user(self):
        try:
            userid = self.username.get()
            password = self.password.get()
            name = self.name.get()
            gender = self.gender.get()
            number = self.phone_number.get()
            address = self.address.get()
            email = self.email.get()
            result = Customer().registration(userid, password, name, gender, number, address, email)
            if result[1]:
                messagebox.showinfo("showinfo", result[0])
            else:
                messagebox.showwarning("showwarning", result[0])
        except:
            messagebox.showwarning("showwarning", "sth wrong")
        self.usrentry.delete(0, tk.END)
        self.passentry.delete(0, tk.END)
        self.namentry.delete(0, tk.END)
        self.gender.delete(0, tk.END)
        self.phonentry.delete(0, tk.END)
        self.emailentry.delete(0, tk.END)
        self.adressentry.delete(0, tk.END)

class Search_Cust_Page(tk.Toplevel):
    def __init__(self, master, userid) -> None:
        super().__init__()
        self.master = master
        self.userid = userid
        self.master.destroy()
        self.title("Search Page")
        self.geometry("350x350")
        
        wid_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        x = (wid_screen/2) - (WIDTH/2)
        y = (height_screen/2) - (HEIGHT2/2)
        self.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT2, x, y))
        tk.Label(self, text="Search your item", font=("Calibri", 20)).pack()

        self.label1 = tk.Label(self, text="Search By").pack()
        self.searchby = ttk.Combobox(self, width="10", values=("Category", "Model")).pack()

        self.label2 = tk.Label(self, text="Color").pack()
        self.colors = ttk.Combobox(self, width="10", values=("White", "Black", "Green", "Yellow")).pack()

        self.begin_year = StringVar()
        self.end_year = StringVar()
        self.begin_yearentry = tk.Entry(self, textvariable=self.begin_year)
        self.end_yearentry = tk.Entry(self, textvariable=self.end_year)
        self.label3 = tk.Label(self, text="Begin year").pack()
        self.begin_yearentry.pack()
        self.label4 = tk.Label(self, text="End year").pack()
        self.end_yearentry.pack()

        self.begin_price = StringVar()
        self.end_price = StringVar()
        self.begin_pricentry = tk.Entry(self, textvariable=self.begin_price)
        self.end_pricentry = tk.Entry(self, textvariable=self.end_price)
        self.label5 = tk.Label(self, text="Begin Price").pack()
        self.begin_pricentry.pack()
        self.label6 = tk.Label(self, text="End Price").pack()
        self.end_pricentry.pack()

        
        tk.Button(self, text="Search", font=("Arial", 12), width=11, height=1, command=self.search).pack()
        tk.Button(self, text="Exit", font=("Arial", 12), width=11, height=1, command=self.close).pack()
    
    def close(self):
        self.destroy()

    def search(self):
        print("to be done")