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

keyword_label = tk.Label(text="Keywords")
keyword_label.pack()

keywords = ["constitution",
                "police",
                "title iv",
                "title ix",
                "homeless",
                "civil right", 
                "freedom of speech",
                "bill of rights",
                "LGBT",
                "vote",
                "amendment",
                "bail",
                "discrimination",
                "abortion",
                "first amendment",
                "eighth amendment"]

keyword_textbox = tk.Text(window, width=25)
keyword_textbox.insert(tk.END, "\n".join(keywords))
keyword_textbox.pack()

refresh_button = tk.Button(
    text="Refresh",
    width=6,
    height=2,
    bg="white",
    fg="black",
    command= aclu.getCases
)

refresh_button.pack()

cases_label = tk.Label(text="Cases")
cases_label.pack()

cases = aclu.getCases()

# create text box for cases
case_textbox = tk.Text(window, width=180)
case_textbox.config(padx = 15, pady=15)
case_textbox.pack()

case_textbox.tag_config('keyword', background="yellow", foreground="black")

for case in cases:
    title = case[0]
    description = case[1]
    #case_title = tk.Label(text=title)
    #case_title.pack()
    #case_description = tk.Label(text=description)
    #case_description.pack()
    case_textbox.insert(tk.END, title+"\n", "keyword")
    case_textbox.insert(tk.END, description+"\n")
    case_textbox.insert(tk.END, "\n")

#print(emoji.emojize(":thumbs_up:"))

case_textbox.tag_remove('found', '1.0', tk.END)
     
def highlightKeywords(keywords_args, textbox):
    for keyword in keywords_args:
        idx = '1.0'
        while 1:
                #searches for desired string from index 1
            idx = textbox.search(keyword, idx, nocase=1,stopindex=tk.END)
            if not idx: break
                    
                #last index sum of current index and
                #length of text
            lastidx = '%s+%dc' % (idx, len(keyword))
                    
                #overwrite 'Found' at idx
            textbox.tag_add('found', idx, lastidx)
            idx = lastidx
                
        textbox.tag_config('found', foreground='red')


highlightKeywords(keywords, case_textbox)


window.mainloop()