from tkinter import *

FONT = ("Arial", 12, "bold")


class Prompt:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(width=300, height=100)
        self.window.config(padx=20, pady=20)
        self.can = Canvas(width=425, height=225, highlightthickness=0, )
        self.pic = PhotoImage(file="images/img_1.png")
        self.can.create_image(210, 100, image=self.pic)
        self.can.grid(row=0, column=0, columnspan=2)
        self.window.title("Google Meet Automation")
        self.lab1 = Label(text="Enter meeting link: ", font=FONT)
        self.lab1.config(padx=10, pady=10)
        self.lab1.grid(row=1, column=0)
        self.link = Entry(width=35)
        self.link.grid(row=1, column=1)
        self.joinpic = PhotoImage(file="images/button_join-now.png")
        self.joinbutton = Button(image=self.joinpic, highlightthickness=0, command=self.send_link)
        self.joinbutton.grid(row=2, column=0, columnspan=2)
        self.window.mainloop()

    def send_link(self):
        self.window.quit()
        self.link_text = self.link.get()

    def get_link(self):
        return self.link_text
