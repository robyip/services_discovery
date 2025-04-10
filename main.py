import requests
from bs4 import BeautifulSoup
from  dataclasses import dataclass, field
from typing import List

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

# From the live well directory found here  https://www.thelivewelldirectory.com/Search?CategoryId=122&SM=ServiceSearch&SME=True (Origina url shared by Simon)

BASE_URL = "https://www.thelivewelldirectory.com"
SEARCH_URL = f"{BASE_URL}/Search?CategoryId=122"
headers = {
    "User-Agent": "Mozilla/5.0"
}
result = requests.get(SEARCH_URL, headers=headers)

soup_searched_page = BeautifulSoup(result.content, "html.parser")

services = []
@dataclass
class Service:
    name: str
    service_type: str = field(default="")
    website: str = field(default="")
    groups_for: List[str] = field(default_factory=list)
    age_groups: List[str] = field(default_factory=list)
    areas_of_city: str = field(default="")
    access_service: str = field(default="")
    who_can_refer: str = field(default="")
    service_open: str = field(default="")
    cost: str = field(default="")
    source_base_url: str = field(default="")
    source_service_url: str = field(default="")
    

for service_link in soup_searched_page.find_all("a", class_="service-name bem-search-result-item__title bem-title bem-title--m"):
    print(service_link.get_text(strip=True))
    print(service_link["href"])  # Uncomment to see the href attribute
    service = Service(name=service_link.get_text(strip=True), source_base_url=BASE_URL, source_service_url=service_link["href"])
    # print(service)
    
    
    # Sub page for each service
    service_page_url = BASE_URL + service_link["href"]
    service_page_result = requests.get(service_page_url, headers=headers)
    service_page_soup = BeautifulSoup(service_page_result.content, "html.parser")

    # get Website link
    dt_elements = service_page_soup.find_all("dt", class_="bem-description-list__title")
    for dt in dt_elements:
        if dt.text == "Service Type:":
           service.service_type = dt.find_next("dd").text.strip()
        if dt.text == "Website:":
           service.website = dt.find_next("dd").find("a")["href"]
        if dt.text == "Group:":
           for grp in dt.find_next("dd").find_all("li"):
               service.groups_for.append(grp.text.strip())
        if dt.text == "Age Range:":
           for grp in dt.find_next("dd").find_all("li"):
               service.age_groups.append(grp.text.strip())    


    services.append(service)
    print(service)   
    # break
    
# print(services)

    

