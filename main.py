import requests
from bs4 import BeautifulSoup as soup
import csv

source = requests.get('https://saras.cbse.gov.in/saras/AffiliatedList/ListOfSchdirReportNew?ID1=D')

# Convert to beautiful soup object
webpage = soup(source.content, features="html.parser")

# print(webpage.prettify())

sNo = []
regNo = []
state =[]
district = []
status = []
schoolName = []
affiliationStatus = []
region = []
details = []

# for i in webpage.find_all(class_ = 'table table-bordered dataTable no-footer'):
#     string =i.td.text
#     print(string)
#     sNo.append(string.strip())

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html, "html.parser")

# Locate the table by its tag (e.g., <table>) or by a specific identifier (e.g., id="mytable")
table = webpage.find("table")


data = []
for row in table.find_all("tr"):
    row_data = [cell.get_text(strip=True) for cell in row.find_all("td")]
    data.append(row_data)

# Now, 'data' contains the table data in a list format.


# import csv

with open("table_data.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)
