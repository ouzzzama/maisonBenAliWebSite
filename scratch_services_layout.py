import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the old service section
old_section = soup.find("section", class_=lambda c: c and "renvia-service_one" in c)

if not old_section:
    print("Could not find the service section in services.html")
    exit()

# Extract the 6 cards data
cards = old_section.find_all("div", class_=lambda c: c and "renvia-service-card" in c)

new_titles = [
    "Achat",
    "Location",
    "Transport Voiture",
    "Boost Style de Vie",
    "Investissement VEFA",
    "Conseil & Patrimoine"
]

# Premium color palette for the 6 sections
colors = [
    ("#FFFFFF", "text-dark"),    # White
    ("#F4F5F8", "text-dark"),    # Soft Gray
    ("#1A2B4C", "light-content"),# Navy (White text)
    ("#FFFFFF", "text-dark"),    # White
    ("#C5A265", "light-content"),# Gold (White text)
    ("#111111", "light-content") # Rich Black (White text)
]

new_sections_html = ""

for i, card in enumerate(cards):
    title = new_titles[i] if i < len(new_titles) else "Service"
    
    # Extract data
    front = card.find("div", class_="flip-card-front")
    back = card.find("div", class_="flip-card-back")
    
    tag = "Service"
    if front:
        tag_span = front.find("span", class_="service-tag")
        if tag_span: tag = tag_span.get_text(strip=True)
        
    paragraph = ""
    img_src = ""
    link = "contact.html"
    
    if back:
        p_tag = back.find("p")
        if p_tag: paragraph = p_tag.decode_contents() # Keep strong tags inside
        
        img_tag = back.find("img")
        if img_tag: img_src = img_tag.get("src")
        
        a_tag = back.find("a", class_="icon-btn")
        if a_tag: link = a_tag.get("href")

    bg_color, theme_class = colors[i % len(colors)]
    
    # Alternate layout
    row_class = "flex-row-reverse" if i % 2 != 0 else ""
    
    # Build new section
    section_html = f"""
    <section class="premium-service-section {theme_class}" style="background-color: {bg_color}; padding: 100px 0; overflow: hidden;" data-aos="fade-up">
        <div class="container">
            <div class="row align-items-center {row_class}">
                <div class="col-lg-5 mb-5 mb-lg-0">
                    <div class="service-text-content">
                        <span class="step-label" style="display: inline-block; font-size: 14px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; opacity: 0.7;">0{i+1}. {tag}</span>
                        <h2 class="title" style="font-size: 42px; font-weight: 700; margin-bottom: 25px;">{title}</h2>
                        <p style="font-size: 18px; line-height: 1.8; margin-bottom: 35px; opacity: 0.9;">{paragraph}</p>
                        <a href="{link}" class="theme-btn style-one">En savoir plus <i class="far fa-arrow-right"></i></a>
                    </div>
                </div>
                <div class="col-lg-6 offset-lg-1">
                    <div class="service-image-wrap" style="border-radius: 20px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.15); transform: perspective(1000px) rotateY({'-5deg' if i%2!=0 else '5deg'}); transition: transform 0.5s;">
                        <img src="{img_src}" alt="{title}" style="width: 100%; height: auto; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    new_sections_html += section_html

# Replace the old section
new_soup = BeautifulSoup(new_sections_html, "html.parser")
old_section.replace_with(new_soup)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("services.html rewritten successfully.")
