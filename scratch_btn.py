import re

file_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\assets\css\style.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific border-radius line
old_line = "border-radius: 4px !important; /* Slightly rounded for modern \nprofessional look (away from generic pills) */"
old_line_alt = "border-radius: 4px !important; /* Slightly rounded for modern professional look (away from generic pills) */"

content = content.replace(old_line, "border-radius: 50px !important; /* Pill shape for premium modern look */")
content = content.replace(old_line_alt, "border-radius: 50px !important; /* Pill shape for premium modern look */")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Button corner radius updated.")
