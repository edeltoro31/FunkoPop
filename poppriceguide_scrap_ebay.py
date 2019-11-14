				    ebay_url = "https://www.ebay.com/sch/"+item_name[i].text
				    response = requests.get(ebay_url)
				    soup = BeautifulSoup(response.text, "html.parser")
				    cost = soup.findAll("span", {"class": "s-item__price"})
				    cost_sum = 0
				    avg_cost = 0
				    for c in range(len(cost)):
				    	cost_split = cost[c].text.split()
				    	cost_sum += float(cost_split[0][1:len(cost_split[0])])
				    if len(cost) == 0:
				    avg_cost = 0
			        else:
			    	avg_cost = cost_sum / len(cost)