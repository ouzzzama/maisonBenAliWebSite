import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the premium service sections
sections = soup.find_all("section", class_="premium-service-section")

if sections:
    achat_section = sections[0]
    
    # Update classes and styles for video background
    achat_section["style"] = "position: relative; padding: 100px 0; overflow: hidden;"
    # Switch from text-dark to light-content for readability
    achat_section["class"] = [c for c in achat_section["class"] if c != "text-dark"] + ["light-content"]
    
    # Check if video already exists
    if not achat_section.find("video", class_="bg-video"):
        # Create video element
        video_html = """
        <video autoplay muted loop playsinline class="bg-video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
            <source src="https://videos.pexels.com/video-files/5044419/5044419-hd_1920_1080_30fps.mp4" type="video/mp4">
        </video>
        <div class="video-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 0;"></div>
        """
        video_soup = BeautifulSoup(video_html, "html.parser")
        
        # Insert video at the beginning of the section
        achat_section.insert(0, video_soup)
        
        # Ensure the container is above the video
        container = achat_section.find("div", class_="container")
        if container:
            if not container.has_attr("style"):
                container["style"] = ""
            container["style"] += " position: relative; z-index: 1;"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Video background added to Achat section.")
