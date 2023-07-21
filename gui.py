import tkinter as tk
from tkinter import ttk
import aclu
import emoji

# create tkinter window
window = tk.Tk()

# set window title
window.title("ACLU Hawaii")

# set window size to full screen width
window.geometry("1200x600")

# add widgets
keywords_frame = tk.Frame(window)

keyword_label = tk.Label(keywords_frame, text="Keywords", font=('Arial', 16, "bold"),pady=8)
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

keyword_textbox = tk.Text(keywords_frame, width=25)
keyword_textbox.tag_config('keywords', font=('Arial', 14))
keyword_textbox.insert(tk.END, "\n".join(keywords), 'keywords')
keyword_textbox.config(padx = 15, pady=15)
keyword_textbox.pack()

# refresh button for cases
refresh_button = tk.Button(master=keywords_frame,
    text="Refresh",
    command= aclu.getCases
)
refresh_button.pack()

keywords_frame.pack(side=tk.RIGHT, fill='both',padx=15,pady=15)

# load in the cases
cases = aclu.getCases()



# table for basic case information and alerts

# row structure: 
# alert emoji | case number | date | keywords found

cases_frame = tk.Frame(window)
cases_label = tk.Label(cases_frame, text="Cases", font=('Arial', 16, "bold"),pady=8)
cases_label.pack()

table_frame = tk.Frame(cases_frame)

x1 = tk.Label(table_frame ,font=('Arial',16, "bold"), text="Alert")
x1.grid(row=0, column=0)
x2 = tk.Label(table_frame ,font=('Arial',16, "bold"), text="Case Number")
x2.grid(row=0, column=1)
x3 = tk.Label(table_frame ,font=('Arial',16, "bold"), text="Date & Time")
x3.grid(row=0, column=2)
x4 = tk.Label(table_frame ,font=('Arial',16, "bold"), text="Keywords Found")
x4.grid(row=0, column=3)

col_len = 4
for i in range(1, len(cases)+1): # for each row
    casenum = 0
    title = cases[i-1][0]
    date = cases[i-1][1]
    description = cases[i-1][2]
    alert = ""
    # check to see if we found any keywords
    keywords_found = []
    for keyword in keywords:
        if keyword in description:
            keywords_found.append(keyword)
    if len(keywords_found) > 0:
        alert = emoji.emojize(":police_car_light:")
    else:
        alert = emoji.emojize("🙃")

    e1 = tk.Label(table_frame ,font=('Arial',16), text=alert)
    e1.grid(row=i, column=0)
    e2 = tk.Label(table_frame ,font=('Arial',16), text=title)
    e2.grid(row=i, column=1)
    e3 = tk.Label(table_frame ,font=('Arial',16), text=date)
    e3.grid(row=i, column=2)
    e4 = tk.Label(table_frame ,font=('Arial',16), text=keywords_found)
    e4.grid(row=i, column=3)
    e5 = tk.Button(table_frame, text="Select", command=(lambda: updateFocusedCase(title, date, description, case_textbox, e5)))
    e5.grid(row=i, column=4)

def updateFocusedCase(title, date, description, textbox, button):
    textbox.delete('1.0', tk.END)
    textbox.insert(tk.END, title+"\n", "title")
    textbox.insert(tk.END, date+"\n", "description")
    textbox.insert(tk.END, description+"\n", "description")
    highlightKeywords(keywords, textbox)
    button.config(fg='green')

table_frame.pack()

description_label = tk.Label(cases_frame, text="Description", font=('Arial', 16, "bold"),pady=8)
description_label.pack()

# create text box for cases
case_textbox = tk.Text(cases_frame, width=180)
case_textbox.config(padx = 15, pady=15)
case_textbox.pack()

case_textbox.tag_config('title', font=('Arial',18,'bold'))
case_textbox.tag_config('description', font=('Arial', 14))

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
                
        textbox.tag_config('found', background='yellow')


highlightKeywords(keywords, case_textbox)

cases_frame.pack(side=tk.LEFT, fill='both',padx=15,pady=15)

window.mainloop()