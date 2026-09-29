import re
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

new_titles = [
    "Achat",
    "Location",
    "Transport Voiture",
    "Boost Style de Vie"
]

cards = soup.find_all("div", class_=lambda c: c and "renvia-service-card" in c and "flip-card" in c)

for idx, card in enumerate(cards):
    if idx >= len(new_titles): break
    new_title_text = new_titles[idx]
    
    # 1. Update Front Title
    front = card.find("div", class_="flip-card-front")
    if front:
        title_h3 = front.find("h3", class_="card-title-big")
        if title_h3:
            title_h3.clear()
            title_h3.string = new_title_text
            
    # 2. Update Back Title
    back = card.find("div", class_="flip-card-back")
    if back:
        title_h4 = back.find("h4")
        if title_h4:
            a_tag = title_h4.find("a")
            if a_tag:
                # Keep the step number span if it exists
                step_span = a_tag.find("span", class_="step-label-num")
                a_tag.clear()
                if step_span:
                    a_tag.append(step_span)
                    a_tag.append(" " + new_title_text)
                else:
                    a_tag.string = new_title_text

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Titles updated successfully.")
