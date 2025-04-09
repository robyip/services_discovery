# Url to scrape: https://www.thelivewelldirectory.com/Search?CategoryId=122&SM=ServiceSearch&SME=True

# Get these data points

# service name
# Service type
# website
# groups for
# Age groups
# what areas of city
# how can I access the service
# Who can refer me
# when is the service open
# cost
import requests
from bs4 import BeautifulSoup
import csv
import time
base_url = "https://www.thelivewelldirectory.com"
search_url = f"{base_url}/Search?start={{}}"
headers = {
    "User-Agent": "Mozilla/5.0"
}
services = []
# Scrape first few pages (adjust range as needed)
for page in range(1, 2):  # Assuming 10 results per page
    url = search_url.format(page)
    # print(f"url={url}")
    # exit()
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    print(soup.prettify())
    # for result in soup.select(".serviceTitle a"):
    #     service_link = base_url + result["href"]
    #     detail_res = requests.get(service_link, headers=headers)
    #     detail_soup = BeautifulSoup(detail_res.text, "html.parser")
    #     name = detail_soup.find("h1").text.strip()
    #     description = detail_soup.select_one(".serviceDetailsText").text.strip() if detail_soup.select_one(".serviceDetailsText") else "N/A"
    #     address = detail_soup.select_one(".addressText").text.strip() if detail_soup.select_one(".addressText") else "N/A"
    #     availability = "N/A"
    #     access = "N/A"
    #     for label in detail_soup.select(".serviceFieldLabel"):
    #         if "Opening Times" in label.text:
    #             availability = label.find_next("div").text.strip()
    #         if "How to access" in label.text:
    #             access = label.find_next("div").text.strip()
    #     services.append([name, description, address, availability, access])
    time.sleep(1)  # Be kind to the server
        

# Save to CSV
# with open("live_well_services.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Description", "Address", "Availability", "Access Method"])
#     writer.writerows(services)
# print(f"Scraped {len(services)} services.")