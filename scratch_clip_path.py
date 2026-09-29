import re

file_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\assets\css\style.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the subtle curve ::after implementation
start_marker = "/* =========================================================================="
end_marker = "/* Mobile adjustments */\n@media (max-width: 768px) {\n    .curve-bottom::after {\n        bottom: -15px;\n        height: 30px;\n    }\n    .curve-bottom + section {\n        padding-top: 60px !important;\n    }\n}\n"

if "SUBTLE, PREMIUM CURVE IMPLEMENTATION" in content:
    # Safely clear out everything added in the last step
    content = content[:content.find("/* ==========================================================================\n   SUBTLE, PREMIUM CURVE IMPLEMENTATION")]

# Apply the mathematically perfect clip-path curve
clip_path_curve = """
/* ==========================================================================
   MATHEMATICALLY PERFECT CLIP-PATH CURVE
   (Works with background images, zero edge hooking, perfect subtlety)
   ========================================================================== */
.curve-bottom {
    /* 
       Center of ellipse: 50% X, -50% Y (far above the top edge so the top isn't clipped)
       Horizontal Radius: 200% (extremely wide so edges don't hook)
       Vertical Radius: 150% (reaches exactly 100% height at the bottom center)
    */
    clip-path: ellipse(200% 150% at 50% -50%) !important;
    -webkit-clip-path: ellipse(200% 150% at 50% -50%) !important;
    
    border-radius: 0 !important;
    margin-bottom: -4vw !important; /* Pull next section up to tuck under curve */
    padding-bottom: 8vw !important; /* Prevent text from being clipped by the curve */
    overflow: hidden !important; 
    z-index: 10;
    position: relative;
}

/* Ensure sections without explicit colors don't become invisible */
.curve-bottom:not(.gray-bg):not(.dark-bg) {
    background-color: var(--white-color, #ffffff);
}

/* Give the next section some padding so content doesn't get hidden under the overlapping curve */
.curve-bottom + section {
    padding-top: 6vw !important;
}

@media (max-width: 768px) {
    .curve-bottom {
        clip-path: ellipse(250% 150% at 50% -50%) !important;
        -webkit-clip-path: ellipse(250% 150% at 50% -50%) !important;
        margin-bottom: -30px !important;
        padding-bottom: 60px !important;
    }
    .curve-bottom + section {
        padding-top: 50px !important;
    }
}
"""

content = content + clip_path_curve

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Clip-path curve applied globally.")
