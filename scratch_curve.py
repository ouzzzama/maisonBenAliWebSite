import re

file_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\assets\css\style.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific CSS block for .curve-bottom
old_block = """/* 1. Create the downward curve using border-radius */
.curve-bottom {
  border-radius: 0 0 50% 50% / 0 0 5vw 5vw !important;
  margin-bottom: -5vw !important; /* Pull the next section up to slide under the curve */
  padding-bottom: 5vw !important; /* Prevent the curve from clipping this section's own content */
  overflow: hidden !important;
}"""

new_block = """/* 1. Create the gentle curve using an oversized pseudo-element */
.curve-bottom {
  border-radius: 0 !important;
  margin-bottom: 0 !important; 
  padding-bottom: 5vw !important; /* Give content room above the curve */
  overflow: visible !important;
  position: relative;
}
.curve-bottom::after {
  content: "";
  position: absolute;
  bottom: -4vw; /* Hangs down */
  left: -50vw; /* Wide enough to push the sharp hooks completely off screen */
  width: 200vw;
  height: 8vw; /* Depth of curve */
  border-radius: 50%;
  background: inherit;
  background-color: inherit;
  pointer-events: none;
  z-index: 1; /* Place above the next section */
}"""

content = content.replace(old_block, new_block)

# Replace the responsive media query block
old_media = """.curve-bottom {
    border-radius: 0 0 50% 50% / 0 0 30px 30px !important;
    margin-bottom: -30px !important;
    padding-bottom: 30px !important;
  }"""
  
new_media = """.curve-bottom::after {
    bottom: -20px;
    height: 40px;
  }
  .curve-bottom {
    padding-bottom: 30px !important;
  }"""

content = content.replace(old_media, new_media)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Curve CSS updated!")
