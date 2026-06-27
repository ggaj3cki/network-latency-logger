import pinging
import gui
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    app = gui.Program(root)
    root.mainloop()

    interv = app.input_catcher()[0]
    time_run = app.input_catcher()[1]

    pinging.pinger(interv, time_run)


