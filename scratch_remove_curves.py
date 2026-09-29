import re

file_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\assets\css\style.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the blocks to remove
blocks_to_remove = [
"""/* --- New Bottom Curve Implementation (Smooth, No Edge Hooks) --- */
  
  /* 1. Remove the old hooking border-radius and ensure overflow is visible so the curve can hang down */
  .curve-bottom {
    border-radius: 0 !important;
    margin-bottom: 0 !important; 
    overflow: visible !important;
    position: relative;
    /* Remove old negative margins so it doesn't break standard flow */
  }
  
  /* 2. Create the gentle curve using a massive off-screen ellipse */
  .curve-bottom::after {
    content: "";
    position: absolute;
    bottom: -5vw; /* Hangs down over the next section */
    left: -50vw; /* 200vw wide so the sharp hooks are 50vw off-screen */
    width: 200vw;
    height: 10vw; /* Total height of the ellipse */
    border-radius: 50%; /* Perfect ellipse */
    background: inherit; /* Copies the gray-bg, dark-bg, or white color */
    pointer-events: none; /* Let clicks pass through to the section below */
    /* z-index is handled by the main > section stacking context below */
  }
  
  /* Ensure sections without explicit background colors have white backgrounds */
  .curve-bottom:not(.gray-bg):not(.dark-bg) {
    background: var(--white-color, #ffffff);
  }""",
"""/* 1. Create the gentle curve using an oversized pseudo-element */
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
}
  
  /* Ensure sections without explicit background colors have white backgrounds, otherwise the curve is invisible (transparent on transparent) */
  .curve-bottom:not(.gray-bg):not(.dark-bg) {
    background-color: var(--white-color, #ffffff);
  }""",
"""/* 3. Automatically pad the content of the section that got pulled up, so it doesn't get hidden under the curve */
  .curve-bottom + section::before {
    content: "";
    display: block;
    height: 5vw;
    width: 100%;
  }""",
"""/* 4. Pad the content of the next section so the hanging curve doesn't hide text */
  .curve-bottom + section {
    padding-top: calc(5vw + 40px) !important;
  }""",
""".curve-bottom::after {
    bottom: -20px;
    height: 40px;
  }
  .curve-bottom {
    padding-bottom: 30px !important;
  }
    .curve-bottom + section::before {
      height: 30px;
    }""",
""".curve-bottom + section {
      padding-top: 70px !important;
    }""",
"""/* Fix for the footer and other sections being covered by the curve */
  main + footer::before {
    content: "";
    display: block;
    height: 5vw;
    width: 100%;
  }
  @media (max-width: 768px) {
    main + footer::before {
      height: 30px;
    }
  }"""
]

# We will just replace all instances of .curve-bottom with a flat override to ensure it's completely dead
override_css = """
/* REMOVE ALL CURVES GLOBALLY */
.curve-bottom {
    border-radius: 0 !important;
    margin-bottom: 0 !important;
    padding-bottom: 80px !important; /* Standard padding */
}
.curve-bottom::after, .curve-bottom::before {
    display: none !important;
}
.curve-bottom + section::before, main + footer::before {
    display: none !important;
}
.curve-bottom + section {
    padding-top: 80px !important; /* Standard padding */
}
"""

content = content + override_css

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("All curves officially neutralized globally.")
