import requests
from bs4 import BeautifulSoup
import csv  # needed to write data on a CSV file

# We need to tell what url we are going to access
url = 'https://www.poppriceguide.com/guide/Dragonball/'

# Opening up connection, grabbing the page, return the html to the variable response
response = requests.get(url)

# parse the response into BeautifulSoup format so we can use BeautifulSoup to work on it.
# store in variable 'soup'
soup = BeautifulSoup(response.text, "html.parser")

# now find all div element that has attributes called itemname, itemvalue and textcontainer
#  and store it into python list "lists"
#lists = soup.findAll("div", {"class": "itemrow"})

item_name = soup.findAll("div", {"class": "itemname"})
# item_name = item_name.text.strip()
#

item_value = soup.findAll("div", {"class": "itemvalue"})
# item_value = item_value.text.strip()
#

description = soup.findAll("div", {"class": "textcontainer"})
# description = description.text.strip()

own_want = soup.findAll("div", {"class": "col-50white"})


# choose a file name to save the data
filename = 'ppg_scrap.csv'

# open a csv file 'w' meaning write
with open(filename, 'w') as csv_file:
    writer = csv.writer(csv_file)

    # using for loop to write on CSV file
    for i in range(128):  # I am only looping 129
        writer.writerow([item_name[i].text, item_value[i].text, own_want[i].text, own_want[i+1].text, description[i].text])
        # writer.writerow([lists[i]['itemname'], lists[i]['itemvalue'], lists[i]['textcontainer']])