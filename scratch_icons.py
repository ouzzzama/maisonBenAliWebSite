import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

sections = soup.find_all("section", class_="premium-service-section")

if len(sections) >= 4:
    # --- Transport Voiture ---
    transport_sec = sections[2]
    img_wrap = transport_sec.find("div", class_="service-image-wrap")
    if img_wrap:
        # Remove the box-shadow and border-radius so the icon floats freely
        img_wrap["style"] = "text-align: center; transform: perspective(1000px) rotateY(-5deg); transition: transform 0.5s;"
        img = img_wrap.find("img")
        if img:
            img["src"] = "assets/images/icons/truck.png"
            img["style"] = "width: 70%; height: auto; max-width: 400px; filter: brightness(0) invert(1); drop-shadow(0 20px 30px rgba(0,0,0,0.3));"
            
    # --- Boost Style de Vie ---
    boost_sec = sections[3]
    img_wrap2 = boost_sec.find("div", class_="service-image-wrap")
    if img_wrap2:
        img_wrap2["style"] = "display: flex; justify-content: center; align-items: center; gap: 40px; transform: perspective(1000px) rotateY(5deg); transition: transform 0.5s;"
        
        # Clear existing images
        img_wrap2.clear()
        
        # Add both icons
        icon1 = soup.new_tag("img", src="assets/images/icons/work-life-balance.png", alt="Work Life Balance", style="width: 45%; max-width: 250px; filter: brightness(0) invert(1); drop-shadow(0 20px 30px rgba(0,0,0,0.3));")
        icon2 = soup.new_tag("img", src="assets/images/icons/effect.png", alt="Effect", style="width: 45%; max-width: 250px; filter: brightness(0) invert(1); drop-shadow(0 20px 30px rgba(0,0,0,0.3));")
        
        img_wrap2.append(icon1)
        img_wrap2.append(icon2)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Icons swapped for Transport and Boost.")
