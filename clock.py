import tkinter as tk
import datetime as dt

def update_time():
    now = dt.datetime.now()
    hr = now.hour
    if hr > 12:
        hr -= 12
    if hr == 0:
        hr = 12
    time_str = f"{str(hr).zfill(2)}:{str(now.minute).zfill(2)}:{str(now.second).zfill(2)}"
    date_str = now.strftime("%A, %B %d, %Y")

    time_label.config(text=time_str)
    date_label.config(text=date_str)

    root.after(1000, update_time)

root = tk.Tk()
root.title("Fullscreen Clock")
root.attributes('-fullscreen', True)
root.configure(bg='black')

# Exit fullscreen on Escape key
root.bind("<Escape>", lambda e: root.destroy())

time_label = tk.Label(root, font=("Times New Roman", 150, "bold"), fg="white", bg="black")
time_label.pack(expand=True)

date_label = tk.Label(root, font=("Brush Script MT", 40), fg="white", bg="black")
date_label.pack()

update_time()
root.mainloop()



