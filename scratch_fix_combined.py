import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

combined_section = soup.find("section", class_="premium-service-combined")

if combined_section:
    # 1. Add top margin/padding to separate from Hero section
    combined_section["style"] = "margin-top: 100px; margin-bottom: 80px; padding: 0;"
    
    # 2. Change container-fluid to container to align with subsequent sections
    container = combined_section.find("div", class_="container-fluid")
    if container:
        container["class"] = ["container"]
        # Remove the max-width style so it naturally matches the standard Bootstrap container
        if container.has_attr("style"):
            del container["style"]
            
    # 3. Add gap between the two cards so they don't touch each other in the center (row gutter)
    # The row already handles standard gutters, but we can make the cards a bit more padded/spaced if needed.
    # Actually Bootstrap 5 has g-4 or g-5 for gap.
    row = combined_section.find("div", class_="row")
    if row:
        classes = row.get("class", [])
        if "g-5" not in classes:
            classes.append("g-5")
        row["class"] = classes

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Combined section spacing and alignment fixed.")
