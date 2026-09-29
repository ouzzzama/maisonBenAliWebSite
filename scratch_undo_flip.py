import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

project_list = soup.find("div", class_="renvia-proiect-list")
if project_list:
    cards = project_list.find_all("div", class_="flip-project-card")
    for card in cards:
        # Remove the class
        card["class"].remove("flip-project-card")
        
        # The inner html we want is inside .flip-project-front .project-card-content-wrap
        front_wrap = card.find("div", class_="flip-project-front")
        if front_wrap:
            content_wrap = front_wrap.find("div", class_="project-card-content-wrap")
            if content_wrap:
                inner_html = "".join([str(child) for child in content_wrap.contents])
                card.clear()
                card.append(BeautifulSoup(inner_html, "html.parser"))

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("HTML reverted successfully.")
