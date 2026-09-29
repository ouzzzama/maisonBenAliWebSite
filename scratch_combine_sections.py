import os
from bs4 import BeautifulSoup

html_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\services.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

sections = soup.find_all("section", class_="premium-service-section")

if len(sections) >= 2:
    sec1 = sections[0]
    sec2 = sections[1]
    
    # Extract data for Achat
    vid1_src = sec1.find("source")["src"] if sec1.find("source") else ""
    tag1 = sec1.find("span", class_="step-label").get_text(strip=True) if sec1.find("span", class_="step-label") else "01. Service"
    title1 = sec1.find("h2", class_="title").get_text(strip=True) if sec1.find("h2", class_="title") else "Achat"
    p1 = sec1.find("p").decode_contents() if sec1.find("p") else ""
    btn1 = sec1.find("a", class_="theme-btn")["href"] if sec1.find("a", class_="theme-btn") else "contact.html"

    # Extract data for Location
    vid2_src = sec2.find("source")["src"] if sec2.find("source") else ""
    tag2 = sec2.find("span", class_="step-label").get_text(strip=True) if sec2.find("span", class_="step-label") else "02. Service"
    title2 = sec2.find("h2", class_="title").get_text(strip=True) if sec2.find("h2", class_="title") else "Location"
    p2 = sec2.find("p").decode_contents() if sec2.find("p") else ""
    btn2 = sec2.find("a", class_="theme-btn")["href"] if sec2.find("a", class_="theme-btn") else "contact.html"

    combined_html = f"""
    <section class="premium-service-combined" style="margin-bottom: 80px; padding: 0 20px;">
        <div class="container-fluid" style="max-width: 1400px;">
            <div class="row">
                <!-- Achat Card -->
                <div class="col-lg-6 mb-4 mb-lg-0" data-aos="fade-up" data-aos-duration="800">
                    <div class="premium-service-card light-content" style="position: relative; padding: 80px 50px; border-radius: 40px; overflow: hidden; height: 100%; box-shadow: 0 30px 60px rgba(0,0,0,0.08); display: flex; flex-direction: column; justify-content: center;">
                        <video autoplay muted loop playsinline class="bg-video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
                            <source src="{vid1_src}" type="video/mp4">
                        </video>
                        <div class="video-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.65); z-index: 0;"></div>
                        <div class="content-wrapper" style="position: relative; z-index: 1;">
                            <span class="step-label" style="display: inline-block; font-size: 14px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; opacity: 0.8; color: #fff;">{tag1}</span>
                            <h2 class="title" style="font-size: 48px; font-weight: 700; margin-bottom: 25px; color: #fff;">{title1}</h2>
                            <p style="font-size: 18px; line-height: 1.8; margin-bottom: 40px; opacity: 0.9; color: #fff;">{p1}</p>
                            <a href="{btn1}" class="theme-btn style-one" style="background-color: #fff; color: #111;">En savoir plus <i class="far fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
                <!-- Location Card -->
                <div class="col-lg-6" data-aos="fade-up" data-aos-duration="1000">
                    <div class="premium-service-card light-content" style="position: relative; padding: 80px 50px; border-radius: 40px; overflow: hidden; height: 100%; box-shadow: 0 30px 60px rgba(0,0,0,0.08); display: flex; flex-direction: column; justify-content: center;">
                        <video autoplay muted loop playsinline class="bg-video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0;">
                            <source src="{vid2_src}" type="video/mp4">
                        </video>
                        <div class="video-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.65); z-index: 0;"></div>
                        <div class="content-wrapper" style="position: relative; z-index: 1;">
                            <span class="step-label" style="display: inline-block; font-size: 14px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 15px; opacity: 0.8; color: #fff;">{tag2}</span>
                            <h2 class="title" style="font-size: 48px; font-weight: 700; margin-bottom: 25px; color: #fff;">{title2}</h2>
                            <p style="font-size: 18px; line-height: 1.8; margin-bottom: 40px; opacity: 0.9; color: #fff;">{p2}</p>
                            <a href="{btn2}" class="theme-btn style-one" style="background-color: #fff; color: #111;">En savoir plus <i class="far fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    
    combined_soup = BeautifulSoup(combined_html, "html.parser")
    
    # Replace sec1 with combined, and remove sec2
    sec1.replace_with(combined_soup)
    sec2.decompose()

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Achat and Location combined into one side-by-side section.")
