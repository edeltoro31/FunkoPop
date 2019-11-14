import requests
from bs4 import BeautifulSoup
import csv  # needed to write data on a CSV file
import time


# We need to tell what url we are going to access


# choose a file name to save the data
filename = 'scrap.csv'

with open(filename, 'w') as csv_file:
	writer = csv.writer(csv_file)

	for x in range(59):

		url = 'https://www.poppriceguide.com/guide/searchresults.php?search=All%20&page='+str(x + 1)
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
		#for i in item_value
		# item_value = item_value[i].text
		# for i in item_value:
		#     print(i)
		# item_value = item_value.text.strip()
		#

		description = soup.findAll("div", {"class": "textcontainer"})
		# description = description.text.strip()

		own_want = soup.findAll("div", {"class": ["col-50white", "col-50green"] })


		#print(len(own_want))
		j = 0
		# open a csv file 'w' meaning write
		    # using for loop to write on CSV file
		for i in range(len(item_name)):
		    item_val = item_value[i].text.split()
		    own = float(own_want[i*2].text.replace("Own", ""))
		    if own == 0:
		    	own = 1
		    want = float(own_want[(i*2)+1].text.replace("Want", ""))
		    if item_val[0] == "--":
		        value = 0
		    else:
		        value = float(item_val[0][1:len(item_val[0])])
		    if value != 0:
		    	writer.writerow([item_name[i].text, value, own, want, "{0:.5f}".format(want / own), description[j].text])

		    j+=1
		    j+=1
		        #writer.writerow([lists[i]['itemname'], lists[i]['itemvalue'], lists[i]['textcontainer']])
		time.sleep(4)