import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

sections = soup.find_all("section", class_="premium-service-section")

if len(sections) >= 3:
    target_section = sections[2] # 3rd section (Transport Voiture)
    
    # Ensure proper positioning and overlay styling
    target_section["style"] = "position: relative; padding: 100px 0; overflow: hidden;"
    target_section["class"] = [c for c in target_section["class"] if c != "text-dark"] + ["light-content"]
    
    # Check if video already exists
    if not target_section.find("video", class_="bg-video"):
        video_html = """
        <video autoplay muted loop playsinline class="bg-video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
            <source src="assets/videos/transport.mp4" type="video/mp4">
        </video>
        <div class="video-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 0;"></div>
        """
        video_soup = BeautifulSoup(video_html, "html.parser")
        
        target_section.insert(0, video_soup)
        
        # Bring container to front
        container = target_section.find("div", class_="container")
        if container:
            if not container.has_attr("style"):
                container["style"] = ""
            container["style"] += " position: relative; z-index: 1;"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Transport video background added.")
