import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

colors = ["#1A2B4C", "#E63946", "#2A4D3E", "#C5A265"]
color_index = 0

project_list = soup.find("div", class_="renvia-proiect-list")
if project_list:
    cards = project_list.find_all("div", class_="renvia-project-item")
    for card in cards:
        if "flip-project-card" in card.get("class", []):
            continue # already processed
            
        card["class"].append("flip-project-card")
        
        # Extract children
        inner_html = "".join([str(child) for child in card.contents])
        card.clear()
        
        bg_color = colors[color_index % 4]
        color_index += 1
        
        # Build new structure
        new_structure = f"""
        <div class="flip-project-inner">
            <div class="flip-project-front">
                <div class="project-card-content-wrap">
                    {inner_html}
                </div>
            </div>
            <div class="flip-project-back" style="background-color: {bg_color};">
                <div class="project-card-content-wrap light-content">
                    {inner_html}
                </div>
            </div>
        </div>
        """
        card.append(BeautifulSoup(new_structure, "html.parser"))

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("HTML modified successfully.")
