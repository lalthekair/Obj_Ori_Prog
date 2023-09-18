from tkinter import *
from tkinter import messagebox
# we are doing 5 interfaces to work with the class; I need to link them and have them interact


class BankAccount:

    def __init__(self):
        self.balance = 100
        self.window = Tk()  # grandparent
        # parent is frame (login, withdraw, check balance, deposit)
        # widgets are children (buttons, labels, entry) - which is why we did this in a class

    # variable without self means that only the init can access these variables (ideally, only frames would be init)
    # self.variable means the variable will be usable anywhere in the class
    # can be inside or outside the constructor or the main, or in other classes as well; better outside bank class
        window_width = 350
        window_height = 300
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
        self.window.title("Bank Software")

        # login frame
        self.frame_login = Frame(self.window, width=310, height=300, bg="white")
        self.heading = Label(self.frame_login, text="LOGIN", bg="white", font='Poppins 23')
        self.heading.pack(pady=5)
        self.username = Label(self.frame_login, text="username *", height=1, bg="white", fg="black", font='Poppins 12')
        self.username.pack(pady=5)
        self.e_name = Entry(self.frame_login, width=25,  font=('Poppins', 15))
        self.e_name.pack(pady=5)
        self.password = Label(self.frame_login, text="password *", height=1,  bg="white", fg="black", font='Poppins 12')
        self.password.pack(pady=5)
        self.e_password = Entry(self.frame_login, width=25,  show='*', font=("", 15), highlightthickness=1)
        self.e_password.pack(pady=5)
        self.button_confirm = Button(self.frame_login, text="Login", width=39, height=2, font="Ivy 9 bold",
                                     command=self.check_password)
        self.button_confirm.pack(padx=5)
        self.frame_login.pack()

        # main frame
        self.frame_main = Frame(self.window, width=310, height=300, bg='white')
        self.welcome_msg = Label(self.frame_main, text="Thank you for choosing SNB.\nPlease select a service below.",
                                 height=3, font='Poppins 12', bg='white')
        self.welcome_msg.pack(pady=5)
        self.but_withdraw = Button(self.frame_main, text='Withdraw', command=self.dis_withdraw_frame, font="Ivy 9 bold")
        self.but_withdraw.pack(pady=5)
        self.but_deposit = Button(self.frame_main, text='Deposit', command=self.dis_deposit_frame, font="Ivy 9 bold")
        self.but_deposit.pack(pady=5)
        self.but_display_bal = Button(self.frame_main, text='Display Balance', command=self.dis_display_frame,
                                      font="Ivy 9 bold")
        self.but_display_bal.pack(pady=5)
        self.but_logout = Button(self.frame_main, text='Logout', font="Ivy 9 bold", command=self.dis_logout)
        self.but_logout.pack(pady=30)

        # withdraw frame
        self.frame_withdraw = Frame(self.window)
        withdraw_amount = Label(self.frame_withdraw, text="Enter the amount you would like to withdraw",
                                font='Poppins 12')
        withdraw_amount.pack(pady=5)
        self.entry_withdraw = Entry(self.frame_withdraw, font=('Arial', 12))
        self.entry_withdraw.pack(pady=5)
        self.btn_withdraw_amount = Button(self.frame_withdraw, text='Confirm', command=self.withdraw, font="Ivy 9 bold")
        self.btn_withdraw_amount.pack(pady=5)
        self.updated_balance_label = Label(self.frame_withdraw, text='', font="Ivy 9 bold")
        self.updated_balance_label.pack(pady=5)
        self.but_back = Button(self.frame_withdraw, text='Back', command=self.dis_main_menu)
        self.but_back.pack()

        # deposit frame
        self.frame_deposit = Frame(self.window)
        deposit_amount = Label(self.frame_deposit, text="Enter the amount you would like to deposit", font='Poppins 12')
        deposit_amount.pack(pady=5)
        self.entry_deposit = Entry(self.frame_deposit, font=('Arial', 26))
        self.entry_deposit.pack(pady=5)
        self.btn_deposit_amount = Button(self.frame_deposit, text='Confirm', command=self.deposit)
        self.btn_deposit_amount.pack(pady=5)
        self.updated_balance_label2 = Label(self.frame_deposit, text='')
        self.updated_balance_label2.pack(pady=5)
        self.but_back2 = Button(self.frame_deposit, text='Back', command=self.dis_main_menu)
        self.but_back2.pack()

        # display frame
        self.frame_display = Frame(self.window)
        self.display_balance_label = Label(self.frame_display, text='')
        self.display_balance_label.pack(pady=40)
        self.but_back3 = Button(self.frame_display, text='Back', command=self.dis_main_menu)
        self.but_back3.pack()


        self.window.mainloop()

    def check_password(self):
        name = self.e_name.get()  # take the input entered by the user and store them in this variable
        password = str(self.e_password.get())
        if name == 'admin' and password == 'admin':
            messagebox.showinfo('Login Successful', 'Welcome Admin!')
            self.frame_login.pack_forget()  # pack_forget means hide this frame, or unpack
            self.frame_main.pack()
        else:
            messagebox.showinfo('Login Failed', 'Invalid username or password.')

    def dis_withdraw_frame(self):
        self.frame_withdraw.pack()
        self.frame_main.pack_forget()

    def dis_deposit_frame(self):
        self.frame_deposit.pack()
        self.frame_main.pack_forget()

    def dis_display_frame(self):
        self.frame_display.pack()
        self.frame_main.pack_forget()
        data = 'Your current balance is ' + str(self.balance)
        self.display_balance_label.config(text=data)

    def dis_logout(self):
        messagebox.showinfo('Logout', 'User logged off successfully.')
        self.frame_main.pack_forget()
        self.frame_login.pack()
        self.e_name.delete(0, END)
        self.e_password.delete(0, END)

    def dis_main_menu(self):
        self.frame_withdraw.pack_forget()
        self.frame_deposit.pack_forget()
        self.entry_withdraw.delete(0, END)
        self.frame_display.pack_forget()
        self.entry_deposit.delete(0, END)
        self.frame_main.pack()

    def withdraw(self):
        self.balance -= float(self.entry_withdraw.get())
        self.updated_balance_label.config(text='Your new balance is ' + str(self.balance))
        # the label already exists and is packed; config merely edited the text in the label

    def deposit(self):
        self.balance += float(self.entry_deposit.get())
        self.updated_balance_label2.config(text='Your new balance is ' + str(self.balance))



def main():
    obj = BankAccount()


main()