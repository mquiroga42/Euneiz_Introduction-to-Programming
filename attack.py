import requests

url = "https://alavabus.araba.eus/SalesPortalRestService-1/searchTicketConsult"

with open("hex.txt", "r") as archivo:
    for ticket in archivo:
        response = requests.get(url, params={"saleCode": "B8270E007613BD01", "lang":1})
        if response.status_code == 200:
            data = response.text
            print("OK " + ticket, response.status_code)
        else:
            print("Fail " + ticket, response.status_code)
