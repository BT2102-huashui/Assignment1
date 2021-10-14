import tkinter as tk
from tkinter import StringVar, messagebox, ttk
from Customers import *
from Admins import *
from AdminsPages import *
from CustomerPages import *

WIDTH = 500
HEIGHT = 200
HEIGHT2 = 500
#The main page when open the OSHES
class Main_Page(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Main Page")

        wid_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        canva = tk.Canvas(self,width=500, height=150)
        canva.grid(columnspan=2, rowspan=4)
        x = (wid_screen/2) - (WIDTH/2)
        y = (height_screen/2) - (HEIGHT/2)
        self.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

        tk.Label(text="Welcome to \n OSHMS System", font=("Calibri", 20)).grid(column=0, row=1, rowspan=2)
        tk.Button(self, text="Admins Login", font=("Arial", 12), width=22, height=1, command=self.call_admin_login).grid(column=1, row=0)
        tk.Button(self, text="Customer Login", font=("Arial", 12), width=22, height=1, command=self.call_cust_login).grid(column=1, row=1)
        tk.Button(self, text="Register as administrators", font=("Arial", 12), width=22, height=1, command=self.call_admin_regis).grid(column=1, row=2)
        tk.Button(self, text="Register as customers", font=("Arial", 12), width=22, height=1, command=self.call_cust_regis).grid(column=1, row=3)
        tk.Button(self, text="Close", font=("Arial", 12), width=12, height=1, command=self.close).grid(column=1, row=4)

    def call_admin_login(self):
        Login_Admin_Page(self)

    def call_cust_login(self):
        Login_Cust_Page(self)

    def call_admin_regis(self):
        Register_Admin_Page(self)

    def call_cust_regis(self):
        Register_Cust_Page(self)

    def close(self):
        self.destroy()