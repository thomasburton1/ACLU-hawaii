# ACLU-hawaii

## CaseWatcher

### Description:
This application was developed for the ACLU of Hawaii. Built using Python 3 and the Tkinter GUI module, it assists them in their legal practice by monitoring supreme court oral arguments related to relevant issues. 

Supreme Court of Hawaii (oral arguments): https://www.courts.state.hi.us/courts/oral_arguments/oral_arguments_schedule

### Features: 
- Live web-scraping using BeautifulSoup
- Keyword specification and highlighting
- Custom GUI, allowing users to specify keywords, pull new data from supreme court website, and identify time-sensitive court events.

### Building Project:
- Clone the project to your local environment
- Navigate to ACLU-hawaii repository 
- Run app through terminal with command: ```python3 gui.py```
- Build into app bundle (Mac OSX) or executable (.EXE) using pyinstaller: ```pyinstaller --onefile --windowed --name CaseWatcher gui.py```
- For more information on how to build specifically for your machine: https://pyinstaller.org/en/stable/usage.html

### Potential Future Updates: 
- Experiment with CustomTkinter (https://github.com/TomSchimansky/CustomTkinter) to make GUI more modern and sleek (also nice to practice with a new GUI module)
- Utilize a GPT model to help summarize court cases (since many of these descriptions are length and very detailed), save attorneys' time 
- Create web-links in the app which opens a web browser to the specific part of the website with the information summarized
