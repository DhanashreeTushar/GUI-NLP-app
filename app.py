from tkinter import *
from mydb import database
from tkinter import messagebox
from myapi import API

class NLPapp():
    def __init__(self):

        # creation of db object
        self.dbo = database()
        self.apio = API()

        # login GUI creation

        self.root = Tk()
        self.root.title('NLP app')
        self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry('350x600')
        self.root.config(bg = '#748790')

        self.login_gui()
        self.root.mainloop() # used to hold gui on screen

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text = 'NLP app',bg = '#748790',fg = 'white')
        heading.pack(pady = (30,30))
        heading.config(font = ('verdana',20,'bold'))

        # adding email and password
        label1 = Label(self.root , text = 'Enter Email')
        label1.pack(pady =(10,10))

        self.email = Entry(self.root,width = 30)
        self.email.pack(pady = (5,10),ipady = 4)

        label2 = Label(self.root , text = 'Enter password')
        label2.pack(pady =(10,10))

        self.password = Entry(self.root,width = 30,show = '*')
        self.password.pack(pady = (5,10),ipady = 4)

        # adding button login

        login_button = Button(self.root,text= 'Login',width = 30,height = 2,command = self.perform_login)
        login_button.pack(pady=(10,10))

        # adding label n button of "already a member"

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_button = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_button.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text='NLP app', bg='#748790', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 20, 'bold'))

        # adding name, email and password
        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name = Entry(self.root, width=30)
        self.name.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email = Entry(self.root, width=30)
        self.email.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter password')
        label2.pack(pady=(10, 10))

        self.password = Entry(self.root, width=30, show='*')
        self.password.pack(pady=(5, 10), ipady=4)

        # adding button login

        register_button = Button(self.root, text='Register', width=30, height=2, command = self.perform_registration)
        register_button.pack(pady=(10, 10))

        # adding label n button of "already a member"

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_button = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_button.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        # fetch the data from user inputs
        name = self.name.get()
        password = self.password.get()
        email = self.email.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success' , 'registration successful.You can register now')
        else:
            messagebox.showerror('Error', 'email already exists')


    def perform_login(self):
        password = self.password.get()
        email = self.email.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Please enter correct credentials')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP app', bg='#748790', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 20, 'bold'))

        sentiment_button = Button(self.root, text='Sentiment Analysis', width =30  ,height = 4,command = self.sentiment_gui)
        sentiment_button.pack(pady=(10, 10))

        ner_button = Button(self.root, text='Named Entity Recognition', width=30, height=4)
        ner_button.pack(pady=(10, 10))

        emotion_button = Button(self.root, text='Emotion Prediction', width=30, height=4)
        emotion_button.pack(pady=(10, 10))

        logout_button = Button(self.root, text='Login Now', command=self.login_gui)
        logout_button.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP app', bg='#748790', fg='white')
        heading.pack(pady=(30, 30))
        heading.config(font=('verdana', 20, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#748790', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.config(font=('verdana', 20, 'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=30,)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_button = Button(self.root, text='Analyze sentiment',command = self.do_sent_anaysis)
        sentiment_button.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg = '#748790', fg = 'white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.config(font=('verdana', 16))


        go_back_button = Button(self.root, text='Go Back',command=self.login_gui)
        go_back_button.pack(pady=(10, 10))


    def do_sent_anaysis(self):
        text = self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)

        print(result)

nlp = NLPapp()
