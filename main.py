from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

Keywords = input('Enter your Keywords: \n')
api = finding(appid='SBX-b321051395ab-4bdd-424d-8603-2373',config_file=None)
api_request = { 'keywords': Keywords, 'outputSelector': 'SellerInfo'}

response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content, 'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

input(items[0])

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower().strip()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()
    seller = item.sellerusername.test.lower()
    listingtype = item.listingtype.string.lower()
    condition = item.conditiondisplayname.string.lower()

    print('________________')
    print(cat)
    print()
    print(title)
    print()
    print(price)
    print()
    print(url)
    print()
    print(seller)
    print()
    print(listingtype)
    print()
    print(condition)
    print()

#response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")

#code = response.status_code
#print(code)

#if code == 200:
#    print(response.json())
