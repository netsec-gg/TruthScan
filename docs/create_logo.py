#!/usr/bin/env python3
"""
Simple script to generate a placeholder logo for TruthScan
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_truthscan_logo():
    # Create a new image with a dark background
    width, height = 800, 400
    image = Image.new('RGB', (width, height), color=(20, 22, 36))
    draw = ImageDraw.Draw(image)
    
    # Draw a header with the TruthScan name
    text = "TRUTHSCAN"
    # Try to use a font that's likely available, fallback to default
    try:
        font = ImageFont.truetype("Arial Bold", 80)
    except IOError:
        font = ImageFont.load_default()
    
    # Draw the main title
    text_width = draw.textlength(text, font=font)
    position = ((width - text_width) // 2, 60)
    draw.text(position, text, fill=(0, 255, 200), font=font)
    
    # Draw a subtitle
    subtitle = "OSINT Claim Verification"
    try:
        subtitle_font = ImageFont.truetype("Arial", 40)
    except IOError:
        subtitle_font = ImageFont.load_default()
    
    subtitle_width = draw.textlength(subtitle, font=subtitle_font)
    subtitle_position = ((width - subtitle_width) // 2, 160)
    draw.text(subtitle_position, subtitle, fill=(180, 180, 200), font=subtitle_font)
    
    # Draw a decorative line
    draw.line([(100, 220), (width - 100, 220)], fill=(0, 200, 255), width=2)
    
    # Add a tagline
    tagline = "Verify International Incidents Without Expensive APIs"
    try:
        tagline_font = ImageFont.truetype("Arial", 25)
    except IOError:
        tagline_font = ImageFont.load_default()
    
    tagline_width = draw.textlength(tagline, font=tagline_font)
    tagline_position = ((width - tagline_width) // 2, 250)
    draw.text(tagline_position, tagline, fill=(150, 150, 180), font=tagline_font)
    
    # Add a cyberpunk-style grid effect
    for i in range(0, width, 20):
        alpha = max(0, min(255, i // 2))
        draw.line([(i, 300), (i, height)], fill=(0, 100, 200, alpha), width=1)
    
    for i in range(300, height, 10):
        draw.line([(0, i), (width, i)], fill=(0, 100, 200, 50), width=1)
    
    # Save the image
    if not os.path.exists('docs'):
        os.makedirs('docs')
    image.save('docs/logo.png')
    print("Logo created successfully at docs/logo.png")

if __name__ == "__main__":
    create_truthscan_logo() 