import re

file_path = r"C:\Users\soufi\Documents\projects\maisonBenAliWebSite-main\maisonBenAliWebSite-main\assets\css\style.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the aggressive flattening override I added
override_marker = "/* REMOVE ALL CURVES GLOBALLY */"
if override_marker in content:
    content = content[:content.find(override_marker)]

# Now, apply the highly subtle, wide curve override
subtle_curve_css = """
/* ==========================================================================
   SUBTLE, PREMIUM CURVE IMPLEMENTATION (No edge hooks, minimal depth)
   ========================================================================== */
.curve-bottom {
    border-radius: 0 !important;
    margin-bottom: 0 !important;
    padding-bottom: 5vw !important; /* Keep internal spacing */
    position: relative;
    overflow: visible !important;
}

/* The oversized pseudo-element hides the sharp border-radius edges off-screen */
.curve-bottom::after {
    content: "";
    position: absolute;
    bottom: -1.5vw; /* Just 1.5vw of curve depth hanging down */
    left: -50vw; /* Stretch it to 200vw wide so edges are completely invisible */
    width: 200vw;
    height: 3vw; /* Total ellipse height */
    border-radius: 50%;
    background: inherit; /* Copies parent background color */
    pointer-events: none;
    z-index: 10;
}

/* Ensure sections without explicit colors don't become invisible */
.curve-bottom:not(.gray-bg):not(.dark-bg) {
    background: var(--white-color, #ffffff);
}

/* Ensure next section has room for the subtle curve */
.curve-bottom + section {
    padding-top: calc(1.5vw + 80px) !important;
}

/* Mobile adjustments */
@media (max-width: 768px) {
    .curve-bottom::after {
        bottom: -15px;
        height: 30px;
    }
    .curve-bottom + section {
        padding-top: 60px !important;
    }
}
"""

content = content + subtle_curve_css

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Subtle curves applied globally.")
