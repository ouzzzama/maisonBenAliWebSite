import re
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the 4 service cards
cards = soup.find_all("div", class_=lambda c: c and "renvia-service-card" in c and "flip-card" in c)

for idx, card in enumerate(cards):
    front = card.find("div", class_="flip-card-front")
    back = card.find("div", class_="flip-card-back")
    
    if front and back:
        # Check if front already has an image
        if front.find("img", class_="front-service-img"):
            continue
            
        # Get the image from the back
        back_img = back.find("img")
        if back_img:
            img_src = back_img.get("src")
            
            # Create a new image element for the front
            img_wrap = soup.new_tag("div", style="margin: 25px 0; border-radius: 15px; overflow: hidden;")
            img_tag = soup.new_tag("img", src=img_src, alt="service image front", class_="front-service-img", style="width: 100%; height: 180px; object-fit: cover;")
            img_wrap.append(img_tag)
            
            # Insert it right before the flip-hint
            hint = front.find("div", class_="flip-hint")
            if hint:
                hint.insert_before(img_wrap)
            else:
                front.append(img_wrap)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Images added to front faces.")
