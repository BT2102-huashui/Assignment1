import tkinter as tk
from tkinter import messagebox, ttk
from Customers import *
from Admins import *


class Main_Page(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Main Page")
        self.geometry("350x350")
        tk.Label(text="Login and Registeration", font=("Calibri", 20)).pack()
        tk.Button(self, text="Admins Login", font=("Arial", 12), width=12, height=1, command=self.call_admin_login).pack()
        tk.Button(self, text="Customer Login", font=("Arial", 12), width=12, height=1, command=self.call_cust_login).pack()
        tk.Button(self, text="Register as administrators", font=("Arial", 12), width=18, height=1, command=self.call_admin_regis).pack()
        tk.Button(self, text="Register as customers", font=("Arial", 12), width=18, height=1, command=self.call_cust_regis).pack()

    def call_admin_login(self):
        Login_Admin_Page(self)

    def call_cust_login(self):
        Login_Cust_Page(self)

    def call_admin_regis(self):
        Register_Admin_Page(self)

    def call_cust_regis(self):
        Register_Cust_Page(self)

class Login_Admin_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.title("Login the system as admin")
        self.geometry("350x350")

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

        result = Administrator().login(userid, password)
        if result[1]:
            messagebox.showinfo("showinfo", result[0])
            self.call_search()
        else:
            messagebox.showinfo("showinfo", result[0])
            self.usrentry.delete(0, tk.END)
            self.passentry.delete(0, tk.END)
        

    def call_search(self):
        self.clear_widgets()
        Search_Admin_Page(self)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        
class Login_Cust_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.title("Login the system")
        self.geometry("350x350")

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
            self.call_search()
        else:
            messagebox.showinfo("showinfo", result[0])
            self.usrentry.delete(0, tk.END)
            self.passentry.delete(0, tk.END)

    def call_search(self):
        self.clear_widgets()
        Search_Cust_Page(self)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

class Register_Admin_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.master.title("Register Page")
        self.geometry("350x350")

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
        tk.Label(self, text="Your User ID").pack()
        self.usrentry = tk.Entry(self, textvariable=self.username)
        self.usrentry.pack()
        tk.Label(self, text="Password").pack()
        self.passentry = tk.Entry(self, textvariable=self.password)
        self.passentry.pack()
        tk.Label(self, text="Gender").pack()
        self.gender = ttk.Combobox(self, width="10", values=("Female", "Male"))
        self.gender.pack()
        

        tk.Button(self, text="Register", font=("Arial", 12), width=15, height=1, command=self.register_user).pack()

    def register_user(self):
        if self.checkcmbo():
            userid = self.username.get()
            password = self.password.get()
            gender = self.gender.get()
            result = Administrator().registration(userid, password, gender)
            if result[1]:
                messagebox.showinfo("showinfo", result[0])
            else:
                messagebox.showwarning("showwarning", result[0])
        else:
            messagebox.showwarning("showwarning", "Plz fill all the box")
        self.usrentry.delete(0, tk.END)
        self.passentry.delete(0, tk.END)
        self.gender.delete(0, tk.END)
        

    def checkcmbo(self):

        if self.gender.get() == "Female":
            return "Female"
        elif self.gender.get() == "Male":
            return "Male"
        else:
            return False


class Register_Cust_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.master.title("Register Page")
        self.geometry("350x350")

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        tk.Label(self, text="Your User ID").pack()
        self.usrentry = tk.Entry(self, textvariable=self.username)
        self.usrentry.pack()
        tk.Label(self, text="password").pack()
        self.passentry = tk.Entry(self, textvariable=self.password)
        self.passentry.pack()

        tk.Button(self, text="Register", font=("Arial", 12), width=15, height=1, command=self.register_user).pack()

    def register_user(self):
        userid = self.username.get()
        password = self.password.get()

        result = Customer().registration(userid, password)
        if result[1]:
            messagebox.showinfo("showinfo", result[0])
        else:
            messagebox.showwarning("showwarning", result[0])

        self.usrentry.delete(0, tk.END)
        self.passentry.delete(0, tk.END)

class Search_Admin_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.master.destroy()
        self.title("Search Page")
        self.geometry("350x350")
        tk.Label(self, text="Administrator Management", font=("Calibri", 20)).pack()
        tk.Button(self, text="Display the sold items", font=("Arial", 12), width=20, height=1, command=self.display_items).pack()
        tk.Button(self, text="Exit", font=("Arial", 12), width=11, height=1, command=self.close).pack()

    def close(self):
        self.destroy()

    def display_items(self):
        Display_Item_Page(self)


class Search_Cust_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.master.destroy()
        self.title("Search Page")
        self.geometry("350x350")
        tk.Label(self, text="Search your item", font=("Calibri", 20)).pack()
        tk.Button(self, text="Search", font=("Arial", 12), width=11, height=1).pack()
        tk.Button(self, text="Exit", font=("Arial", 12), width=11, height=1, command=self.close).pack()
    
    def close(self):
        self.destroy()

class Display_Item_Page(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.title("Display the Items Page")
        self.geometry("500x350")
        tk.Label(self, text="Items Sold and Unsold", font=("Calibri", 20)).pack()
        table = ttk.Treeview(self)
        table["columns"] = ("IID", "Sold", "Unsold")
        table.column('#0', width=0, stretch=tk.NO)
        table.column('IID', anchor=tk.CENTER, width=100)
        table.column('Sold', anchor=tk.CENTER, width=100)
        table.column('Unsold', anchor=tk.CENTER, width=100)
        table.heading('#0', text='', anchor=tk.CENTER)
        table.heading('IID', text='IID', anchor=tk.CENTER)
        table.heading('Sold', text='Sold', anchor=tk.CENTER)
        table.heading('Unsold', text='Unsold', anchor=tk.CENTER)

        values = Administrator().product_manage()
        for i in range(len(values)):
            table.insert(parent='', index=i, iid=i, text='', values=values[i])
        table.pack()
        # tk.Button(self, text="Search", font=("Arial", 12), width=11, height=1).pack()
        # tk.Button(self, text="Exit", font=("Arial", 12), width=11, height=1, command=self.close).pack()

        

Main_Page().mainloop()
