import tkinter as tk
import threading, time

root = tk.Tk()        # create the root window

def run(func):
    threading.Thread(target=func).start()

run(lambda:     root.wm_title('FAILURE'))

root.update()
time.sleep(2)  # _tkinter.c:WaitForMainloop fails
root.mainloop()