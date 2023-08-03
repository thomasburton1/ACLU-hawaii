import tkinter as tk
from tkinter import ttk
import aclu
import emoji
from functools import partial


# icon by
# <a href="https://www.flaticon.com/free-icons/law" title="law icons">Law icons created by Freepik - Flaticon</a>


# create tkinter window
window = tk.Tk()

# set window title
window.title("ACLU Hawaii")

# set window size to full screen width
window.geometry("1200x600")

# default keywords
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

def buildInterface(inputted_keywords):
    # add widgets
    keywords_frame = tk.Frame(window)

    # create label to indicate keywords text box
    keyword_label = tk.Label(keywords_frame, text="Keywords", font=('Arial', 16, "bold"),pady=8)
    keyword_label.pack()
    # load in the cases
    cases = aclu.getCases(inputted_keywords)

    # configure keyword text_box, where user can enter keywords
    keyword_textbox = tk.Text(keywords_frame, width=25)
    keyword_textbox.tag_config('keywords', font=('Arial', 14))
    keyword_textbox.insert(tk.END, "\n".join(inputted_keywords), 'keywords')
    keyword_textbox.config(padx = 15, pady=15, font=('Arial', 14))
    keyword_textbox.pack()

    def refresh():
        # grab the keywords from the keyword_textbox
        new_keywords = keyword_textbox.get('1.0', tk.END).splitlines()
        # remove all instances of empty strings in the list
        new_keywords = list(filter(lambda x: x != '', new_keywords)) 
        for widget in window.winfo_children():
            widget.destroy()
        buildInterface(new_keywords)

    # refresh button for cases
    refresh_button = tk.Button(master=keywords_frame,
        text="Refresh",
        command=refresh
    )
    refresh_button.pack()

    keywords_frame.pack(side=tk.RIGHT, fill='both',padx=15,pady=15)

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

    select_buttons = []

    def updateFocusedCase(title_x, date_x, description_x, textbox_x, button_x):
        for button in select_buttons:
            button.config(fg='black')

        textbox_x.delete('1.0', tk.END)
        textbox_x.insert(tk.END, title_x+"\n", "title")
        textbox_x.insert(tk.END, date_x+"\n", "description")
        textbox_x.insert(tk.END, description_x+"\n", "description")
        highlightKeywords(inputted_keywords, textbox_x)
        button_x.config(fg='green')

    # create text box for cases
    case_textbox = tk.Text(cases_frame, width=180)
    case_textbox.config(padx = 15, pady=15)



    col_len = 4
    for i in range(1, len(cases)+1): # for each row
        casenum = 0
        title = cases[i-1][0]
        date = cases[i-1][1]
        description = cases[i-1][2]
        alert = ""
        # check to see if we found any keywords
        keywords_found = []
        for keyword in inputted_keywords:
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
        e4 = tk.Label(table_frame ,font=('Arial',16), text=', '.join(keywords_found))
        e4.grid(row=i, column=3)
        e5 = tk.Button(table_frame, text="Select")
        e5.config(command=partial(updateFocusedCase, title, date, description, case_textbox, e5))
        e5.grid(row=i, column=4)
        select_buttons.append(e5)

    table_frame.pack()

    description_label = tk.Label(cases_frame, text="Description", font=('Arial', 16, "bold"),pady=8)
    description_label.pack()

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


    highlightKeywords(inputted_keywords, case_textbox)

    cases_frame.pack(side=tk.LEFT, fill='both',padx=15,pady=15)

    window.mainloop()

buildInterface(keywords)