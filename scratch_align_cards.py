import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

combined = soup.find("section", class_="premium-service-combined")

if combined:
    # Remove old container class and inline styles
    container = combined.find("div", class_="container")
    if container:
        container["class"] = ["aligned-cards-wrapper"]
        
        # Add custom inline CSS to perfectly match the margins of .premium-service-section
        # The CSS for .premium-service-section has margin: 0 20px (mobile) and margin: 0 60px (desktop)
        # We can add this via style.css instead of inline to ensure media queries work.
        
with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Combined container replaced.")
