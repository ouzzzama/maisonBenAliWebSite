import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

sections = soup.find_all("section", class_="premium-service-section")

if len(sections) >= 4:
    # --- Update Transport Voiture (Index 0) ---
    transport_sec = sections[0]
    img_wrap_trans = transport_sec.find("div", class_="service-image-wrap")
    if img_wrap_trans:
        img_wrap_trans.clear()
        img_wrap_trans["style"] = "display: flex; justify-content: center; align-items: center; transform: perspective(1000px) rotateY(-5deg); transition: transform 0.5s;"
        
        col_trans = soup.new_tag("div", style="display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 300px;")
        
        img_truck = soup.new_tag("img", src="assets/images/icons/truck.png", alt="Transport", style="width: 180px; filter: brightness(0) invert(1); drop-shadow(0 15px 25px rgba(0,0,0,0.3)); margin-bottom: 20px;")
        
        p_truck = soup.new_tag("p", style="font-size: 15px; line-height: 1.6; color: #ffffff; opacity: 0.95; font-weight: 500;")
        p_truck.string = "Livraison premium et sécurisée de votre véhicule dès votre arrivée."
        
        col_trans.append(img_truck)
        col_trans.append(p_truck)
        img_wrap_trans.append(col_trans)
        
    # --- Update Boost Style de Vie (Index 1) ---
    boost_sec = sections[1]
    img_wrap_boost = boost_sec.find("div", class_="service-image-wrap")
    if img_wrap_boost:
        img_wrap_boost.clear()
        img_wrap_boost["style"] = "display: flex; justify-content: center; align-items: flex-start; gap: 40px; transform: perspective(1000px) rotateY(5deg); transition: transform 0.5s;"
        
        # Icon 1
        col_boost1 = soup.new_tag("div", style="display: flex; flex-direction: column; align-items: center; text-align: center; flex: 1;")
        icon1 = soup.new_tag("img", src="assets/images/icons/work-life-balance.png", alt="Work Life Balance", style="width: 130px; filter: brightness(0) invert(1); drop-shadow(0 15px 25px rgba(0,0,0,0.3)); margin-bottom: 20px;")
        p_boost1 = soup.new_tag("p", style="font-size: 14px; line-height: 1.6; color: #ffffff; opacity: 0.95; font-weight: 500;")
        p_boost1.string = "Équilibre parfait entre productivité et détente absolue."
        col_boost1.append(icon1)
        col_boost1.append(p_boost1)
        
        # Icon 2
        col_boost2 = soup.new_tag("div", style="display: flex; flex-direction: column; align-items: center; text-align: center; flex: 1;")
        icon2 = soup.new_tag("img", src="assets/images/icons/effect.png", alt="Effect", style="width: 130px; filter: brightness(0) invert(1); drop-shadow(0 15px 25px rgba(0,0,0,0.3)); margin-bottom: 20px;")
        p_boost2 = soup.new_tag("p", style="font-size: 14px; line-height: 1.6; color: #ffffff; opacity: 0.95; font-weight: 500;")
        p_boost2.string = "Impact immédiat sur votre bien-être au quotidien."
        col_boost2.append(icon2)
        col_boost2.append(p_boost2)
        
        img_wrap_boost.append(col_boost1)
        img_wrap_boost.append(col_boost2)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Icons scaled down and paragraphs added underneath.")
