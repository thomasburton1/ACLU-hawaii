import tkinter as tk
from tkinter import ttk
import aclu
import emoji

# create tkinter window
window = tk.Tk()

# set window title
window.title("ACLU Hawaii")

# set window size to full screen width
window.geometry(str(window.winfo_screenwidth())+"x"+str(window.winfo_screenheight()))

# add widgets
title = tk.Label(text="Yo")
title.pack()

keywords = "constitution\npolice\ntitle iv\ntitle ix\nhomeless\ncivil right\nfreedom of speech\nbill of rights\nLGBT\nvote\namendment\nbail\ndiscrimination\nabortion\nfirst amendment\neighth amendment"

keyword_textbox = tk.Text(window)
keyword_textbox.insert(tk.END, keywords)
keyword_textbox.pack()

refresh_button = tk.Button(
    text="Refresh",
    width=6,
    height=2,
    bg="white",
    fg="black",
)
refresh_button.pack()




#print(emoji.emojize(":thumbs_up:"))

window.mainloop()



