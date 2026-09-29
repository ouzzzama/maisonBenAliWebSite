import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

sections = soup.find_all("section", class_="premium-service-section")

if len(sections) >= 4:
    # --- Revert Investissement VEFA (Index 2) ---
    invest_sec = sections[2]
    img_wrap_inv = invest_sec.find("div", class_="service-image-wrap")
    if img_wrap_inv:
        # Restore standard styling
        img_wrap_inv["style"] = "border-radius: 20px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.15); transform: perspective(1000px) rotateY(-5deg); transition: transform 0.5s;"
        img_wrap_inv.clear()
        img_inv = soup.new_tag("img", src="assets/images/innerpage/service/service-img5.jpg", alt="Investissement VEFA", style="width: 100%; height: auto; object-fit: cover;")
        img_wrap_inv.append(img_inv)

    # --- Revert Conseil & Patrimoine (Index 3) ---
    conseil_sec = sections[3]
    img_wrap_cons = conseil_sec.find("div", class_="service-image-wrap")
    if img_wrap_cons:
        img_wrap_cons["style"] = "border-radius: 20px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.15); transform: perspective(1000px) rotateY(5deg); transition: transform 0.5s;"
        img_wrap_cons.clear()
        img_cons = soup.new_tag("img", src="assets/images/innerpage/service/service-img6.jpg", alt="Conseil & Patrimoine", style="width: 100%; height: auto; object-fit: cover;")
        img_wrap_cons.append(img_cons)

    # --- Apply Icons to Transport Voiture (Index 0) ---
    transport_sec = sections[0]
    img_wrap_trans = transport_sec.find("div", class_="service-image-wrap")
    if img_wrap_trans:
        img_wrap_trans["style"] = "text-align: center; transform: perspective(1000px) rotateY(-5deg); transition: transform 0.5s;"
        img_wrap_trans.clear()
        img_truck = soup.new_tag("img", src="assets/images/icons/truck.png", alt="Truck", style="width: 70%; height: auto; max-width: 400px; filter: brightness(0) invert(1); drop-shadow(0 20px 30px rgba(0,0,0,0.3));")
        img_wrap_trans.append(img_truck)
        
    # --- Apply Icons to Boost Style de Vie (Index 1) ---
    boost_sec = sections[1]
    img_wrap_boost = boost_sec.find("div", class_="service-image-wrap")
    if img_wrap_boost:
        img_wrap_boost["style"] = "display: flex; justify-content: center; align-items: center; gap: 40px; transform: perspective(1000px) rotateY(5deg); transition: transform 0.5s;"
        img_wrap_boost.clear()
        icon1 = soup.new_tag("img", src="assets/images/icons/work-life-balance.png", alt="Work Life Balance", style="width: 45%; max-width: 250px; filter: brightness(0) invert(1); drop-shadow(0 20px 30px rgba(0,0,0,0.3));")
        icon2 = soup.new_tag("img", src="assets/images/icons/effect.png", alt="Effect", style="width: 45%; max-width: 250px; filter: brightness(0) invert(1); drop-shadow(0 20px 30px rgba(0,0,0,0.3));")
        img_wrap_boost.append(icon1)
        img_wrap_boost.append(icon2)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Icons corrected and applied to proper sections.")
