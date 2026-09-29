import re
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

cards = soup.find_all("div", class_=lambda c: c and "renvia-service-card" in c and "flip-card" in c)

for card in cards:
    front = card.find("div", class_="flip-card-front")
    back = card.find("div", class_="flip-card-back")
    
    if front and back:
        # Check if already added
        if front.find("p", class_="front-paragraph"):
            continue
            
        p_back = back.find("p")
        if p_back:
            # Create a clone of the paragraph for the front
            p_front = soup.new_tag("p", style="margin-top: 15px; font-size: 14px; line-height: 1.6; color: var(--text-color); opacity: 0.9; text-align: left;")
            p_front["class"] = ["front-paragraph"]
            p_front.append(BeautifulSoup(p_back.decode_contents(), "html.parser"))
            
            hint = front.find("div", class_="flip-hint")
            if hint:
                hint.insert_after(p_front)
            else:
                front.append(p_front)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Paragraphs added to front faces.")
