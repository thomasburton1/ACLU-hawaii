import requests
from bs4 import BeautifulSoup

'''
Idea: use GPT model to summarize the cases for easier reading
'''

def getCases(keywords):
    URL = "https://www.courts.state.hi.us/courts/oral_arguments/oral_arguments_schedule"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    rows = soup.findAll("table")[0].findAll("tr")

    cases = []

    for row in rows:
        #print()
        cells = row.findChildren('td')
        for cell in cells:
            case = []
            text = cell.findChildren(["p", "h3"])
            for item in text:
                #print(item)
                if "No. " in item.text:
                    details = item.text.split(',', 1)
                    # will give us [case number, date & time]
                    for x in details:
                        case.append(x)
                if "Brief Description" in item.text:
                    summary = ""
                    descriptions = item.find_next_siblings()
                    for description in descriptions:
                        summary += description.text
                    case.append(summary)

            if not len(case) == 0:
                cases.append(case)
    return cases
