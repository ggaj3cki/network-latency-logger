import tkinter as tk
from tkinter import messagebox as msg


class Program:

    def __init__(self, master):
        self.interval_num = tk.StringVar()
        self.hlr_num = tk.StringVar()
        self.master = master

        self.font_type = ('Arial', 20)

        self.intervals_label = tk.Label(master, text="Please enter frequency of pinging (in seconds): ", font=self.font_type)
        self.intervals_label.pack()

        self.intervals_entry = tk.Entry(master, font=self.font_type, textvariable=self.interval_num)
        self.intervals_entry.pack()

        self.hlr_label = tk.Label(master, text="Please enter how many minutes program has to work: ", font=self.font_type)
        self.hlr_label.pack()

        self.hlr_entry = tk.Entry(master, font=self.font_type, textvariable=self.hlr_num)
        self.hlr_entry.pack()

        self.int_check = tk.Label(master, text="", font=self.font_type, fg="#ff0000")
        self.int_check.pack()

        self.submit = tk.Button(master, font=self.font_type, text="Run program", relief=tk.RAISED, bd=10, cursor='hand2',command=self.input_catcher)
        self.submit.pack()

        self.mes = tk.Label(master, font=self.font_type, text="After click 'Run program' button close the window")
        self.mes.pack()


    def input_catcher(self):
        inter = self.interval_num.get()
        how_long = self.hlr_num.get()
        try:
            inter = int(inter)
            how_long = int(how_long)
            return inter, how_long
            # self.master.destroy()
        except ValueError:
            msg.showerror('ValueError', 'Only number values allowed')


if __name__ == '__main__':
    root = tk.Tk()
    app = Program(root)
    root.mainloop()
    print(app.input_catcher())
