from tkinter import *
from tkinter import messagebox

class BankAccount:


    def __init__(self):
        self.balance = 100

        self.window = Tk()

        window_width = 310
        window_height = 300

        # find width and height of the screen
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # find x and y coordinates of the app
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_width / 2)

        self.window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

        self.window.title("SNB")


        # login frame
        self.frame_login = Frame(self.window, width=150, height=200, bg="white")
        # frame_login widgets
        self.heading = Label(self.frame_login, text="LOGIN", font=('Poppins 23'))
        self.heading.pack(pady=5)

        self.username = Label(self.frame_login, text="username *", height=1, bg="white", fg="black", font=('Poppins 12'))
        self.username.pack(pady=5)

        self.e_name = Entry(self.frame_login, width=25,  font=("", 15))
        self.e_name.pack(pady=5)

        self.password = Label(self.frame_login, text="password *", height=1,  bg="white", fg="black", font=('Poppins 12'))
        self.password.pack(pady=5)

        self.e_password = Entry(self.frame_login, width=25,  show='*', font=("", 15), highlightthickness=10)
        self.e_password.pack(pady=5)

        self.button_confirm = Button(self.frame_login, text="Login", width=39, height=2, font=("Ivy 9 bold"), command=self.check_password)
        self.button_confirm.pack(pady=5)

        self.frame_login.pack()


        #main menu frame
        self.frame_main = Frame(self.window, width=310, height=400)

        welcome_msg = Label(self.frame_main, text="Thank You for Choosing DAH Bank\nPlease Select One of the Services" , height=3, font=('Poppins 12'))
        welcome_msg.pack(pady=5)

        but_withdraw = Button(self.frame_main, text='Withdraw', command=self.dis_withdraw_frame, font=("Ivy 9 bold"))
        but_withdraw.pack(pady=5)

        but_deposit = Button(self.frame_main, text='Deposit', command= self.dis_deposit_frame, font=("Ivy 9 bold"))
        but_deposit.pack(pady=5)

        but_display_bal = Button(self.frame_main, text='Display Balance', command= self.dis_display_frame, font=("Ivy 9 bold"))
        but_display_bal.pack(pady=5)


        #withdraw frame
        self.frame_withdraw = Frame(self.window)
        withdraw_amount = Label(self.frame_withdraw, text="Enter the amount you would like to withdraw", font=('Poppins 12'))
        withdraw_amount.pack(pady=5)

        self.entry_withdraw = Entry(self.frame_withdraw, font=('Arial',12))
        self.entry_withdraw.pack(pady=5)

        self.btn_withdraw_amount = Button(self.frame_withdraw, text='Click Here is the Amount is Correct', command = self.withdraw, font=("Ivy 9 bold"))
        self.btn_withdraw_amount.pack(pady=5)

        self.updated_balance_label = Label(self.frame_withdraw, text='', font=("Ivy 9 bold"))
        self.updated_balance_label.pack(pady=5)


        #deposit frame
        self.frame_deposit = Frame(self.window)

        deposit_amount = Label(self.frame_deposit, text="Enter the amount you would like to deposit", font=('Poppins 12'))
        deposit_amount.pack(pady=5)

        self.entry_deposit = Entry(self.frame_deposit, font=('Arial',26))
        self.entry_deposit.pack(pady=5)

        self.btn_deposit_amount = Button(self.frame_deposit, text='Click Here is the Amount is Correct', command = self.deposit)
        self.btn_deposit_amount.pack(pady=5)

        self.updated_balance_label2 = Label(self.frame_deposit, text=' ')
        self.updated_balance_label2.pack(pady=5)


        #DISPLAY FRAME
        self.frame_display = Frame(self.window)
        self.display_balance_label = Label(self.frame_display, text= f'current balance is {self.balance}')
        self.display_balance_label.pack(pady=5)


        self.window.mainloop()


    # button commands
    def withdraw(self):
        self.balance -= float(self.entry_withdraw.get())
        self.updated_balance_label.config(text = 'Your New Balance is ' + str(self.balance))

    def deposit(self):
        self.balance += float(self.entry_deposit.get())
        self.updated_balance_label2.config(text = 'Your New Balance is ' + str(self.balance))


    #Followings will be called when clicked on display, withdraw, and deposit methods from Main Menu
    def dis_deposit_frame(self):
        self.frame_deposit.pack()
        self.frame_main.pack_forget()

    def dis_withdraw_frame(self):
        self.frame_withdraw.pack()
        self.frame_main.pack_forget()

    def dis_display_frame(self):
        self.frame_display.pack()
        self.frame_main.pack_forget()


    ###############################


    def check_password(self):
        name = self.e_name.get()
        password = str(self.e_password.get())
        if name == 'admin' and password == 'admin':
            messagebox.showinfo('Login', 'Welcome Admin!')
            self.frame_login.pack_forget()
            self.frame_main.pack()
        elif name == 'salma' and password == '123':
            messagebox.showinfo('Login', 'Welcome Back ' + 'salma')
            self.frame_login.pack_forget()
            self.frame_main.pack()
        else:
            messagebox.showwarning('Error', 'Invalid username or password')


#Create an Object to run the program
a=BankAccount()
