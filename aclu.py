import requests
from bs4 import BeautifulSoup

'''
Idea: use GPT model to summarize the cases for easier reading
'''

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

URL = "https://www.courts.state.hi.us/courts/oral_arguments/oral_arguments_schedule"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

rows = soup.findAll("table")[0].findAll("tr")

cases = []

for row in rows:
    print()
    cells = row.findChildren('td')
    for cell in cells:
        case = []

        text = cell.findChildren(["p", "h3"])
        for item in text:
            print(item)
            if "No. " in item.text:
               case.append(item.text)
            if "Brief Description" in item.text:
                summary = ""
                descriptions = item.find_next_siblings()
                for description in descriptions:
                    summary += description.text
                case.append(summary)
        cases.append(case)

print()
for case in cases:
    print()
    for detail in case:
        print(detail)
        
